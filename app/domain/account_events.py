from app.domain.event import Event


class AccountOpened(Event):

    def __init__(self, stream_id, stream_version):
        super().__init__(stream_id, stream_version)

    def to_payload(self):
        return {}



class Deposited(Event):

    def __init__(self, stream_id, stream_version, amount):
        super().__init__(stream_id, stream_version)

        self._amount = amount

    def get_amount(self):
        return self._amount

    def to_payload(self):
        return {
            "amount": self._amount
        }



class Withdrawn(Event):

    def __init__(self, stream_id, stream_version, amount):
        super().__init__(stream_id, stream_version)

        self._amount = amount

    def get_amount(self):   
        return self._amount

    def to_payload(self):
        return {
            "amount": self._amount
        }