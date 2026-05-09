import socket
import threading
import json
from lamport_clock import LamportClock

class MsgQMgr:
    def __init__(self, host='localhost', port=5000):
        self.buffer = []
        self.lock = threading.Lock()
        self.clock = LamportClock()
        self.host = host
        self.port = port
        self.log_file = "audit.log"

    def write_log(self, msg_id, l_time, p_id, c_id="PENDING"):
        """Gera log persistente para auditoria[cite: 35, 58]."""
        with open(self.log_file, "a") as f:
            log_entry = f"ID:{msg_id} | L_Time:{l_time} | Prod:{p_id} | Cons:{c_id}\n"
            f.write(log_entry)

    def handle_client(self, conn, addr):
        while True:
            try:
                data = conn.recv(4096).decode()
                if not data: break
                
                request = json.loads(data)
                action = request.get("action")

                if action == "produce":
                    self.process_production(request)
                    conn.send(json.dumps({"status": "OK"}).encode())
                
                elif action == "consume":
                    msg = self.process_consumption(request)
                    conn.send(json.dumps(msg).encode())

            except Exception as e:
                print(f"Erro na conexão: {e}")
                break
        conn.close()

    def process_production(self, req):
        with self.lock: # Exclusão Mútua [cite: 40]
            # Atualiza relógio com o tempo do produtor
            self.clock.update(req['timestamp'])
            msg_data = {
                "id": req['id'],
                "payload": req['payload'],
                "producer": req['sender_id'],
                "mode": req['mode'], # unicast/multicast/broadcast [cite: 31]
                "target": req.get('target'),
                "timestamp": self.clock.value
            }
            self.buffer.append(msg_data)
            self.buffer.sort(key=lambda x: x['timestamp']) # Ordenação total [cite: 25]
            self.write_log(msg_data['id'], msg_data['timestamp'], msg_data['producer'])

    def process_consumption(self, req):
        with self.lock:
            if not self.buffer: return {"status": "EMPTY"}
            
            # Lógica simples de consumo (FIFO ordenada)
            # Para Unicast/Multicast, haveria filtro por 'target'
            msg = self.buffer.pop(0)
            self.clock.tick()
            self.write_log(msg['id'], self.clock.value, msg['producer'], req['consumer_id'])
            return msg

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Middleware rodando em {self.host}:{self.port}...")
        while True:
            conn, addr = server.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    MsgQMgr().start()