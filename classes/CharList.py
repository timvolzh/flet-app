import flet as ft
from classes.Char import Char


class CharList(ft.Page):

    def _stat_cube(self, parameter_name: str, parameter_value: int = 10, parameter_name_size: int = 12) -> ft.Stack:
        if int((parameter_value - 10) / 2) > 0:
            parameter_bonus = f"+{int((parameter_value - 10) / 2)}"
        else:
            parameter_bonus = f"{int((parameter_value - 10) / 2)}"

        cube = ft.Stack(
            [ft.Container(
                content=ft.Text(parameter_bonus, size=25, color="BLACK"),
                margin=0,
                padding=0,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE,
                width=70,
                height=70,
                border_radius=10,
                border=ft.border.all(2, ft.colors.BLACK)
            ),
                ft.Container(
                    content=ft.Text(str(parameter_value), size=15, color="BLACK"),
                    width=30,
                    height=25,
                    margin=0,
                    padding=0,
                    border=ft.border.all(2, ft.colors.BLACK),
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    right=25,
                    bottom=0,

                ),
                ft.Container(
                    content=ft.Text(parameter_name, size=parameter_name_size, color="BLACK"),
                    alignment=ft.alignment.center,
                    width=75,
                    top=2

                )

            ],
            width=75,
            height=75,

        )
        return cube

    def stat_block(self, char):
        block = ft.Column(
            controls=[
                self._stat_cube("Сила", char.strength),
                self._stat_cube("Телосложение", char.constitution, 10),
                self._stat_cube("Ловкость", char.dexterity),
                self._stat_cube("Интелект", char.intelligence),
                self._stat_cube("Мудрость", char.wisdom),
                self._stat_cube("Харизма", char.charisma),
            ]
        )
        return block

    # !!!!!!!!!!!!!!!!!!!!!!!!
    def saving_throws(self, base_bonus: int = 0):
        def saving_throw(parameter_name: str = None, parameter_bonus: int = 0) -> ft.Row:

            def checkbox_change(box):

                pass

            if parameter_bonus > 0:
                parameter_bonus = f"+{parameter_bonus}"
            elif parameter_bonus == 0:
                parameter_bonus = f" {parameter_bonus}"

            throw = ft.Row(controls=[
                ft.Checkbox(value=False, shape=ft.RoundedRectangleBorder(radius=25)),
                ft.Text(f"{parameter_bonus}", size=15, color="BLACK"),
                ft.Text(parameter_name, size=15, color="BLACK"),
            ],
                spacing=10,
                height=20,
            )
            return throw

        throws = ft.Column(controls=[
            saving_throw('Сила', 3),
            saving_throw('Ловкость', 0),
            saving_throw('Телосложение', -1),
            saving_throw('Интелект'),
            saving_throw('Мудрость'),
            saving_throw('Харизма'),

        ],
            spacing=0,

        )

        return throws

    # !!!!!!!!!!!!!!!!!!!!!!!!
    def skill_throws(self):
        def skill_throw(skill_name: str = None, stat_bonus: int = 0, base_bonus: int = 0, is_prof: bool = False, ):
            if is_prof:
                skill_bonus = stat_bonus + base_bonus
            else:
                skill_bonus = stat_bonus
            throw = ft.Row(controls=[
                ft.Checkbox(value=is_prof, shape=ft.RoundedRectangleBorder(radius=25)),
                ft.Text(f"{skill_bonus}", size=15, color="BLACK"),
                ft.Text(skill_name, size=15, color="BLACK"),
            ],
                spacing=10,
                height=20,

                alignment=ft.alignment.top_center
            )
            return throw

        throws = ft.Column(controls=[
            skill_throw("Акробатика", 3, 2, False),
            skill_throw("Анализ", 1, 2, True),
            skill_throw("Атлетика", 3, 2, False),
            skill_throw("Восприятие", 2, 2, False),
            skill_throw("Выживание", 1, 2, True),
            skill_throw("Выступление", 3, 2, False),
            skill_throw("Запугивание", 2, 2, True),
            skill_throw("История", 3, 2, False),
            skill_throw("Ловкость рук", 1, 2, False),
            skill_throw("Магия", 1, 2, False),
            skill_throw("Медицина", 2, 2, False),
            skill_throw("Обман", 3, 2, False),
            skill_throw("Природа", 1, 2, False),
            skill_throw("Проницательность", 2, 2, True),
            skill_throw("Религия", 2, 2, False),
            skill_throw("Скрытность", 2, 2, False),
            skill_throw("Убеждение", 1, 2, False),
            skill_throw("Уход за животными", 1, 2, True),
        ],
            spacing=0,
        )

        return throws

    def format(self, char):
        first_column = ft.Column(controls=[ft.Row([self.stat_block(),
                                                   ft.Column([
                                                       self.saving_throws(),
                                                       self.skill_throws(), ]),
                                                   ]),
                                           ft.Row([ft.Container(
                                               content=ft.Text("13", size=20, color="BLACK"),
                                               margin=0,
                                               padding=0,
                                               alignment=ft.alignment.center,
                                               bgcolor=ft.colors.WHITE,
                                               width=35,
                                               height=35,
                                               border_radius=5,
                                               border=ft.border.all(2, ft.colors.BLACK)
                                           ),
                                               ft.Container(
                                                   content=ft.Text("ПАССИВНАЯ МУДРОСТЬ (ВОСПРИЯТИЕ)", size=10,
                                                                   color="BLACK"),
                                                   margin=0,
                                                   padding=0,
                                                   alignment=ft.alignment.center,
                                                   bgcolor=ft.colors.WHITE,
                                                   width=250,
                                                   height=25,
                                                   border_radius=5,
                                                   border=ft.border.all(2, ft.colors.BLACK)
                                               )],
                                               spacing=0
                                           ),
                                           ])
        return self.add(first_column)

    def build(self, char: Char = None):
        self.bgcolor = ft.colors.WHITE
        self.add(ft.Text("Hello, world!!!!!"))
        # page.add(ft.Text("Hello, world!"))
        # page.add(saving_throws())
        # self.add(self.stat_block())
        # self.add(format(char))
