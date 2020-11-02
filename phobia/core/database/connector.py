from motor import motor_asyncio

from phobia.core.config.database import DataBaseConfig


class Mongo:
    def __init__(self):
        self._client = motor_asyncio.AsyncIOMotorClient(DataBaseConfig.URI, connect=True)
        self._db = self._client[DataBaseConfig.NAME]

    @property
    def db(self):
        return self._db

    @property
    def client(self):
        return self._client

    async def ping(self):
        return await self.client.admin.command("ping")

    def close(self):
        self._client.close()


mongo = Mongo()
