import re

from playwright.sync_api import Playwright, sync_playwright

from core.google.sheet import add, create, open
from core.google.folder import list

def create_sheet(file_name: str, sheet_name: str):
    spreadsheet = create.new_file(file_name, sheet_name)
    
    return spreadsheet


def run(pw: Playwright) -> None:  # pylint: disable=C0116
    file_name = "PromoHub"
    worksheet_name = "etl"

    files = filter(lambda x: x['name'] == file_name, list.folder())
    file = next(files, None)
    spreadsheet = open.sheet(file['id']) if file else create_sheet(file_name, worksheet_name)

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
        
    add.lines(promos, sheet_name=worksheet_name, spreadsheet=spreadsheet)

    # ---------------------
    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
