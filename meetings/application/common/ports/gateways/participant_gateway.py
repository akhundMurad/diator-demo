from typing import Protocol

from meetings.domain.common.identity import Identity


class ParticipantGatewayPort(Protocol):
    async def insert(self, *, user_id: Identity, meeting_id: Identity, greetings: str) -> None:
        ...
