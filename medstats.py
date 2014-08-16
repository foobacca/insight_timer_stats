#!/usr/bin/env python

import csv
from datetime import date, datetime, timedelta
import sys


def read_csv_data(csvfilename):
    dates = {}
    with open(csvfilename) as csvfile:
        insightreader = csv.reader(csvfile)
        for index, row in enumerate(insightreader):
            # skip the first two lines
            if index < 2:
                continue
            # the date is formatted like 08/16/2014 11:33:11
            sitting_date = datetime.strptime(row[0], "%m/%d/%Y %H:%M:%S").date()
            duration = int(row[1])
            if sitting_date not in dates:
                dates[sitting_date] = []
            dates[sitting_date].append(duration)
    return dates


def percent_sat_in_last_year(dates):
    days_sat = 0
    for i in xrange(365):
        olddate = date.today() - timedelta(i)
        if olddate in dates:
            days_sat += 1
    return days_sat / 365.0


def main():
    dates = read_csv_data("insight_connect_export_20140816.csv")
    #import pprint
    #pprint.pprint(dates, width=2)
    print "Sat %.1f%% days in last year" % (100 * percent_sat_in_last_year(dates))
    return 0

if __name__ == "__main__":
    sys.exit(main())
