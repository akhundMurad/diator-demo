from dataclasses import dataclass, field
from diator.response import Response

from meetings.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class Participant:
    user_id: Identity
    greetings: str


@dataclass(frozen=True, kw_only=True)
class ReadParticipantsQueryResult(Response):
    meeting_id: Identity
    participants: list[Participant] = field(default_factory=list)
