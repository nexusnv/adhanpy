from datetime import datetime, timedelta
from adhanpy.PrayerTimes import PrayerTimes
from adhanpy.util.CalendarUtil import rounded_minute


class SunnahTimes:
    """
    Sunnah night markers derived from prayer times.
    Ported from upstream adhan (adhan-kotlin SunnahTimes).
    """

    #: The midpoint between Maghrib and (next-day) Fajr.
    middle_of_the_night: datetime

    #: The beginning of the last third of the period between Maghrib
    #: and (next-day) Fajr, a recommended time to perform Qiyam.
    last_third_of_the_night: datetime

    def __init__(self, prayer_times: PrayerTimes) -> None:
        tomorrow = PrayerTimes(
            prayer_times.coordinates,
            prayer_times._prayer_date + timedelta(days=1),
            calculation_parameters=prayer_times.calculation_parameters,
            time_zone=prayer_times.time_zone,
        )

        night_duration = (tomorrow.fajr - prayer_times.maghrib).total_seconds()
        self.middle_of_the_night = rounded_minute(
            prayer_times.maghrib + timedelta(seconds=int(night_duration / 2))
        )
        self.last_third_of_the_night = rounded_minute(
            prayer_times.maghrib + timedelta(seconds=int(night_duration * (2 / 3)))
        )
