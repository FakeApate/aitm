"""
Upstream addon
"""

from mitmproxy.http import HTTPFlow

from aitm.aitm_config import (
    LOCAL_UPSTREAM_HOSTNAME,
    LOCAL_UPSTREAM_SCHEME,
    TARGET_PROXIES,
    TARGETS,
)


def proxy_port(flow: HTTPFlow) -> int | None:
    """
    Function to get the correct port for the upstream
    """
    for target in TARGETS:
        if target["proxy"] == flow.request.host:
            return target["port"]
    return None


class UpstreamAddon:
    """
    Addon Class for the upstream proxy
    """

    def request(self, flow: HTTPFlow) -> None:
        """
        Method which mitmproxy calls for each request
        """
        if flow.request.host in TARGET_PROXIES:
            port = proxy_port(flow)
            if port is not None:
                flow.server_conn.via = LOCAL_UPSTREAM_SCHEME, (
                    LOCAL_UPSTREAM_HOSTNAME,
                    port,
                )
                flow.request.host = LOCAL_UPSTREAM_HOSTNAME
                flow.request.port = port
                flow.request.scheme = LOCAL_UPSTREAM_SCHEME
