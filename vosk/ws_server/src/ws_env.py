import os
import dataclasses


@dataclasses.dataclass
class WSEnv:
    """
    Переменные окружения WebSocket-сервера
    """
    ip_addr: str          # WS-server IP address
    port: int             # WS-server IP port


def get_env() -> WSEnv:

    env = WSEnv(
        ip_addr=os.environ.get("WS_SERVER_IP_ADDR", "0.0.0.0"),
        port=int(os.environ.get("WS_SERVER_PORT", 2701)),
    )
    return env
