import asyncio
import sys

class PubSubClient:
    def __init__(self, host, port, topics):
        self.host = host
        self.port = port
        self.topics = topics

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        print(f'Connected to {self.host}:{self.port}')

        # Subscribe to the specified topics
        await self.send_message(f'SUBSCRIBE:{",".join(self.topics)}')

        # Start receiving messages
        await self.receive_messages()

    async def disconnect(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
            print('Disconnected')

    async def send_message(self, message):
        self.writer.write(message.encode() + b'\n')
        await self.writer.drain()

    async def receive_messages(self):
        while True:
            data = await self.reader.readline()
            if not data:
                break
            message = data.decode().strip()
            print(f'Received message: {message}')

    async def run_subscriber(self):
        await self.connect()

    async def monitor_input(self):
        pass


async def run_subscriber(host, port, topics):
    client = PubSubClient(host, port, topics)
    await client.run_subscriber()
    await client.disconnect()


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage:')
        print('  python program.py subscriber <host> <port> <topics>')
        sys.exit(1)

    mode = sys.argv[1].lower()
    host = sys.argv[2]
    port = int(sys.argv[3])
    topics = sys.argv[4].split(',')

    loop = asyncio.get_event_loop()

    if mode == 'subscriber':
        loop.run_until_complete(run_subscriber(host, port, topics))
    else:
        print('Invalid mode. Please specify "subscriber".')
        sys.exit(1)

    loop.close()