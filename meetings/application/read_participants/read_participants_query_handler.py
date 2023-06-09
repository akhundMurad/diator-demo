from diator.events import Event
from diator.requests import RequestHandler

from meetings.application.common.ports.gateways import ParticipantGatewayPort

from .read_participants_query import ReadParticipantsQuery
from .read_participants_query_result import Participant, ReadParticipantsQueryResult


class ReadParticipantsQueryHandler(RequestHandler[ReadParticipantsQuery, ReadParticipantsQueryResult]):
    def __init__(self, participant_gateway: ParticipantGatewayPort) -> None:
        self._participant_gateway = participant_gateway
        self._events: list[Event] = []

    @property
    def events(self) -> list[Event]:
        return self._events

    async def handle(self, request: ReadParticipantsQuery) -> ReadParticipantsQueryResult:
        query_result = ReadParticipantsQueryResult(meeting_id=request.meeting_id, participants=[])

        participants = await self._participant_gateway.find_by_meeting_id(meeting_id=request.meeting_id)

        for participant in participants:
            query_result.participants.append(Participant(user_id=participant.user_id, greetings=participant.greetings))

        return query_result
