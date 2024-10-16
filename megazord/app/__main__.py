"""
This script uses Playwright to automate browser actions.

Functions:
    run(playwright: Playwright) -> None:
        Launches a Chromium browser, navigates to "http://example.com", 
        performs other actions, and then closes the browser.

Usage:
    The script initializes Playwright in synchronous mode and calls the `run` function.
"""
import re
from playwright.sync_api import Playwright, sync_playwright

from app.google.sheet.add import add_promotion


def run(pw: Playwright) -> None:  # pylint: disable=C0116
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://promohub.com.br/")    
    page.wait_for_selector(".flex-row > div")
    itens = page.locator(".flex-row > div")
    promos = []    
    for item in itens.all():
        img = item.locator("img").get_attribute("src")
        title = item.locator("div.text-lg.font-light").inner_text()
        price = item.locator("div.text-xl.font-bold > div").first.inner_text()
        link = item.locator("a").get_attribute("href")
        url_pattern = re.compile(r'^(https?://[^/]+)')
        match = url_pattern.match(link)
        source_key = link.replace(match.group(1), '')

        promos.append({
            'Source': 'promohub',
            'SourceKey': source_key,
            'Title': title,
            'Price': price.replace('R$', '').strip(),
            'Link': link,
            'ImageLink': img,
            'Date': '15/10/2024'
        })
    add_promotion(promos)

    # ---------------------
    context.close()
    browser.close()


if __name__ == "__main__":
    # pylint: disable=line-too-long
    # add_promotion([{'Source': 'rsn2',
    #                'SourceKey': '/promocoes/236703/cerveja-hoegaarden-269ml-lata-8-unidades',
    #                'Title': 'Cerveja Hoegaarden 269ml Lata 8 Unidades',
    #                'Price': 'R$30,11',
    #                'Link': 'https://www.magazinevoce.com.br/magazinegatry/cerveja-hoegaarden-269ml-lata-8-unidades/p/232270200/me/cvej/',
    #                'ImageLink': 'https://cdn.gatry.com/gatry-static/promocao/imagem/ecea094a35131af5b6d01812da6f7ae0.png',
    #                'Date': '15/10/2024'}])
    with sync_playwright() as playwright:
        run(playwright)
