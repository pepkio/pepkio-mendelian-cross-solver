"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_mendelian_cross_solver.client import PepkioClient

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, base_url = request.param
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "mendelian-cross-solver"
    names = live_client.list_examples()
    assert "complete_monohybrid" in names


def test_run_complete_monohybrid(live_client: PepkioClient):
    inp = live_client.get_example_input("complete_monohybrid")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert result.result.get("can_compute") is True
    assert result.result.get("phenotype_ratios", {}).get("ratio") == "3:1"
    grid = result.result.get("grid")
    assert isinstance(grid, list)
    assert len(grid) > 0
    assert result.error is None


def test_run_abo_cross(live_client: PepkioClient):
    inp = live_client.get_example_input("abo_cross")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("phenotype_ratios", {}).get("ratio") == "1:1:1:1"


def test_run_sex_linked_hemophilia(live_client: PepkioClient):
    inp = live_client.get_example_input("sex_linked_hemophilia")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("can_compute") is True
    grid = result.result.get("grid")
    assert isinstance(grid, list)
    assert len(grid) > 0
