from datetime import datetime, timedelta, timezone
from adhanpy import PrayerTimes, SunnahTimes
from adhanpy.calculation import CalculationMethod, CalculationParameters
from adhanpy.util.DateComponents import DateComponents


def _prayer_times():
    return PrayerTimes(
        (35.7750, -78.6336),
        DateComponents(2015, 7, 12),
        CalculationMethod.MUSLIM_WORLD_LEAGUE,
    )


def test_sunnah_times():
    prayer_times = _prayer_times()
    sunnah_times = SunnahTimes(prayer_times)

    assert sunnah_times.middle_of_the_night == datetime(
        2015, 7, 13, 4, 28, tzinfo=timezone.utc
    )
    assert sunnah_times.last_third_of_the_night == datetime(
        2015, 7, 13, 5, 46, tzinfo=timezone.utc
    )


def test_sunnah_times_ordering():
    prayer_times = _prayer_times()
    sunnah_times = SunnahTimes(prayer_times)
    tomorrow = PrayerTimes(
        (35.7750, -78.6336),
        prayer_times._prayer_date + timedelta(days=1),
        calculation_parameters=CalculationParameters(
            method=CalculationMethod.MUSLIM_WORLD_LEAGUE
        ),
    )

    assert prayer_times.maghrib < sunnah_times.middle_of_the_night
    assert sunnah_times.middle_of_the_night < sunnah_times.last_third_of_the_night
    assert sunnah_times.last_third_of_the_night < tomorrow.fajr
