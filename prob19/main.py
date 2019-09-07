from datetime import date

def main():
    dates = [date(year, month, 1) for year in range(1901, 2001)
                                  for month in range(1, 13)]

    days = [dt.strftime("%A") for dt in dates]

    sundays = [day for day in days if day == "Sunday"]

    print(len(sundays))

if __name__ == "__main__":
    main()
