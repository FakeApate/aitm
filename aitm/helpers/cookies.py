from http.cookies import SimpleCookie
from aitm.aitm_config import TARGETS


def parse_cookies(cookies: SimpleCookie) -> list:
    parsed_cookies = []
    for name, morsel in cookies.items():
        cookie = {"name": name, "value": morsel.value}
        for k, v in morsel.items():
            if k == "domain":
                for target in TARGETS:
                    v = v.replace(target["proxy"], target["origin"])
            cookie[k] = v
        parsed_cookies.append(cookie)
    return parsed_cookies
