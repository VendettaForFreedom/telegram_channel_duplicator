from loguru import logger
import colorama
import os
import sys
import asyncio

from telegram_channel_duplicator.duplicator import Duplicator


async def main():
    logger.remove()
    logger.add(
        sys.stderr,
        format="<cyan>{time}</cyan> | <lvl>{level}</lvl> - <lvl>{message}</lvl>",
        colorize=True,
        level="DEBUG",
    )

    logger.add(
        os.path.join("logs", "debug.log"),
        format="{time} {level} {message}",
        level="DEBUG",
        rotation="3mb",
        compression="zip",
    )
    logger.info(colorama.Fore.LIGHTYELLOW_EX + "Created by https://github.com/deFiss")

    duplicator = Duplicator()
    await duplicator.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())  # Schedule main() to run
    loop.run_forever()
