import logging

from sqlalchemy import Result, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


class PersistenceManager:
    def __init__(self, session_factory: sessionmaker) -> None:
        self._session_factory = session_factory

    async def __aenter__(self) -> "PersistenceManager":
        self._session: AsyncSession = self._session_factory()  # type: ignore
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            logging.error("Handled exception: %s - %s", exc_type, exc_val)
            await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def execute(self, statement: str, **params) -> Result:
        return await self._session.execute(text(statement), params)
