from abc import ABCMeta, abstractmethod

from matsuyama_jihen.util.model import ExampleMessage


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, message: ExampleMessage) -> None:
        pass


class PrintHandler(Handler):
    def handle(self, message: ExampleMessage) -> None:
        print(f"Received message: {message.model_dump_json()}")
