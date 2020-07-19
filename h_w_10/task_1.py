"""Без использования библиотек, создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд."""


class Time:

    def __init__(self, h=0, m=0, s=0):
        self._hours = h
        self._minutes = m
        self._seconds = s

    def __repr__(self):
        return {'hours': self._hours, 'minutes': self._minutes, 'seconds': self._seconds}

    def __str__(self):
        rez = []
        if len(str(self._hours)) == 2:
            rez.append(self._hours)
        else:
            rez.append(f'0{self._hours}')

        if len(str(self._minutes)) == 2:
            rez.append(self._minutes)
        else:
            rez.append(f'0{self._minutes}')

        if len(str(self._seconds)) == 2:
            rez.append(self._seconds)
        else:
            rez.append(f'0{self._seconds}')

        return f'Точное время {rez[0]}:{rez[1]}:{rez[2]}'

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @property
    def seconds(self):
        return self._seconds

    @hours.setter
    def hours(self, value):
        self._hours = self.check_hours(value)

    @minutes.setter
    def minutes(self, value):
        if value > 59:
            self._minutes = 59
        else:
            self._minutes = value

    @seconds.setter
    def seconds(self, value):
        if value > 59:
            self._seconds = 59
        else:
            self._seconds = value

    @staticmethod
    def check_hours(value):
        if value > 23:
            return 23
        return value

    def change_time_by_hours(self, h):
        h += self._hours
        self._hours = self.check_hours(h)

    def change_time_by_minutes(self, m):
        m += self._minutes
        if m > 59:
            self._minutes = m % 60
            self.change_time_by_hours(m//60)
        else:
            self._minutes = m

    def change_time_by_seconds(self, s):
        s += self._seconds
        if s > 59:
            self._seconds = s % 60
            self.change_time_by_minutes(s//60)
        else:
            self._seconds = s


t = Time(h=1, m=1, s=1)
print(str(t))

t.hours = 5
t.minutes = 12
t.seconds = 34
print(str(t))

t.change_time_by_hours(26)
print(str(t))

t.hours = 5

t.change_time_by_minutes(61)
print(str(t))

t.change_time_by_seconds(3661)
print(str(t))
