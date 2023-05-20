from blacksheep import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from diator.mediator import Mediator
from openapidocs.v3 import Info

from meetings.application.mediator import build_mediator
from meetings.di import build_container

from .controllers import Meeting, Participants  # noqa


def build_asgi() -> Application:
    container = build_container()
    mediator = build_mediator(external_container=container)
    container.register(Mediator, instance=mediator)

    app = Application(services=container)

    docs = OpenAPIHandler(info=Info(title="Meetings API", version="0.0.1"))
    docs.bind_app(app)

    return app
