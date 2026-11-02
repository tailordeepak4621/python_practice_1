# Day 2 Solution
def is_leap_year(year: int) -> bool:
    # A year is leap if divisible by 4 and not 100, OR divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test driver
if __name__ == "__main__":
    test_years = [1900, 2000, 2024, 2026]
    for y in test_years:
        status = "a Leap Year" if is_leap_year(y) else "NOT a Leap Year"
        print(f"Year {y} is {status}.")
