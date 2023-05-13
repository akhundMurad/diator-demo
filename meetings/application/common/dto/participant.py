from dataclasses import dataclass

from meetings.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class ParticipantDTO:
    user_id: Identity
    greetings: str
