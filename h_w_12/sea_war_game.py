import random
import os


class Player:
    def __init__(self, name):
        self.name = name
        self.cnt_ships = 8
        self.place_1 = [['~' for _ in range(10)] for _ in range(10)]
        self.place_2 = [['~' for _ in range(10)] for _ in range(10)]

    def creat_place_1(self):
        coordinates_ships = []
        while len(coordinates_ships) < self.cnt_ships:
            temp = [random.randint(0, 9), random.randint(0, 9)]
            if temp not in coordinates_ships:
                coordinates_ships.append(temp)
                self.place_1[temp[1]][temp[0]] = 'o'


class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def run(self):
        self.player_1.creat_place_1()
        self.player_2.creat_place_1()
        active_player = self.player_1
        passive_player = self.player_2

        os.system('cls')
        while True:
            input(f'Ходит {active_player.name}, для начала нажмите "Enter"')
            os.system('cls')
            print(self.paint_place(active_player.name, active_player.place_1, active_player.place_2))
            while True:
                coordinates_shot_x = input('Введите координуту по Х: ')
                coordinates_shot_y = input('Введите координуту по Y: ')
                rez_check = self.check_shot_coordinates(active_player,
                                                        {'X': coordinates_shot_x, 'Y': coordinates_shot_y})
                if not rez_check[0]:
                    print(rez_check[1])
                    continue
                break

            rez_shot = self.rez_shot(active_player, passive_player, int(coordinates_shot_x)-1,
                                     int(coordinates_shot_y)-1)
            if not passive_player.cnt_ships:
                os.system('cls')
                print(f'Игра закончена, победил: {active_player.name}')
                break
            if rez_shot:
                print("Вы потопили вражеский корабль!")
            else:
                print("Вы промахнулись!")
            input('Для завершения хода нажмите "Enter"')
            os.system('cls')
            active_player, passive_player = passive_player, active_player

    @staticmethod
    def rez_shot(player_attack, player, x, y):
        if player.place_1[y][x] is 'o':
            player.place_1[y][x] = 'x'
            player_attack.place_2[y][x] = 'x'
            player.cnt_ships -= 1
            return True
        player.place_1[y][x] = '*'
        player_attack.place_2[y][x] = '*'
        return False

    @staticmethod
    def check_shot_coordinates(player, dict_coordinates):
        for key, value in dict_coordinates.items():
            if not value.isdigit():
                return [False, f"Координата {key} не является числом, повторитте ввод сначала!"]
            dict_coordinates[key] = int(value)
            if not dict_coordinates[key] or dict_coordinates[key] > 10:
                return [False, f"Координата {key} не в диапазоне чисел от 1 до 10!"]

        if player.place_2[dict_coordinates['Y']-1][dict_coordinates['X']-1] is not '~':
            return [False, "По этой координате уже был выполнен выстрел рание!"]

        return [True]

    @staticmethod
    def paint_place(name, list_coordinates_1, list_coordinates_2):
        str_text = f'{" " * 10}Корабли{" " * 29}Выстрелы\n'
        for y in range(10):
            for x in list_coordinates_1[y]:
                str_text += f'{x}  '

            str_text += ' ' * 5

            for x in list_coordinates_2[y]:
                str_text += f'{x}  '

            str_text += '\n'

        return f'\nХод игрока {name}\n\n{str_text}'


os.system('cls')
player_name_1 = input("Введите имя первого игрока: ")
player_name_2 = input("Введите имя второго игрока: ")

player_one = Player(player_name_1)
player_two = Player(player_name_2)

game = Game(player_one, player_two)
game.run()
