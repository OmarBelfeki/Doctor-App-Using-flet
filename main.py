import time

from views.home_screen import Home
from views.splash_screen import Splash, SplashFirst

import flet as ft


def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 380
    page.window.height = 750
    page.window.top = 0.5
    page.window.left = 898
    page.padding = 0




    def router(route: str) -> None:
        page.views.clear()
        if page.route == "/":
            page.views.append(SplashFirst())
            page.update()
            time.sleep(0.3)
            page.views.clear()
            page.views.append(Splash())
            page.update()
        if page.route == "/home":
            page.views.append(Home())
            page.update()

    page.on_route_change = router
    page.go("/")
    page.update()


ft.app(target=main, assets_dir="assets")
