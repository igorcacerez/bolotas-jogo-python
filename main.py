import asyncio
from scripts.startgame import StartGame

if __name__ == "__main__":
    game = StartGame()
    asyncio.run(game.run())