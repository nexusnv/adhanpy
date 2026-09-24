from datetime import datetime, timezone
import pytest
import adhanpy.util.CalendarUtil as CalendarUtil


def test_rounding_when_second_is_less_than_30():
    dt = datetime(2015, 1, 1, 10, 2, 29, tzinfo=timezone.utc)
    rounded = CalendarUtil.rounded_minute(dt)

    assert rounded.minute == 2
    assert rounded.second == 0


def test_rounding_when_second_is_greater_than_30():
    dt = datetime(2015, 1, 1, 10, 2, 31)
    rounded = CalendarUtil.rounded_minute(dt)

    assert rounded.minute == 3
    assert rounded.second == 0


def test_rounding_when_second_is_greater_than_30_and_minute_is_59():
    dt = datetime(2015, 1, 1, 10, 59, 31, tzinfo=timezone.utc)
    rounded = CalendarUtil.rounded_minute(dt)

    assert rounded.hour == 10
    assert rounded.minute == 59
    assert rounded.second == 0


@pytest.mark.parametrize(
    "second, expected_minute",
    [(0, 2), (29, 2), (31, 3)],
)
def test_rounding_boundaries(second, expected_minute):
    dt = datetime(2015, 1, 1, 10, 2, second, tzinfo=timezone.utc)
    rounded = CalendarUtil.rounded_minute(dt)

    assert (rounded.hour, rounded.minute, rounded.second) == (
        10,
        expected_minute,
        0,
    )


@pytest.mark.xfail(
    reason="hour carry lost: 10:59:31 rounds to 10:59 instead of 11:00 (issue #2.1)",
    strict=True,
)
def test_rounding_carries_into_next_hour():
    dt = datetime(2015, 1, 1, 10, 59, 31, tzinfo=timezone.utc)
    rounded = CalendarUtil.rounded_minute(dt)

    assert (rounded.hour, rounded.minute, rounded.second) == (11, 0, 0)


@pytest.mark.xfail(
    reason="banker's rounding: exactly 30s does not round up (issue #2.3)",
    strict=True,
)
def test_rounding_half_up_at_exactly_30_seconds():
    dt = datetime(2015, 1, 1, 10, 2, 30, tzinfo=timezone.utc)
    rounded = CalendarUtil.rounded_minute(dt)

    assert (rounded.hour, rounded.minute) == (10, 3)


@pytest.mark.xfail(
    reason="microseconds ignored in decision and retained in output (issue #2.2)",
    strict=True,
)
def test_rounding_folds_microseconds_and_zeroes_them():
    dt = datetime(2015, 1, 1, 10, 2, 29, 900000, tzinfo=timezone.utc)
    rounded = CalendarUtil.rounded_minute(dt)

    assert rounded == datetime(2015, 1, 1, 10, 3, 0, tzinfo=timezone.utc)


@pytest.mark.xfail(
    reason="microseconds retained instead of zeroed (issue #2.2)", strict=True
)
def test_rounding_zeroes_microseconds():
    dt = datetime(2015, 1, 1, 10, 2, 10, 500000, tzinfo=timezone.utc)
    rounded = CalendarUtil.rounded_minute(dt)

    assert rounded == datetime(2015, 1, 1, 10, 2, 0, tzinfo=timezone.utc)
