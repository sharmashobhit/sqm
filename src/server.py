# The code in this file is a mass broadcaster. Instead we should be able to subscribe to particular topics
import asyncio

class PubSubServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    async def start(self):
        server = await asyncio.start_server(
            self.handle_client,
            self.host,
            self.port
        )

        addr = server.sockets[0].getsockname()
        print(f'Server started at {addr}')

        async with server:
            await server.serve_forever()

    async def handle_client(self, reader, writer):
        self.clients.append(writer)
        print(f'New client connected: {writer.get_extra_info("peername")}')

        try:
            while True:
                data = await reader.readline()
                if not data:
                    break
                message = data.decode().strip()
                print(f'Received message: {message}')

                # Broadcast the message to all clients
                for client in self.clients:
                    client.write(data)
                    await client.drain()
        except asyncio.CancelledError:
            pass
        finally:
            self.clients.remove(writer)
            writer.close()
            await writer.wait_closed()
            print(f'Client disconnected: {writer.get_extra_info("peername")}')


async def run_pub_sub_server(host, port):
    server = PubSubServer(host, port)
    await server.start()
