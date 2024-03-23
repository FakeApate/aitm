
from mitmproxy.http import HTTPFlow
from aitm.aitm_config import TARGET_PROXIES, TARGETS, LOCAL_UPSTREAM_HOSTNAME, LOCAL_UPSTREAM_SCHEME

def proxy_port(flow: HTTPFlow) -> int | None:
    for target in TARGETS:
        if target["proxy"] == flow.request.host:
            return target["port"]

class UpstreamAddon:
    def request(self, flow: HTTPFlow) -> None:
        if flow.request.host in TARGET_PROXIES:
            port = proxy_port(flow)
            if port is not None:
                address = (LOCAL_UPSTREAM_SCHEME, (LOCAL_UPSTREAM_HOSTNAME, port))
                flow.server_conn.via = address
                flow.request.host = LOCAL_UPSTREAM_HOSTNAME
                flow.request.port = port
                flow.request.scheme = LOCAL_UPSTREAM_SCHEME