from abc import ABC
from abc import abstractmethod




class step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, Input):
        pass


class StepException(Exception):
        pass
