from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
  
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday <= 6:
            congratulation_date = birthday_this_year

         
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Anna", "birthday": "1990.10.25"},
        {"name": "Marco", "birthday": "1985.10.28"},
        {"name": "Olena", "birthday": "1992.10.31"},
        {"name": "Taras", "birthday": "1988.11.05"},
        {"name": "Sofia", "birthday": "1995.10.20"},
    ]

    upcoming = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming)