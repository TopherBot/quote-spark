import pytest
from quote_spark import _QUOTES, get_random_quote


def test_random_quote_is_from_list():
    """The returned quote must be one of the predefined entries."""
    quote = get_random_quote()
    assert quote in _QUOTES


def test_multiple_calls_vary():
    """Running the function a few times should produce at least two distinct quotes.
    This is a probabilistic test but with the small list the chance of failure is < 1 %.
    """
    samples = {get_random_quote() for _ in range(10)}
    assert len(samples) >= 2
