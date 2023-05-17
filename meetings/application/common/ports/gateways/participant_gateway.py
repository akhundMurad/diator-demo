from typing import Protocol

from meetings.application.common.dto.participant import ParticipantDTO
from meetings.domain.common.identity import Identity


class ParticipantGatewayPort(Protocol):
    async def insert(self, *, user_id: Identity, meeting_id: Identity, greetings: str) -> None:
        raise NotImplementedError

    async def find_by_meeting_id(self, *, meeting_id: Identity) -> list[ParticipantDTO]:
        raise NotImplementedError
