from azure.identity import DefaultAzureCredential
from azure.eventhub import EventHubProducerClient

from matsuyama_jihen.util.model import ExampleMessage
from matsuyama_jihen.util.publisher import AzureEventHubPublisher


EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "matsuyama.servicebus.windows.net"
EVENT_HUB_NAME = "example"


if __name__ == "__main__":
    credential = DefaultAzureCredential()
    client = EventHubProducerClient(
        fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
        eventhub_name=EVENT_HUB_NAME,
        credential=credential,
    )

    publisher = AzureEventHubPublisher(client=client)

    messages = [
        ExampleMessage.of_body("First event"),
        ExampleMessage.of_body("Second event"),
        ExampleMessage.of_body("Third event"),
    ]
    publisher.publish_messages(messages)

    credential.close()
