#!/usr/bin/env python3

import asyncio
import websockets
import functools
import logging
import json
from ws_env import get_env

logging.basicConfig(level=logging.INFO)


async def connection_handler(websocket, path, connected):

    logging.info(f'Connection from {websocket.remote_address}')
    connected.add(websocket)
    try:
        while True:
            text = "XXX"
            await asyncio.sleep(1)
            greeting = json.dumps({"text": f"Hello {text}!"}, ensure_ascii=False)
            await asyncio.wait([ws.send(greeting) for ws in connected])
    except websockets.ConnectionClosed as e:
        logging.info(f'Lost connection {websocket.remote_address}: {e!s}')
    finally:
        connected.remove(websocket)


def start_ws_server():

    env = get_env()
    loop = asyncio.get_event_loop()
    connected = set()

    conn_handler = functools.partial(connection_handler, connected=connected)
    start_server = websockets.serve(conn_handler, env.ip_addr, env.port)

    logging.info(f'Listening on {env.ip_addr} {env.port}')
    loop.run_until_complete(start_server)
    loop.run_forever()


if __name__ == "__main__":
    start_ws_server()
