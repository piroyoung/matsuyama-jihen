from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import List
from azure.eventhub import EventData
from azure.eventhub import EventHubProducerClient

from .model import ExampleMessage


class Publisher(metaclass=ABCMeta):
    @abstractmethod
    def publish_message(self, message: ExampleMessage) -> None:
        pass

    @abstractmethod
    def publish_messages(self, messages: List[ExampleMessage]) -> None:
        pass


@dataclass(frozen=True)
class AzureEventHubPublisher(Publisher):
    client: EventHubProducerClient

    def publish_messages(self, messages: List[ExampleMessage]) -> None:
        event_data_batch = self.client.create_batch()
        for message in messages:
            try:
                event_data_batch.add(EventData(message.model_dump_json()))
            except BatchFullError:
                self.client.send_batch(event_data_batch)
                event_data_batch = self.client.create_batch()
                event_data_batch.add(EventData(message.model_dump_json()))
        self.client.send_batch(event_data_batch)

    def publish_message(self, message: ExampleMessage) -> None:
        self.publish_messages([message])
