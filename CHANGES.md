# Changelog

## Unreleased
* Fix hour-rollover in `rounded_minute` (`10:59:31` now rounds to `11:00`),
  use half-up rounding at exactly 30 seconds, and zero microseconds.
* Polar day/night and undefined Asr now raise `RuntimeError` with a
  diagnostic message instead of an empty `RuntimeError`.
* Narrowed bare `except:` clauses (`Astronomical.corrected_hour_angle`,
  `PrayerTimes._set_isha`).
* Unknown madhab raises `ValueError`; non-`CalculationMethod` method raises
  `TypeError` (`None` still means `NONE`).
* `PrayerTimes` accepts a `Coordinates` object as well as a
  `(latitude, longitude)` tuple; fixed `src/example` header using the wrong date.
* Method parameters are now copied per instance: mutating one
  `CalculationParameters.method_adjustments` no longer leaks into
  subsequently created instances.
* Require Python `>=3.11`; CI matrix is now 3.11–3.13 with refreshed dev pins.
* Ship `py.typed` (PEP 561) and complete type annotations; the package
  is now `mypy --disallow-untyped-defs` clean with no runtime changes.
* Define the public API surface (`adhanpy.__all__` plus `calculation`
  and `data` re-exports) and add `PrayerTimes.time_for_prayer(Prayer)`.

## v1.0.5
* Fix [#16](https://github.com/alphahm/adhanpy/issues/16) where method is either not provided or
explicitly set to `None` when initialising `CalculationParameters` results in an `AttributeError`
in `PrayerTimes`

## v1.0.4
* Fix [#4](https://github.com/alphahm/adhanpy/issues/4) where rounding of minutes function tried to
incorrectly set 60 for minutes on a datetime object.
* Bring support for Python 3.9
