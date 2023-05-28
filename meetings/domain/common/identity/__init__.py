from .protocol import IdentityProtocol
from .uuid import UUIDIdentity

Identity = UUIDIdentity


__all__ = ("Identity", "IdentityProtocol")
