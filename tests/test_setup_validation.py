"""Validation tests to ensure the testing infrastructure is properly set up."""
import sys
from pathlib import Path

import pytest


class TestInfrastructureSetup:
    """Test class to validate the testing infrastructure."""

    def test_python_version(self):
        """Verify Python version is 3.8 or higher."""
        assert sys.version_info >= (3, 8), "Python 3.8 or higher is required"

    def test_pytest_installed(self):
        """Verify pytest is installed and importable."""
        import pytest as pt
        assert pt is not None
        assert hasattr(pt, '__version__')

    def test_pytest_cov_installed(self):
        """Verify pytest-cov is installed."""
        import pytest_cov
        assert pytest_cov is not None

    def test_pytest_mock_installed(self):
        """Verify pytest-mock is installed."""
        import pytest_mock
        assert pytest_mock is not None

    def test_directory_structure(self):
        """Verify the expected directory structure exists."""
        project_root = Path(__file__).parent.parent
        
        # Check main directories
        assert (project_root / 'tests').exists()
        assert (project_root / 'tests' / 'unit').exists()
        assert (project_root / 'tests' / 'integration').exists()
        
        # Check __init__.py files
        assert (project_root / 'tests' / '__init__.py').exists()
        assert (project_root / 'tests' / 'unit' / '__init__.py').exists()
        assert (project_root / 'tests' / 'integration' / '__init__.py').exists()
        
        # Check conftest.py
        assert (project_root / 'tests' / 'conftest.py').exists()

    def test_pyproject_toml_exists(self):
        """Verify pyproject.toml exists and contains required sections."""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / 'pyproject.toml'
        
        assert pyproject_path.exists(), "pyproject.toml should exist"
        
        content = pyproject_path.read_text()
        assert '[tool.poetry]' in content
        assert '[tool.pytest.ini_options]' in content
        assert '[tool.coverage.run]' in content

    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that the unit marker works."""
        assert True

    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that the integration marker works."""
        assert True

    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that the slow marker works."""
        assert True


class TestFixtures:
    """Test class to validate pytest fixtures."""

    def test_temp_dir_fixture(self, temp_dir):
        """Test the temp_dir fixture."""
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test we can write to it
        test_file = temp_dir / 'test.txt'
        test_file.write_text('test content')
        assert test_file.exists()
        assert test_file.read_text() == 'test content'

    def test_mock_config_fixture(self, mock_config):
        """Test the mock_config fixture."""
        assert hasattr(mock_config, 'debug')
        assert hasattr(mock_config, 'verbose')
        assert hasattr(mock_config, 'dry_run')
        assert mock_config.debug is False
        assert mock_config.verbose is True

    def test_mock_env_fixture(self, mock_env):
        """Test the mock_env fixture."""
        import os
        assert os.environ.get('TEST_MODE') == 'true'
        assert os.environ.get('LOG_LEVEL') == 'DEBUG'

    def test_sample_data_fixture(self, sample_data):
        """Test the sample_data fixture."""
        assert 'maintainers' in sample_data
        assert 'repositories' in sample_data
        assert len(sample_data['maintainers']) == 2
        assert len(sample_data['repositories']) == 2

    def test_capture_logs_fixture(self, capture_logs):
        """Test the capture_logs fixture."""
        import logging
        logger = logging.getLogger(__name__)
        logger.debug("Test debug message")
        logger.info("Test info message")
        
        assert "Test debug message" in capture_logs.text
        assert "Test info message" in capture_logs.text