"""Shared pytest fixtures and configuration."""
import os
import tempfile
from pathlib import Path
from unittest.mock import Mock

import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config():
    """Create a mock configuration object."""
    config = Mock()
    config.debug = False
    config.verbose = True
    config.dry_run = False
    return config


@pytest.fixture
def mock_env(monkeypatch):
    """Create a mock environment with test variables."""
    test_env = {
        'TEST_MODE': 'true',
        'LOG_LEVEL': 'DEBUG',
    }
    for key, value in test_env.items():
        monkeypatch.setenv(key, value)
    return test_env


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return {
        'maintainers': [
            {'name': 'John Doe', 'email': 'john@example.com'},
            {'name': 'Jane Smith', 'email': 'jane@example.com'},
        ],
        'repositories': [
            'flatcar/portage-stable',
            'flatcar/coreos-overlay',
        ]
    }


@pytest.fixture
def mock_requests(mocker):
    """Mock requests library for HTTP testing."""
    mock = mocker.patch('requests.get')
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {'status': 'success'}
    return mock


@pytest.fixture(autouse=True)
def cleanup():
    """Cleanup any test artifacts after each test."""
    yield
    # Add any cleanup code here if needed


@pytest.fixture
def capture_logs(caplog):
    """Capture log output for testing."""
    with caplog.at_level('DEBUG'):
        yield caplog