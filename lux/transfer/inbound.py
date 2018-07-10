import jsonpickle

from lux.transfer import DTO


class GroupMeMessage(DTO):
    def __init__(self, author="", text=""):
        super().__init__()
        self._author = author
        self._text = text

    @property
    def author(self):
        return self._author

    @property
    def text(self):
        return self._text

    @classmethod
    def from_dict(cls, d):
        return cls(d["author"], d["text"])

    @classmethod
    def from_json(cls, json):
        return GroupMeMessage.from_dict(jsonpickle.decode(json, classes=dict))