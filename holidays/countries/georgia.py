#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars.gregorian import MAR, APR, MAY, OCT, NOV
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Georgia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Georgia holidays.

    References:
     - https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
     - https://matsne.gov.ge/en/document/view/1155567?publication=24
    """

    country = "GE"
    default_language = "ka"
    supported_languages = ("en_US", "ka", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1990:
            return None
        super()._populate(year)

        # New Year's Day.
        name = tr("ახალი წელი")
        self._add_new_years_day(name)
        self._add_new_years_day_two(name)

        # Christmas Day.
        self._add_christmas_day(tr("ქრისტეშობა"))

        # Epiphany.
        self._add_epiphany_day(tr("ნათლისღება"))

        # Mother's Day.
        self._add_holiday(tr("დედის დღე"), MAR, 3)

        # International Women's Day.
        self._add_womens_day(tr("ქალთა საერთაშორისო დღე"))

        # Good Friday.
        self._add_good_friday(tr("წითელი პარასკევი"))

        # Holy Saturday.
        self._add_holy_saturday(tr("დიდი შაბათი"))

        # Easter Sunday.
        self._add_easter_sunday(tr("აღდგომა"))

        # Easter Monday.
        self._add_easter_monday(tr("შავი ორშაბათი"))

        # National Unity Day.
        self._add_holiday(tr("ეროვნული ერთიანობის დღე"), APR, 9)

        # Day of Victory over Fascism.
        self._add_world_war_two_victory_day(tr("ფაშიზმზე გამარჯვების დღე"))

        # Saint Andrew's Day.
        self._add_holiday(tr("წმინდა ანდრია პირველწოდებულის დღე"), MAY, 12)

        # Independence Day.
        self._add_holiday(tr("დამოუკიდებლობის დღე"), MAY, 26)

        # Assumption of the Virgin Mary.
        self._add_assumption_of_mary_day(tr("მარიამობა"))

        # Holiday of Svetitskhovloba, Robe of Jesus.
        self._add_holiday(tr("მცხეთობის"), OCT, 14)

        # Saint George's Day.
        self._add_holiday(tr("გიორგობა"), NOV, 23)


class GE(Georgia):
    pass


class GEO(Georgia):
    pass
