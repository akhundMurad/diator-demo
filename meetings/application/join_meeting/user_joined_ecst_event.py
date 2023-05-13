from dataclasses import dataclass
from diator.events import ECSTEvent

from meetings.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class UserJoinedECSTEvent(ECSTEvent):
    meeting_id: Identity
    new_user_id: Identity
