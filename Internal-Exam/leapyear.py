# CO1 Q2: Display future leap years

start = int(input("Enter current year: "))
end = int(input("Enter final year: "))

for year in range(start, end + 1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)

