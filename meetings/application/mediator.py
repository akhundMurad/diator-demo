from diator.mediator import Mediator
from diator.requests import RequestMap
from diator.container.rodi import RodiContainer

from meetings.di import build_container
from meetings.application.join_meeting import JoinMeetingCommand, JoinMeetingCommandHandler
from meetings.application.read_participants import ReadParticipantsQuery, ReadParticipantsQueryHandler


def get_container() -> RodiContainer:
    external_container = build_container()

    rodi_container = RodiContainer()
    rodi_container.attach_external_container(external_container)

    return rodi_container



def build_mediator() -> Mediator:
    container = get_container()
    request_map = RequestMap()
    request_map.bind(JoinMeetingCommand, JoinMeetingCommandHandler)
    request_map.bind(ReadParticipantsQuery, ReadParticipantsQueryHandler)

    return Mediator(request_map=request_map, container=container)
