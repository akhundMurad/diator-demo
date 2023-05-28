from meetings.adapters.persistence.persistence_manager import PersistenceManager
from meetings.application.common.dto.participant import ParticipantDTO
from meetings.application.common.ports.gateways import ParticipantGatewayPort
from meetings.domain.common.identity import Identity


class ParticipantGateway(ParticipantGatewayPort):
    def __init__(self, persistence_manager: PersistenceManager) -> None:
        self._persistence_manager = persistence_manager

    async def insert(self, *, user_id: Identity, meeting_id: Identity, greetings: str) -> None:
        statement = """
        INSERT INTO participants(user_id, meeting_id, greetings)
        VALUES(:user_id, :meeting_id, :greetings)
        """
        async with self._persistence_manager as persistence_manager:
            await persistence_manager.execute(
                statement,
                user_id=user_id.value,
                meeting_id=meeting_id.value,
                greetings=greetings,
            )
            await persistence_manager.commit()

    async def find_by_meeting_id(self, *, meeting_id: Identity) -> list[ParticipantDTO]:
        statement = """
        SELECT user_id, greetings FROM participants
        WHERE meeting_id = :meeting_id
        """
        participants = []
        async with self._persistence_manager as persistence_manager:
            rows = await persistence_manager.execute(statement, meeting_id=meeting_id.value)
            for row in rows:
                participants.append(ParticipantDTO(user_id=row[0], greetings=row[1]))
            await persistence_manager.commit()

        return participants
