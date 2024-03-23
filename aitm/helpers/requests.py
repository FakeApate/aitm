from aitm.aitm_config import TARGETS, TARGET_PROXIES
from mitmproxy.http import HTTPFlow


def modify_header(flow: HTTPFlow, header: str) -> None:
    if header == "Host":
        modify_host(flow)
    else:
        value = flow.request.headers.get(header)
        if value is not None:
            for target in TARGETS:
                value = value.replace(target["proxy"], target["origin"])
            flow.request.headers[header] = value


def modify_query(flow: HTTPFlow, query_key: str) -> None:
    value = flow.request.query.get(query_key)
    if value is not None:
        for target in TARGETS:
            value = value.replace(target["proxy"], target["origin"])
        flow.request.query[query_key] = value


def get_local_upstream_port(host: str) -> int | None:
    split = host.split(":")
    if len(split) == 2:
        if split[0] == "local.fsoc.bid":
            return int(split[1])


def search_targets(_for: str, _where: str, _is: str | int) -> str | int:
    result = [target[_for] for target in TARGETS if target[_where] == _is]
    if len(result) == 1:
        return result[0]


def modify_host(flow: HTTPFlow) -> None:
    host = flow.request.headers.get("Host")
    if host is not None:
        port = get_local_upstream_port(host)
        origin = None
        if port is not None:
            origin = search_targets("origin", "port", port)
        elif host in TARGET_PROXIES:
            origin = search_targets("origin", "proxy", host)
        if origin is not None:
            flow.request.headers["Host"] = origin
