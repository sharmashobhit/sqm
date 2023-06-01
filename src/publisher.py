import asyncio
import sys

async def run_publisher(host, port, topic, message):
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(f'{topic}:{message}\n'.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage:')
        print('  python program.py publisher <host> <port> <topic> <message>')
        sys.exit(1)

    mode = sys.argv[1].lower()
    host = sys.argv[2]
    port = int(sys.argv[3])
    topic = sys.argv[4]
    message = sys.argv[5]

    loop = asyncio.get_event_loop()

    if mode == 'publisher':
        loop.run_until_complete(run_publisher(host, port, topic, message))
    else:
        print('Invalid mode. Please specify "publisher".')
        sys.exit(1)

    loop.close()
