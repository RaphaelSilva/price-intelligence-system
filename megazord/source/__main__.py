"""
This script uses Playwright to automate browser actions.

Functions:
    run(playwright: Playwright) -> None:
        Launches a Chromium browser, navigates to "http://example.com", 
        performs other actions, and then closes the browser.

Usage:
    The script initializes Playwright in synchronous mode and calls the `run` function.
"""
# import re
from playwright.sync_api import Playwright, sync_playwright

from source.google.sheet.add import add_promotion


def run(pw: Playwright) -> None:  # pylint: disable=C0116
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://promohub.com.br/")
    # /html/body/div/div/div/div/div[1]
    itens = page.locator(".flex > div")
    for item in itens.all():
        print(item.inner_text())

    # ---------------------
    context.close()
    browser.close()


if __name__ == "__main__":
    # pylint: disable=line-too-long
    add_promotion([{'Source': 'rsn2',
                   'SourceKey': '/promocoes/236703/cerveja-hoegaarden-269ml-lata-8-unidades',
                   'Title': 'Cerveja Hoegaarden 269ml Lata 8 Unidades',
                   'Price': 'R$30,11',
                   'Link': 'https://www.magazinevoce.com.br/magazinegatry/cerveja-hoegaarden-269ml-lata-8-unidades/p/232270200/me/cvej/',
                   'ImageLink': 'https://cdn.gatry.com/gatry-static/promocao/imagem/ecea094a35131af5b6d01812da6f7ae0.png',
                   'Date': '15/10/2024'}])
else:
    with sync_playwright() as playwright:
        run(playwright)
