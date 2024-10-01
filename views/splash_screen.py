import time
import asyncio

import flet as ft


class Splash(ft.View):

    def __init__(self):
        super().__init__(
            route="/",
            padding=ft.padding.only(left=0, right=0, bottom=0, top=30),
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor="#5A8E05"
        )

        self.__green_screen = ft.Container(
            bgcolor="#5A8E05",
            expand=True

        )

        self.__image = ft.Container(
            margin=ft.margin.only(left=40, right=41, top=30),
            border_radius=180,
            bgcolor=ft.colors.WHITE,
            width=279, height=263,
            content=ft.Image(
                src=r"splash\doctor_anime.png",
                width=279, height=263
            )
        )

        self.__text = ft.Text(
            value="Your Health",
            width=217, height=54,
            top=314, left=81,
            font_family="Poppins",
            weight=ft.FontWeight.W_700,
            size=36,
            color=ft.colors.WHITE
        )

        self.__text2 = ft.Text(
            value="Our Priority",
            width=187, height=48,
            top=361, left=87+9,
            font_family="Poppins",
            weight=ft.FontWeight.W_700,
            size=32,
            color=ft.colors.WHITE

        )

        self.__text3 = ft.Text(
            value="Consult the best doctors from here",
            width=246, height=21,
            top=432, left=57+9,
            font_family="Poppins",
            weight=ft.FontWeight.W_500,
            size=14,
            color="#DDDDDD"
        )

        self.__btn = ft.ElevatedButton(
            content=ft.Text(
                value="START",
                color="#5A8E05",
                font_family="Poppins",
                weight=ft.FontWeight.W_700,
                size=20,
            ),
            width=215, height=51,
            top=509, left=72+9,
            bgcolor=ft.colors.WHITE,
            on_click=lambda e: e.page.go("/home")
        )

        self.__splash = ft.Container(
            bgcolor="#5A8E05",
            width = 360,
            height = 750,
            content=ft.Stack(
                controls=[
                    self.__image,
                    self.__text,
                    self.__text2,
                    self.__text3,
                    self.__btn
                ]
            )
        )

        self.controls = [
            self.__splash,
        ]

    async def __animate_image(self):
        self.__image.offset = ft.Offset(x=0, y=0)
        self.__image.update()


    async def run(self) -> None:
        await asyncio.gather(self.__animate_image())




class SplashFirst(ft.View):
    def __init__(self):
        super().__init__(
            padding=0,
            bgcolor="#5A8E05"
        )
