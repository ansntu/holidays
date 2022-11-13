#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import EASTER_ORTHODOX, easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Bulgaria(HolidayBase):
    """
    Official holidays in Bulgaria in their current form. This class does not
    any return holidays before 1990, as holidays in the People's Republic of
    Bulgaria and earlier were different.

    Most holidays are fixed and if the date falls on a Saturday or a Sunday,
    the following Monday is a non-working day. The exceptions are (1) the
    Easter holidays, which are always a consecutive Friday, Saturday, and
    Sunday; and (2) the National Awakening Day which, while an official holiday
    and a non-attendance day for schools, is still a working day.

    Sources (Bulgarian):
    - http://lex.bg/laws/ldoc/1594373121
    - https://www.parliament.bg/bg/24
    - https://kik-info.com/spravochnik/calendar/2021/

    Sources (English):
    - https://en.wikipedia.org/wiki/Public_holidays_in_Bulgaria
    """

    country = "BG"

    def _populate(self, year):
        super()._populate(year)

        if year < 1990:
            return

        # New Year's Day
        self[date(year, JAN, 1)] = "Нова година"

        # Liberation Day
        self[
            date(year, MAR, 3)
        ] = "Ден на Освобождението на България от османско иго"

        # International Workers' Day
        self[
            date(year, MAY, 1)
        ] = "Ден на труда и на международната работническа солидарност"

        # Saint George's Day
        self[
            date(year, MAY, 6)
        ] = "Гергьовден, Ден на храбростта и Българската армия"

        # Bulgarian Education and Culture and Slavonic Literature Day
        self[date(year, MAY, 24)] = (
            "Ден на светите братя Кирил и Методий, на българската азбука, "
            "просвета и култура и на славянската книжовност"
        )

        # Unification Day
        self[date(year, SEP, 6)] = "Ден на Съединението"

        # Independence Day
        self[date(year, SEP, 22)] = "Ден на Независимостта на България"

        # National Awakening Day
        self[date(year, NOV, 1)] = "Ден на народните будители"

        # Christmas
        self[date(year, DEC, 24)] = "Бъдни вечер"
        self[date(year, DEC, 25)] = "Рождество Христово"
        self[date(year, DEC, 26)] = "Рождество Христово"

        # Easter
        dt = easter(year, method=EASTER_ORTHODOX)
        self[dt - rd(days=2)] = "Велики петък"
        self[dt - rd(days=1)] = "Велика събота"
        self[dt] = "Великден"
        self[dt + rd(days=1)] = " Великден"


class BG(Bulgaria):
    pass


class BLG(Bulgaria):
    pass
