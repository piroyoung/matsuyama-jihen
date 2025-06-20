from typing import List
from azure.identity import DefaultAzureCredential
from azure.eventhub import EventHubProducerClient

from matsuyama_jihen.util.model import ExampleMessage
from matsuyama_jihen.util.publisher import AzureEventHubPublisher, Publisher


EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "matsuyama.servicebus.windows.net"
EVENT_HUB_NAME = "example"


if __name__ == "__main__":
    credential = DefaultAzureCredential()
    try:
        client = EventHubProducerClient(
            fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
            eventhub_name=EVENT_HUB_NAME,
            credential=credential,
        )

        publisher: Publisher = AzureEventHubPublisher(client=client)

        messages: List[ExampleMessage] = [
            ExampleMessage.of_body("First event"),
            ExampleMessage.of_body("Second event"),
            ExampleMessage.of_body("Third event"),
        ]
        publisher.publish_messages(messages)

    finally:
        credential.close()
