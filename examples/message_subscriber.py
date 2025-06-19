from azure.identity import DefaultAzureCredential
from azure.eventhub import EventHubConsumerClient

from matsuyama_jihen.util.handler import PrintHandler
from matsuyama_jihen.util.service import AzureEventHubSubscriptionService

EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "matsuyama.servicebus.windows.net"
EVENT_HUB_NAME = "example"
CONSUMER_GROUP = "example"


if __name__ == "__main__":
    credential = DefaultAzureCredential()
    try:
        client = EventHubConsumerClient(
            fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
            eventhub_name=EVENT_HUB_NAME,
            consumer_group=CONSUMER_GROUP,
            credential=credential,
        )

        handler = PrintHandler()

        service = AzureEventHubSubscriptionService(
            handler=handler,
            client=client,
        )

        service.serve()

    finally:
        credential.close()
