
"""Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и переопределения этих атрибутов в классе."""


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @property
    def mac_address(self):
        return self._mac_address

    @property
    def ip_address(self):
        return self._ip_address

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @login.setter
    def login(self, value):
        self._login = value

    @password.setter
    def password(self, value):
        self._password = value


a = ConnHandler(unit_name='1', mac_address='2', ip_address='3', login='4', password='5')
print(a.unit_name, a.mac_address, a.ip_address, a.login, a.password)

a.unit_name = a.mac_address = a.ip_address = a.login = a.password = '6'
print(a.unit_name, a.mac_address, a.ip_address, a.login, a.password)
