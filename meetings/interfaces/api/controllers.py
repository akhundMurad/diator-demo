from uuid import UUID

from blacksheep import FromJSON, Response, accepted
from blacksheep.server.controllers import APIController, get, post
from diator.mediator import Mediator

from meetings.application.join_meeting import JoinMeetingCommand
from meetings.application.read_participants import (
    ReadParticipantsQuery,
    ReadParticipantsQueryResult,
)
from meetings.domain.common.identity import Identity


class Participants(APIController):
    @get("/{meeting_id}")
    async def read_participants(self, meeting_id: UUID, mediator: Mediator) -> ReadParticipantsQueryResult:
        query = ReadParticipantsQuery(meeting_id=Identity(meeting_id))
        query_result = await mediator.send(query)
        return query_result


class Meeting(APIController):
    @post("/join/")
    async def join_meeting(self, body: FromJSON[JoinMeetingCommand], mediator: Mediator) -> Response:
        command = body.value
        await mediator.send(command)
        return accepted()
