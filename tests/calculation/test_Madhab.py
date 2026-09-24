import pytest
from adhanpy.calculation.Madhab import Madhab


def test_shafi_shadow_length():
    assert Madhab.SHAFI.get_shadow_length().shadow_length == pytest.approx(1.0)


def test_hanafi_shadow_length():
    assert Madhab.HANAFI.get_shadow_length().shadow_length == pytest.approx(2.0)


@pytest.mark.xfail(
    reason="unknown madhab returns None instead of raising (issue #2.6)",
    strict=True,
)
def test_unknown_madhab_raises():
    with pytest.raises(ValueError, match="(?i)madhab"):
        Madhab.get_shadow_length(None)
