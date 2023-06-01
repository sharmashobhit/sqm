# SQM CLI

SQM CLI is a command-line interface (CLI) application that allows you to publish and subscribe to messages using a TCP-based pub/sub server.

## Features

- Start a pub/sub server to handle message publication and subscription.
- Run a publisher to publish messages to specific topics.
- Run a subscriber to subscribe to topics and receive messages.

## Installation

1. Clone the repository:

```shell
$ git clone <repository_url>
Change into the project directory:

$ cd sqm
Install the dependencies:

$ pip install -e .
```

## Usage

### Server

To start the pub/sub server, use the following command:

```shell
$ sqm server <host> <port>
```

Replace <host> with the host IP address or hostname where the server should listen, and <port> with the port number to bind the server to.

### Publisher

To run a publisher and publish messages to a specific topic, use the following command:

```shell
$ sqm publisher <host> <port> <topic> <message>
```

Replace <host> and <port> with the server's host and port to connect to. <topic> should be the desired topic for publishing, and <message> is the message content.

### Subscriber

To run a subscriber and subscribe to one or more topics, use the following command:

```shell
$ sqm subscriber <host> <port> <topic1> <topic2> ...
```

Replace <host> and <port> with the server's host and port to connect to. <topic1>, <topic2>, and so on are the topics to subscribe to. You can specify one or more topics separated by spaces.
