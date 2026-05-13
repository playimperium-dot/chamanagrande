import os


class Config:
    # Você pode preencher aqui diretamente ou usar variáveis de ambiente.
    # API_ID precisa ser número inteiro.
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    PHONE_NUMBER = os.getenv("PHONE_NUMBER", "+5599999999999")

    # Nome do arquivo de sessão que será criado pelo Telethon.
    NAME = os.getenv("SESSION_NAME", "channel_clone")

    # IDs precisam começar com -100 para canais/supergrupos privados.
    SRC_CHAT_ID = int(os.getenv("SRC_CHAT_ID", "-1001234567890"))
    DEST_CHAT_ID = int(os.getenv("DEST_CHAT_ID", "-1001234567891"))

    # Pausa a cada BATCH_SIZE mensagens para reduzir risco de flood wait.
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", "40"))
    BATCH_SLEEP = int(os.getenv("BATCH_SLEEP", "3"))
