from diator.container.rodi import RodiContainer
from diator.mediator import Mediator
from diator.requests import RequestMap
from rodi import Container

from meetings.application.join_meeting import (
    JoinMeetingCommand,
    JoinMeetingCommandHandler,
)
from meetings.application.read_participants import (
    ReadParticipantsQuery,
    ReadParticipantsQueryHandler,
)


def build_mediator(external_container: Container) -> Mediator:
    request_map = RequestMap()
    request_map.bind(JoinMeetingCommand, JoinMeetingCommandHandler)
    request_map.bind(ReadParticipantsQuery, ReadParticipantsQueryHandler)

    rodi_container = RodiContainer()
    rodi_container.attach_external_container(external_container)

    return Mediator(request_map=request_map, container=rodi_container)
