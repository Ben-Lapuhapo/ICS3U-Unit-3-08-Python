# usr/bin/env python3

# Created by Ben Lapuhapo
# Created on Oct 2019
# This Program determines if a year is a leap year


def main():
    while True:
        try:
            # Input
            # calculates if year is a leap year
            year = int(input("Enter a year: "))
            print("")

            # Output and Process
            if year % 4 == 0 and year % 100 != 0:
                print("It is a leap year")
            if year % 4 != 0:
                print("It is not a leap year")
            if year % 4 == 0 and year % 100 == 0:
                if year % 400 != 0:
                    print("It is not a leap year")
                if year % 400 == 0 and year % 100 == 0:
                    print("It is a leap year")

        except ValueError:
            print("")
            print("Invalid Input, Please Try Again")
            print("")

        else:
            break


if __name__ == "__main__":
    main()
