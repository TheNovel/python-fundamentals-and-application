from datetime import date, timedelta

year, month, day = map(int, input().split())
start = date(year, month, day)

delta = timedelta(days=int(input()))

result = start + delta

print(result.year, result.month, result.day)
