import flet as ft


class Sense(ft.Container):
    def __init__(
            self,
            icon: str,
            sense: str,
            left: int | float,
            icon_left: int | float,
            top: int | float = 241,
            icon_top: int | float = 260
    ) -> None:
        self.__icon = icon
        self.sense = sense
        self.__top = top
        self.__left = left
        self.icon_top = icon_top
        self.icon_left = icon_left
        super().__init__()
        self.alignment = ft.alignment.center
        self.width ,self.height = 58, 73
        self.bgcolor = "#FBFFF4"
        self.top, self.left = self.__top, self.__left
        self.border_radius = ft.border_radius.all(value=25)
        self.padding = ft.padding.only(top=12)
        self.ink = True
        self.shadow = ft.BoxShadow(
            blur_radius=10,
            color=ft.colors.with_opacity(opacity=25, color=ft.colors.GREY)
        )

        self.__icon = ft.Image(
            src=self.__icon,
            width=25,
            height=25,
            #top=self.icon_top,
            #left=self.icon_left,
            color="#5A8E05"
        )

        self.__text = ft.Text(
            value=self.sense,
            color="#5A8E05",
            #top=287,
            #left=self.icon_left,
            size=13,
            font_family="Poppins",
            weight=ft.FontWeight.BOLD
        )

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.__icon,
                self.__text
            ]
        )


class Doctor(ft.Row):
    def __init__(self, doctor_image: str, doctor_name: str, top: int | float):
        self.doctor_image = doctor_image
        self.doctor_name = doctor_name
        self.__top = top
        super().__init__()
        self.width = 234
        self.height = 90
        self.top = top
        self.left = 28

        self.image_doctor = ft.Image(
            src=self.doctor_image,
            width=88.71, height=90,
        )

        self.name = ft.Text(
            value=f"Dr.{self.doctor_name}",
            size=19,
            weight=ft.FontWeight.BOLD,
            font_family="Poppins",

        )



        self.column = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0,
            controls=[
                self.name,
                self.__text("Medicine Expert"),
                self.__text("ABCD Hospital"),
            ]
        )

        self.controls = [
            self.image_doctor,
            self.column
        ]

    @staticmethod
    def __text(text: str) -> ft.Text:
        return ft.Text(
            value=f"Dr.{text}",
            size=13,
            weight=ft.FontWeight.W_700,
            font_family="Poppins",
            color="#3C3C3C"
        )


class BottomAppBar(ft.BottomAppBar):
    def __init__(self):
        super().__init__()
        self.height = 60
        self.bgcolor = ft.colors.TRANSPARENT
        self.shadow_color = ft.colors.BLACK
        self.elevation = 7
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=8)
        self.__bottom = ft.Container(
            height=55,
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.only(top_left=30, top_right=30),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.__icon(ft.icons.HOME, True),
                    self.__icon(ft.icons.EMAIL),
                    self.__icon(ft.icons.SETTINGS),
                    self.__icon(ft.icons.PERSON),
                ]
            )

        )

        self.content = self.__bottom

    @staticmethod
    def __icon(name: str, selected: bool = False) -> ft.IconButton:
        return ft.IconButton(
            icon=name,
            icon_color="#5A8E05" if selected else "#C1C1C1",
            icon_size=40,
        )


class Home(ft.View):

    def __init__(self):
        super().__init__(
            route="/home",
            padding=ft.padding.only(left=0, right=0, bottom=0, top=-20),
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor=ft.colors.WHITE
        )

        self.bottom_appbar = BottomAppBar()

        self.__avatar = ft.Container(
            content=ft.Image(
                src=r"faces\omar.png",
                width=100, height=80.24*1.2
            ),
            width=68, height=68,
            left=28, top=55,
            bgcolor=ft.colors.RED,
            border_radius=180
        )

        self.__hello = ft.Text(
            value="Hello, Omar Blefeki",
            size=16,
            color=ft.colors.BLACK,
            font_family="Poppins",
            weight=ft.FontWeight.BOLD,
            left=116, top=68
        )

        self.__help = ft.Text(
            value="How can I help you?",
            size=13,
            color="#4F4F4F",
            font_family="Poppins",
            weight=ft.FontWeight.W_500,
            left=116, top=92
        )

        self.__notification = ft.Container(
            content=ft.Image(
                src=r"senses\notification.png",
                width=50, height=50,
            ),
            bgcolor="white",
            left=289, top=64,
            border_radius=180,
            shadow=ft.BoxShadow(
                blur_radius=10,
                color=ft.colors.with_opacity(30, "grey")

            )
        )

        self.__search = ft.Container(
            content=ft.SearchBar(
                width=311, height=45,
                expand=True,
                bar_bgcolor=ft.colors.WHITE,
                bar_leading=ft.Icon(name=ft.icons.SEARCH, color=ft.colors.BLACK),
                divider_color=ft.colors.BLACK,
                bar_hint_text="Search ...",
            ),
            left=28, top=144
        )

        self.__cat = ft.Text(
            value="Category",
            size=19,
            font_family="Poppins",
            top=205, left=28,
            weight=ft.FontWeight.BOLD
        )

        self.__see = ft.Text(
            value="See all",
            size=13,
            font_family="Poppins",
            top=205, left=307,
            weight=ft.FontWeight.BOLD,
            color="#5A8E05"
        )

        self.__pop_doc = ft.Text(
            value="Popular Doctor",
            size=19,
            font_family="Poppins",
            top=335, left=28,
            weight=ft.FontWeight.BOLD
        )

        self.__see2 = ft.Text(
            value="See all",
            size=13,
            font_family="Poppins",
            top=335, left=307,
            weight=ft.FontWeight.BOLD,
            color="#5A8E05"
        )

        self.__screen = ft.Container(
            bgcolor=ft.colors.WHITE,
            width=360,
            height=750,
            content=ft.Stack(
                controls=[
                    self.__avatar,
                    self.__hello,
                    self.__help,
                    self.__notification,
                    self.__search,
                    self.__cat,
                    self.__see,
                    Sense(
                        icon=r"senses\skin.png",
                        sense="Skin",
                        left=18,
                        icon_left=35
                    ),
                    Sense(
                        icon=r"senses\touth.png",
                        sense="Touth",
                        left=86,
                        icon_left=103
                    ),
                    Sense(
                        icon=r"senses\eye.png",
                        sense="Eye",
                        left=154,
                        icon_left=172
                    ),
                    Sense(
                        icon=r"senses\nose.png",
                        sense="Nose",
                        left=222,
                        icon_left=239
                    ),
                    Sense(
                        icon=r"senses\ear.png",
                        sense="Ear",
                        left=290,
                        icon_left=310
                    ),
                    self.__pop_doc,
                    self.__see2,
                    Doctor(
                        doctor_image=r"doctors\nassim.png",
                        doctor_name="Nassim Belfeki",
                        top=380
                    ),
                    Doctor(
                        doctor_image=r"doctors\oussema.png",
                        doctor_name="Oussema Belfeki",
                        top=486

                    ),
                    Doctor(
                        doctor_image=r"doctors\yassine.png",
                        doctor_name="Yassine Salhi",
                        top=592

                    )

                ]
            )
        )

        self.controls = [
            self.__screen,
        ]


def main(page):
    page.theme_mode = ft.ThemeMode.LIGHT
    def router(route: str) -> None:
        page.views.clear()

        if page.route == "/home":
            page.views.append(Home())
            page.update()

    page.on_route_change = router
    page.go("/home")

    page.update()



if __name__ == "__main__":
    ft.app(target=main)