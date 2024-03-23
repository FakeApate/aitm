"""
Helper functions for request manipulations
"""

from http.cookies import SimpleCookie

from aitm.aitm_config import CONTENT_TYPES, CUSTOM_MODIFICATIONS, TARGET_SITES, TARGETS
from mitmproxy.http import HTTPFlow


def modify_header(flow: HTTPFlow, header: str) -> None:
    """
    Function to modify the headers of a response
    """
    value = flow.response.headers.get(header)
    if value is not None:
        for target in TARGETS:
            value = value.replace(target["origin"], target["proxy"])
        flow.response.headers[header] = value


def modify_content(flow: HTTPFlow) -> None:
    """
    Function to modify body of a response
    """
    mime = flow.response.headers.get("Content-Type", "").split(";")[0]
    site = flow.server_conn.address[0]
    if mime in CONTENT_TYPES and site in TARGET_SITES:
        for target in TARGETS:
            flow.response.text = flow.response.text.replace(
                f'https://{target["origin"]}', f'https://{target["proxy"]}'
            )

    for mod in CUSTOM_MODIFICATIONS:
        if mime in mod["mimes"] and site in mod["sites"]:
            flow.response.text = flow.response.text.replace(
                mod["search"], mod["replace"]
            )


def modify_cookies(flow: HTTPFlow) -> None:
    """
    Function to modify set-cookies of a response
    """
    set_cookies_str = flow.response.headers.get_all("set-cookie")
    set_cookies_str_modified: list[str] = []

    if set_cookies_str:
        for cookie in set_cookies_str:
            for target in TARGETS:
                cookie = cookie.replace(target["origin"], target["proxy"])
            set_cookies_str_modified.append(cookie)
        flow.response.headers.set_all("set-cookie", set_cookies_str_modified)


def save_cookies(flow: HTTPFlow, simple_cookie: SimpleCookie):
    """
    Function to load cookies into SimpleCookie
    """
    set_cookies_str = flow.response.headers.get_all("set-cookie")
    if set_cookies_str:
        for cookie in set_cookies_str:
            simple_cookie.load(cookie)
