"""Pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load monorepo .env for local integration runs (never log keys).
_monorepo_env = Path(__file__).resolve().parents[3] / ".env"
if _monorepo_env.is_file():
    load_dotenv(_monorepo_env)

_package_env = Path(__file__).resolve().parents[1] / ".env"
if _package_env.is_file():
    load_dotenv(_package_env)


@pytest.fixture
def mock_manifest() -> dict:
    return {
        "tool_id": "mendelian-cross-solver",
        "title": "Mendelian Cross Solver",
        "execution_mode": "sync",
        "examples": [
            {
                "name": "complete_monohybrid",
                "input": {
                    "dominance_mode": "complete",
                    "parent1_genotype": "Aa",
                    "parent2_genotype": "Aa",
                    "custom_phenotypes": {
                        "dominant": "Dominant",
                        "recessive": "Recessive",
                    },
                },
            },
            {
                "name": "sex_linked_hemophilia",
                "input": {
                    "dominance_mode": "sex_linked",
                    "parent1_genotype": "X^H X^h",
                    "parent2_genotype": "X^H Y",
                    "custom_phenotypes": {
                        "dominant": "Unaffected",
                        "recessive": "Hemophilia",
                    },
                },
            },
        ],
    }


@pytest.fixture
def mock_run_response() -> dict:
    return {
        "run_id": "run_test123",
        "status": "completed",
        "result": {
            "can_compute": True,
            "grid": [
                {"genotype": "AA", "phenotype": "Dominant", "count": 1},
                {"genotype": "Aa", "phenotype": "Dominant", "count": 2},
                {"genotype": "aa", "phenotype": "Recessive", "count": 1},
            ],
            "genotype_ratios": {"ratio": "1:2:1"},
            "phenotype_ratios": {"ratio": "3:1"},
            "walkthrough": [{"step": 1, "text": "Set up gametes"}],
            "warnings": [],
        },
        "error": None,
        "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_test123",
        "permalink": "https://tools.pepkio.com/r/run_test123",
    }
