from diator.requests import RequestHandler
from diator.events import Event

from meetings.application.common.ports.gateways.participant_gateway import ParticipantGatewayPort

from .join_meeting_command import JoinMeetingCommand
from .user_joined_ecst_event import UserJoinedECSTEvent


class JoinMeetingCommandHandler(RequestHandler[JoinMeetingCommand, None]):
    def __init__(self, participant_gateway: ParticipantGatewayPort) -> None:
        self._participant_gateway = participant_gateway
        self.events: list[Event] = []

    async def handle(self, request: JoinMeetingCommand) -> None:
        await self._participant_gateway.insert(user_id=request.user_id, meeting_id=request.meeting_id, greetings=request.greetings)
        self.events.append(UserJoinedECSTEvent(meeting_id=request.meeting_id, new_user_id=request.user_id))
