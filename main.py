import flet as ft
from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
)



def stat_cube(parameter_name: str, parameter_value: int = 10, parameter_name_size: int = 12) -> ft.Stack:
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


def stat_block():
    block = ft.Column(
        controls=[
            stat_cube("Сила", 18),
            stat_cube("Телосложение", 16, 10),
            stat_cube("Ловкость", 8),
            stat_cube("Интелект", 10),
            stat_cube("Мудрость", 12),
            stat_cube("Харизма", 8),
        ]
    )
    return block


def saving_throws(base_bonus: int = 0):
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


def skill_throws():
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


def format_page(page: ft.Page):
    first_column = ft.Column(controls=[ft.Row([stat_block(),
                                               ft.Column([
                                                   saving_throws(),
                                                   skill_throws(), ]),
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
                                               content=ft.Text("ПАССИВНАЯ МУДРОСТЬ (ВОСПРИЯТИЕ)", size=10, color="BLACK"),
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

    return first_column


def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    # page.add(ft.Text("Hello, world!"))
    # page.add(saving_throws())
    # page.add(stat_block())
    page.add(format_page(page))


'''
if __name__ == "__main__":
    def main(page: Page):
        page.title = "CharList"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = CharList(page)
        page.add(app)
        page.update()
'''

ft.app(target=main, view=ft.WEB_BROWSER)
