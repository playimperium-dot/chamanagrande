
class Client:
    def __init__(self, *args, **kwargs):
        print("[BLOQUEADO] Filestack desativado.")

    def upload(self, *args, **kwargs):
        raise RuntimeError("Upload bloqueado por seguranca.")
