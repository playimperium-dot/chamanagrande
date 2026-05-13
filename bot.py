import asyncio

from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.types import MessageService

from config import Config as BOT_SETTING


def validate_config() -> None:
    if not BOT_SETTING.API_ID:
        raise ValueError("Configure API_ID em config.py ou na variável de ambiente API_ID.")
    if not BOT_SETTING.API_HASH:
        raise ValueError("Configure API_HASH em config.py ou na variável de ambiente API_HASH.")
    if not BOT_SETTING.PHONE_NUMBER or BOT_SETTING.PHONE_NUMBER == "+5599999999999":
        raise ValueError("Configure PHONE_NUMBER com seu número real, incluindo o código do país.")


async def main() -> None:
    validate_config()

    client = TelegramClient(
        BOT_SETTING.NAME,
        BOT_SETTING.API_ID,
        BOT_SETTING.API_HASH,
        flood_sleep_threshold=60,
    )

    await client.start(phone=BOT_SETTING.PHONE_NUMBER)

    forwarded = 0
    skipped = 0

    print("Iniciando cópia das mensagens...")

    async for message in client.iter_messages(BOT_SETTING.SRC_CHAT_ID, reverse=True):
        if isinstance(message, MessageService):
            skipped += 1
            continue

        try:
            # Envia uma cópia sem cabeçalho de encaminhado.
            await client.send_message(BOT_SETTING.DEST_CHAT_ID, message)
            forwarded += 1
            print(f"Copiadas: {forwarded} | Ignoradas: {skipped}")

            if forwarded % BOT_SETTING.BATCH_SIZE == 0:
                await asyncio.sleep(BOT_SETTING.BATCH_SLEEP)

        except FloodWaitError as exc:
            wait_seconds = int(exc.seconds) + 1
            print(f"FloodWait: aguardando {wait_seconds}s...")
            await asyncio.sleep(wait_seconds)

        except Exception as exc:
            print(f"Erro ao copiar mensagem {getattr(message, 'id', '?')}: {exc}")
            await asyncio.sleep(5)

    await client.disconnect()
    print(f"Finalizado. Copiadas: {forwarded} | Ignoradas: {skipped}")


if __name__ == "__main__":
    asyncio.run(main())
