import threading

class LamportClock:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def tick(self):
        """Incrementa o relógio para eventos internos/envio."""
        with self.lock:
            self.value += 1
            return self.value

    def update(self, received_time):
        """Sincroniza o relógio com base no tempo recebido (Deitel 17.4)."""
        with self.lock:
            self.value = max(self.value, received_time) + 1
            return self.value