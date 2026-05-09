import socket
import json
from lamport_clock import LamportClock
from security import CryptoLayer

class MessageStub:
    def __init__(self, client_id, host='localhost', port=5000):
        self.client_id = client_id
        self.server_addr = (host, port)
        self.clock = LamportClock()
        self.crypto = CryptoLayer(key=b'CG7LiijgRx5USt1s0_W-dj2ikXqmcYXnJ5man6qnbn8=') # Exemplo fixo

    def send_message(self, content, mode="broadcast", target=None):
        """Encapsula e cifra a mensagem antes do envio[cite: 34]."""
        encrypted_payload = self.crypto.encrypt(content)
        msg_id = f"MSG_{self.clock.tick()}_{self.client_id}"
        
        data = {
            "action": "produce",
            "id": msg_id,
            "sender_id": self.client_id,
            "payload": encrypted_payload,
            "timestamp": self.clock.value,
            "mode": mode,
            "target": target
        }
        return self._transmit(data)

    def receive_message(self):
        data = {"action": "consume", "consumer_id": self.client_id}
        response = self._transmit(data)
        
        if response.get("payload"):
            # Decifra ao receber [cite: 34]
            response['payload'] = self.crypto.decrypt(response['payload'])
            self.clock.update(response['timestamp'])
        return response

    def _transmit(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(self.server_addr)
            s.sendall(json.dumps(data).encode())
            return json.loads(s.recv(4096).decode())