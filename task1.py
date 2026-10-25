from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f"неправильний формат: '{date}'. використовуй фомат YYYY-MM-DD.")
        return None

    today = datetime.today().date()
    return (today - given_date).days


if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))
    print(get_days_from_today("2026-12-25"))
    print(get_days_from_today("ciao"))