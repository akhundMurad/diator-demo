import base64
import dataclasses
import json
from datetime import date, datetime, time
from enum import Enum
from typing import Any
from uuid import UUID

from meetings.domain.common.identity import Identity


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return json.JSONEncoder.default(self, obj)
        except TypeError:
            if hasattr(obj, "dict"):
                return obj.dict()
            if isinstance(obj, time):
                return obj.strftime("%H:%M:%S")
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, date):
                return obj.strftime("%Y-%m-%d")
            if isinstance(obj, bytes):
                return base64.urlsafe_b64encode(obj).decode("utf8")
            if isinstance(obj, UUID):
                return str(obj)
            if isinstance(obj, Enum):
                return obj.value
            if isinstance(obj, Identity):
                return obj.value
            if dataclasses.is_dataclass(obj):
                return dataclasses.asdict(obj)
            raise


def dumps(obj: Any) -> str:
    return json.dumps(obj, separators=(",", ":"), cls=JsonEncoder)


def pretty_dumps(obj: Any) -> str:
    return json.dumps(obj, indent=4, cls=JsonEncoder)
