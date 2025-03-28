from   dateutil.parser   import   parse
from   dateutil.relativedelta   import   relativedelta
from   datetime   import   datetime

class   BirthdayReminder:
    def __init__(self):
        self.birthdays   =   {}

    def add_birthday(self, name, birthday):
        self.birthdays[name]=parse(birthday)

    def get_upcoming_birthdays(self, days=30):
        today=datetime.now()
        upcoming=[]
        # print(f"{self.birthdays}")
        for name, bday in self.birthdays.items():
            next_birthday = bday.replace(year=today.year)
            # print(f"{name}的生日是{bday.strftime('%Y-%m-%d')},   距离下个生日还有{relativedelta(next_birthday, today).days}天")
            if next_birthday< today:
                next_birthday=next_birthday.replace(year=today.year+1)
            days_until=(next_birthday-today).days
            # print(f"{name}的下个生日是{next_birthday.strftime('%Y-%m-%d')}, {days_until}")
            # if days_until<=days:
            upcoming.append((name, next_birthday, days_until))

        return sorted(upcoming, key=lambda x:x[2])

#   使用示例
reminder=BirthdayReminder()
reminder.add_birthday("Alice",   "1990-05-15")
reminder.add_birthday("Bob",   "1985-11-29")
reminder.add_birthday("Charlie",   "1995-04-30")

upcoming=reminder.get_upcoming_birthdays()
# print(f"Upcoming birthdays: {upcoming}")

for name, bday, days  in upcoming:
    print(f"{name}的生日是{bday.strftime('%Y-%m-%d')},   还有{days}天")
