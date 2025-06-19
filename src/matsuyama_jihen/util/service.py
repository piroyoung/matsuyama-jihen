from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional

from matsuyama_jihen.util.handler import Handler
from azure.eventhub import EventHubConsumerClient
from azure.eventhub import EventData
from azure.eventhub import PartitionContext

from matsuyama_jihen.util.model import ExampleMessage


class SubscriptionService(metaclass=ABCMeta):
    @abstractmethod
    def serve(self) -> None:
        pass


@dataclass(frozen=True)
class AzureEventHubSubscriptionService(SubscriptionService):
    handler: Handler
    client: EventHubConsumerClient

    def _on_event(
        self, partiton_context: PartitionContext, event: Optional[EventData]
    ) -> None:
        if event:
            body = event.body_as_str()

            # Deserialize the JSON body into an ExampleMessage
            m: ExampleMessage = ExampleMessage.model_validate_json(body)
            self.handler.handle(m)

    def serve(self) -> None:
        self.client.receive(on_event=self._on_event)
