N = int(input())
years = N //365
remaining_days = N % 365 
months = remaining_days // 30
days = remaining_days % 30
print(years,"years")
print(months,"months")
print(days,"days")