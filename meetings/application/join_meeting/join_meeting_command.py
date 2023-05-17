from dataclasses import dataclass

from diator.requests import Request

from meetings.domain.common.identity import Identity


@dataclass(frozen=True, kw_only=True)
class JoinMeetingCommand(Request):
    meeting_id: Identity
    user_id: Identity
    greetings: str
