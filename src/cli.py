import sys
import argparse
import asyncio
from .publisher import run_publisher
from .subscriber import run_subscriber
from .server import run_pub_sub_server

def main():
    parser = argparse.ArgumentParser(description='TCP PubSub CLI')
    subparsers = parser.add_subparsers(dest='command', required=True, metavar='COMMAND')

    server_parser = subparsers.add_parser('server', help='Run the PubSub server')
    server_parser.add_argument('host', type=str, help='Host to bind the server to')
    server_parser.add_argument('port', type=int, help='Port number to listen on')

    publisher_parser = subparsers.add_parser('publisher', help='Run a PubSub publisher')
    publisher_parser.add_argument('host', type=str, help='Server host to connect to')
    publisher_parser.add_argument('port', type=int, help='Server port to connect to')
    publisher_parser.add_argument('topic', type=str, help='Topic to publish to')
    publisher_parser.add_argument('message', type=str, help='Message to publish')

    subscriber_parser = subparsers.add_parser('subscriber', help='Run a PubSub subscriber')
    subscriber_parser.add_argument('host', type=str, help='Server host to connect to')
    subscriber_parser.add_argument('port', type=int, help='Server port to connect to')
    subscriber_parser.add_argument('topics', type=str, nargs='+', help='Topics to subscribe to')

    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    if args.command == 'server':
        loop.run_until_complete(run_pub_sub_server(args.host, args.port))
    elif args.command == 'publisher':
        loop.run_until_complete(run_publisher(args.host, args.port, args.topic, args.message))
    elif args.command == 'subscriber':
        loop.run_until_complete(run_subscriber(args.host, args.port, args.topics))
    
    loop.close()

if __name__ == '__main__':
    main()
