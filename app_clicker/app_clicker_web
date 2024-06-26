import flet as ft
from flet_core import Page
import asyncio


async def main(page: Page) -> None:
    page.title = 'Dolphin Kombat'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#191970'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {'PatsySans': 'PatsySans.otf'}
    page.theme = ft.Theme(font_family='PatsySans')

    async def score_coins_event_plus(event: ft.ContainerTapEvent) -> None:
        score_coins.data += 1
        score_coins.value = str(score_coins.data)
        image_dolphin.scale = 0.95
        counter_of_coins_click.opacity = 1
        counter_of_coins_click.value = '+1'
        counter_of_coins_click.right = 0
        # counter_of_coins_click.left = event.local_x
        # counter_of_coins_click.top = event.local_y
        counter_of_coins_click.bottom = 0
        progress_clicks.value += (1 / 100)  # Шкала кликов разделена на 100 делений, уведомление о каждых +100 кликов

        if score_coins.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='Дельфин пойман +100 Dolphins 🐬',
                    size=20,
                    color='#1E90FF',  # Dodger blue. Цвет фона всплывающего окна
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#000080'
            )
            page.snack_bar.open = True
            progress_clicks.value = 0

        await page.update_async()

        await asyncio.sleep(0.1)

        image_dolphin.scale = 1
        counter_of_coins_click.opacity = 0

        await page.update_async()

    score_coins = ft.Text(
        value='0',
        size=100,
        data=0
    )

    counter_of_coins_click = ft.Text(
        size=50,
        animate_opacity=ft.Animation(
            duration=500,
            curve=ft.AnimationCurve.BOUNCE_IN
            )
    )

    image_dolphin = ft.Image(
        src='dolphin1.png',
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(
            duration=500,
            curve=ft.AnimationCurve.EASE
        )
    )

    progress_clicks = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color='#1E90FF',
        bgcolor='#6495ED'
    )

    await page.add_async(
        score_coins,
        ft.Container(
            content=ft.Stack(
                controls=[
                    image_dolphin,
                    counter_of_coins_click
                ]
            ),
            on_click=score_coins_event_plus,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_clicks,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )


if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.FLET_APP,
        port=8080
    )
