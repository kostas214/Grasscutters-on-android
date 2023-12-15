import os
import collections
import random
from mitmproxy import http, connection, ctx, tls
from abc import ABC, abstractmethod
from enum import Enum
from mitmproxy.utils import human

# This can also be replaced with another IP address.
USE_SSL = True
REMOTE_HOST = "127.0.0.1"
REMOTE_PORT = 5000

if os.getenv('MITM_REMOTE_HOST') != None:
    REMOTE_HOST = os.getenv('MITM_REMOTE_HOST')
if os.getenv('MITM_REMOTE_PORT') != None:
    REMOTE_PORT = int(os.getenv('MITM_REMOTE_PORT'))
if os.getenv('MITM_USE_SSL') != None:
    USE_SSL = bool(os.getenv('MITM_USE_SSL'))

print('MITM Remote Host: ' + REMOTE_HOST)
print('MITM Remote Port: ' + str(REMOTE_PORT))
print('MITM Use SSL ' + str(USE_SSL))

class MlgmXyysd_Animation_Company_Proxy:

    LIST_DOMAINS = [
        "ps.yuuki.me"
    ]

    def request(self, flow: http.HTTPFlow) -> None:
        print(flow.request.host)
        if flow.request.host in self.LIST_DOMAINS:
            if USE_SSL:
                flow.request.scheme = "http"
            else:
                flow.request.scheme = "http"
            print("HELOOO")
            flow.request.host = REMOTE_HOST
            flow.request.port = REMOTE_PORT

class InterceptionResult(Enum):
    SUCCESS = 1
    FAILURE = 2
    SKIPPED = 3

class TlsStrategy(ABC):
    def __init__(self):
        self.history = collections.defaultdict(lambda: collections.deque(maxlen=200))

    @abstractmethod
    def should_intercept(self, server_address: connection.Address) -> bool:
        raise NotImplementedError()

    def record_success(self, server_address):
        self.history[server_address].append(InterceptionResult.SUCCESS)

    def record_failure(self, server_address):
        self.history[server_address].append(InterceptionResult.FAILURE)

    def record_skipped(self, server_address):
        self.history[server_address].append(InterceptionResult.SKIPPED)


class ConservativeStrategy(TlsStrategy):
    def should_intercept(self, server_address: connection.Address) -> bool:
        return InterceptionResult.FAILURE not in self.history[server_address]

class ProbabilisticStrategy(TlsStrategy):
    def __init__(self, p: float):
        self.p = p
        super().__init__()

    def should_intercept(self, server_address: connection.Address) -> bool:
        return random.uniform(0, 1) < self.p

class MaybeTls:
    strategy: TlsStrategy

    def load(self, l):
        l.add_option(
            "tls_strategy", int, 0,
            "TLS passthrough strategy. If set to 0, connections will be passed through after the first unsuccessful "
            "handshake. If set to 0 < p <= 100, connections with be passed through with probability p.",
        )

    def configure(self, updated):
        if "tls_strategy" not in updated:
            return
        if ctx.options.tls_strategy > 0:
            self.strategy = ProbabilisticStrategy(ctx.options.tls_strategy / 100)
        else:
            self.strategy = ConservativeStrategy()

    def tls_clienthello(self, data: tls.ClientHelloData):
        server_address = data.context.server.peername
        if not self.strategy.should_intercept(server_address):
            ctx.log(f"TLS passthrough: {human.format_address(server_address)}.")
            data.ignore_connection = True
            self.strategy.record_skipped(server_address)

    def tls_established_client(self, data: tls.TlsData):
        server_address = data.context.server.peername
        ctx.log(f"TLS handshake successful: {human.format_address(server_address)}")
        self.strategy.record_success(server_address)

    def tls_failed_client(self, data: tls.TlsData):
        server_address = data.context.server.peername
        ctx.log(f"TLS handshake failed: {human.format_address(server_address)}")
        self.strategy.record_failure(server_address)
        
addons = [
	MlgmXyysd_Animation_Company_Proxy(),
    MaybeTls()
]
