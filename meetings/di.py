from rodi import ActivationScope, Container, ServiceLifeStyle
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from meetings.adapters.persistence.gateways import ParticipantGateway
from meetings.adapters.persistence.persistence_manager import PersistenceManager
from meetings.application.common.ports.gateways import ParticipantGatewayPort
from meetings.application.join_meeting import JoinMeetingCommandHandler
from meetings.application.read_participants import ReadParticipantsQueryHandler
from meetings.config import DatabaseConfig


def provide_sa_engine(scope: ActivationScope) -> AsyncEngine:
    config: DatabaseConfig = scope.provider.get(DatabaseConfig)

    return create_async_engine(config.connection_string)


def provide_sa_sessionmaker(scope: ActivationScope) -> sessionmaker:
    engine = scope.provider.get(AsyncEngine)

    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def provide_persistence_manager(scope: ActivationScope) -> PersistenceManager:
    session_factory = scope.provider.get(sessionmaker)
    return PersistenceManager(session_factory=session_factory)


def provide_database_config(scope: ActivationScope) -> DatabaseConfig:
    return DatabaseConfig()


def build_container() -> Container:
    container = Container()

    container.register_factory(provide_database_config, DatabaseConfig, life_style=ServiceLifeStyle.TRANSIENT)
    container.register_factory(provide_sa_engine, AsyncEngine, life_style=ServiceLifeStyle.TRANSIENT)
    container.register_factory(provide_sa_sessionmaker, sessionmaker, life_style=ServiceLifeStyle.TRANSIENT)
    container.register_factory(provide_persistence_manager, PersistenceManager, life_style=ServiceLifeStyle.TRANSIENT)

    container.bind_types(ParticipantGatewayPort, ParticipantGateway)

    container.register(JoinMeetingCommandHandler)
    container.register(ReadParticipantsQueryHandler)

    return container
