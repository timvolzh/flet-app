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
    margin
)

stat_cube = ft.Stack(
    [ft.Container(
        content=ft.Text("+3", size=25, color="BLACK"),
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
            content=ft.Text("16", size=15, color="BLACK"),
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

    ],
    width=75,
    height=75,

)


def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE38
    page.add(ft.Text("Hello, world!"))
    page.add(stat_cube)


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

ft.app(target=main)  # , view=ft.WEB_BROWSER)
