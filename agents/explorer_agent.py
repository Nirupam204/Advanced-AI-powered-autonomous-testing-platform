from playwright.sync_api import sync_playwright


def explore_website(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)

        title = page.title()
        html_content = page.content()

        forms = page.locator("form").count()
        password_fields = page.locator("input[type='password']").count()
        links = page.locator("a").count()

        load_time = page.evaluate(
            "performance.timing.loadEventEnd - performance.timing.navigationStart"
        )

        browser.close()

        return {
            "title": title,
            "content": html_content[:2000],
            "forms": forms,
            "password_fields": password_fields,
            "links": links,
            "load_time": load_time
        }