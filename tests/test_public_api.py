import pytest

import adhanpy
from adhanpy import PrayerTimes as RootPrayerTimes
from adhanpy import Qibla, SunnahTimes
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
    assert getattr(adhanpy, "__all__") == [
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
    ]
    assert {
        "PrayerTimes": PrayerTimes,
        "Qibla": Qibla,
        "SunnahTimes": SunnahTimes,
        "CalculationMethod": CalculationMethod,
        "CalculationParameters": CalculationParameters,
        "HighLatitudeRule": HighLatitudeRule,
        "Madhab": Madhab,
        "PrayerAdjustments": PrayerAdjustments,
        "Coordinates": Coordinates,
        "Prayer": Prayer,
    } == {name: getattr(adhanpy, name) for name in adhanpy.__all__}
    assert adhanpy.PrayerTimes is RootPrayerTimes


def test_subpackage_exports():
    from adhanpy import calculation, data

    assert {
        "CalculationMethod": CalculationMethod,
        "CalculationParameters": CalculationParameters,
        "HighLatitudeRule": HighLatitudeRule,
        "Madhab": Madhab,
        "PrayerAdjustments": PrayerAdjustments,
    } == {name: getattr(calculation, name) for name in calculation.__all__}
    assert {
        "Coordinates": Coordinates,
        "NightPortions": NightPortions,
        "Prayer": Prayer,
        "ShadowLength": ShadowLength,
    } == {name: getattr(data, name) for name in data.__all__}


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
