import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.identity.aio import DefaultAzureCredential

EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "matsuyama.servicebus.windows.net"
EVENT_HUB_NAME = "example"
CONSUMER_GROUP = "example"

credential = DefaultAzureCredential()


async def on_event(partition_context, event):
    print(f"Received event: {event.body_as_str()}")
    await partition_context.update_checkpoint(event)


async def run():
    client = EventHubConsumerClient(
        fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
        eventhub_name=EVENT_HUB_NAME,
        consumer_group=CONSUMER_GROUP,
        credential=credential,
    )
    print("Consumer client created successfully.")
    async with client:
        await client.receive(
            on_event=on_event,
        )
    await credential.close()


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()
