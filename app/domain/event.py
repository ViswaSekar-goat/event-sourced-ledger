from abc import ABC, abstractmethod
from datetime import datetime, timezone


class Event(ABC):

    def __init__(self, stream_id, stream_version):
        self._stream_id = stream_id
        self._stream_version = stream_version
        self._created_at = datetime.now(timezone.utc)

    @property
    def stream_id(self):
        return self._stream_id

    @property
    def stream_version(self):
        return self._stream_version

    @property
    def created_at(self):
        return self._created_at

    @property
    def event_type(self):
        return self.__class__.__name__

    def get_stream_id(self):
        return self.stream_id

    def get_stream_version(self):
        return self.stream_version

    def get_created_at(self):
        return self.created_at

    def get_event_type(self):
        return self.event_type

    @abstractmethod
    def to_payload(self):
        pass
