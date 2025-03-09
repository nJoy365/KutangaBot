from motor.motor_asyncio import AsyncIOMotorClient
import os
from logging import Logger


class Database:
    def __init__(self, logger: Logger = None):
        self.logger = logger
        self.DB_USER = str(os.getenv("MONGO_USER"))
        self.DB_PASSWORD = str(os.getenv("MONGO_PASSWORD"))
        self.DB_HOST = str(os.getenv("MONGO_HOST"))
        self.DB_PORT = int(os.getenv("MONGO_PORT"))
        self.DB_NAME = str(os.getenv("DB_NAME"))
        self.DB_AUTH = str(os.getenv("MONGO_AUTH"))
        self.CONNECTION_STRING = f"mongodb://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/?authSource={self.DB_NAME}"
        self.client = AsyncIOMotorClient(self.CONNECTION_STRING)
        self.db = self.client[self.DB_NAME]

    async def test(self):
        try:
            await self.client.admin.command("ping")
            await self.logger.info(message=f"Connected to database {self.db.name}")
        except Exception as e:
            await self.logger.error(
                message=f"Failed to connect to database {self.db.name}"
            )
            await self.logger.error(message=e)

    async def get_user(self, user_id: int) -> dict:
        docs = await self.db.users.find_one({"user_id": user_id})
        return docs if docs is not None else {}

    async def get_guild(self, guild_id: int) -> dict:
        docs = await self.db.guilds.find_one({"guild_id": guild_id})
        return docs if docs is not None else {}
