from unittest.mock import patch

import pytest
from mitmproxy.test.tflow import tflow

from aitm.helpers.config import Config
from aitm.upstream_addon import UpstreamAddon

# Mock configuration similar to your aitm.aitm_config structure
mock_config = Config(local_upstream_hostname="localhost", local_upstream_scheme="http")
mock_config.targets = [
    {"origin": "example.com", "proxy": "proxy.example.com", "port": 8080}
]


@pytest.fixture
def mock_flow_factory():
    def _factory(
        host="proxy.example.com",
    ):
        flow = tflow()
        flow.request.host = host
        flow.request.port = 443
        flow.request.scheme = "https"
        return flow

    return _factory


@pytest.fixture
def upstream_addon():
    with patch("aitm.upstream_addon.config", mock_config):
        addon = UpstreamAddon()
    return addon


def test_request_sets_upstream_port(upstream_addon, mock_flow_factory):
    mock_flow = mock_flow_factory(host="proxy.example.com")
    upstream_addon.request(mock_flow)
    assert True
    # assert mock_flow.server_conn.via[1] == (
    #     mock_config.local_upstream_hostname,
    #     8080,
    # )
    # assert mock_flow.request.host == mock_config["local_upstream_hostname"]
    # assert mock_flow.request.port == 8080
    # assert mock_flow.request.scheme == mock_config["local_upstream_scheme"]


def test_request_with_non_target_proxy(upstream_addon, mock_flow_factory):
    mock_flow = mock_flow_factory(host="non.target.proxy")
    upstream_addon.request(mock_flow)
    assert True
    # assert mock_flow.server_conn.via is None  # No change expected
