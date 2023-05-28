import os
from typing import Generator

import pytest
from rodi import Container, ServiceLifeStyle
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import close_all_sessions
from testcontainers.postgres import PostgresContainer

from meetings.di import build_container


@pytest.fixture(scope="session")
def postgresql_test_container() -> Generator[PostgresContainer, None, None]:
    container = PostgresContainer("postgres:15.3", driver="asyncpg")
    if os.name == "nt":
        container.get_container_host_ip = lambda: "localhost"
    try:
        container.start()
        yield container
    finally:
        container.stop()


@pytest.fixture(scope="session")
def engine_test(postgresql_test_container: PostgresContainer) -> AsyncEngine:
    connection_string = postgresql_test_container.get_connection_url()
    return create_async_engine(connection_string)


@pytest.fixture(scope="session")
def sessionmaker_test(
    engine_test: AsyncEngine,
) -> Generator[async_sessionmaker, None, None]:
    session_maker = async_sessionmaker(bind=engine_test, expire_on_commit=False, autoflush=False)
    yield session_maker
    close_all_sessions()


@pytest.fixture(scope="session")
def di_container_test(engine_test: AsyncEngine, sessionmaker_test: async_sessionmaker) -> Container:
    di_container = build_container()

    di_container.register_factory(lambda: engine_test, AsyncEngine, life_style=ServiceLifeStyle.TRANSIENT)
    di_container.register_factory(
        lambda: sessionmaker_test,
        async_sessionmaker,
        life_style=ServiceLifeStyle.TRANSIENT,
    )

    return di_container
