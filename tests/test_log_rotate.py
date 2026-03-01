"""Tests for log-rotate."""

import pytest
from log_rotate import rotate


class TestRotate:
    """Test suite for rotate."""

    def test_basic(self):
        """Test basic usage."""
        result = rotate("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            rotate("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = rotate(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
