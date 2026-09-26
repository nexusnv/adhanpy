import pytest

import adhanpy
from adhanpy import PrayerTimes as RootPrayerTimes
from adhanpy.calculation import (
    CalculationMethod,
    CalculationParameters,
    HighLatitudeRule,
    Madhab,
    PrayerAdjustments,
)
from adhanpy.data import Coordinates, NightPortions, Prayer, ShadowLength
from adhanpy.PrayerTimes import PrayerTimes
from adhanpy.util.DateComponents import DateComponents


def test_root_exports_match_all():
    assert set(adhanpy.__all__) == {
        "PrayerTimes",
        "Qibla",
        "SunnahTimes",
        "CalculationMethod",
        "CalculationParameters",
        "HighLatitudeRule",
        "Madhab",
        "PrayerAdjustments",
        "Coordinates",
        "Prayer",
    }
    for name in adhanpy.__all__:
        assert getattr(adhanpy, name) is not None
    assert adhanpy.PrayerTimes is RootPrayerTimes


def test_subpackage_exports():
    from adhanpy import calculation, data

    assert set(calculation.__all__) == {
        "CalculationMethod",
        "CalculationParameters",
        "HighLatitudeRule",
        "Madhab",
        "PrayerAdjustments",
    }
    assert set(data.__all__) == {
        "Coordinates",
        "NightPortions",
        "Prayer",
        "ShadowLength",
    }


def test_time_for_prayer_matches_attributes():
    prayer_times = PrayerTimes(
        (35.7750, -78.6336),
        DateComponents(2015, 7, 12),
        calculation_parameters=CalculationParameters(
            method=CalculationMethod.NORTH_AMERICA
        ),
    )

    assert prayer_times.time_for_prayer(Prayer.FAJR) == prayer_times.fajr
    assert prayer_times.time_for_prayer(Prayer.SUNRISE) == prayer_times.sunrise
    assert prayer_times.time_for_prayer(Prayer.DHUHR) == prayer_times.dhuhr
    assert prayer_times.time_for_prayer(Prayer.ASR) == prayer_times.asr
    assert prayer_times.time_for_prayer(Prayer.MAGHRIB) == prayer_times.maghrib
    assert prayer_times.time_for_prayer(Prayer.ISHA) == prayer_times.isha


def test_time_for_prayer_rejects_none():
    prayer_times = PrayerTimes(
        (35.7750, -78.6336),
        DateComponents(2015, 7, 12),
        calculation_parameters=CalculationParameters(
            method=CalculationMethod.NORTH_AMERICA
        ),
    )

    with pytest.raises(ValueError, match="(?i)prayer"):
        prayer_times.time_for_prayer(Prayer.NONE)
