from playwright.sync_api import Playwright, sync_playwright
from sys import argv
from datetime import datetime


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, timeout=5000)
    context = browser.new_context(ignore_https_errors=True)

    # Open new page
    page = context.new_page()

    page.goto(argv[1] or "https://www.yuque.com/kebayi/yuebao/vcm8d0")

    page.locator("text=登录 / 注册").click()

    page.locator("text=密码登录").click()

    page.locator("[data-testid=\"prefix-phone-input\"]").click()


    page.locator("[data-testid=\"prefix-phone-input\"]").fill("请修改用户名")

    page.locator("[data-testid=\"loginPasswordInput\"]").click()


    page.locator("[data-testid=\"loginPasswordInput\"]").fill("请修改密码")

    page.locator("[data-testid=\"protocolCheckBox\"]").check()

    with page.expect_navigation():
        page.locator("[data-testid=\"btnLogin\"]").click()

    # Click [data-testid="doc-create-entry"]
    for _ in range(int(argv[2]) or 10):
        try:
            try:
        
                page.locator(".larkui-icon.icon-svg.BookCatalog-module_actionItem_gOq-V").click(timeout=5000)

                with page.expect_navigation():
                    page.locator("text=新建文档").click(timeout=5000)

            except Exception:
                page.locator("[data-testid=\"doc-create-entry\"]").click(timeout=5000)

                with page.expect_navigation():
                    page.locator("[data-testid=\"doc-action-menu-item-create_doc\"] >> text=文档").click(timeout=5000)


            page.locator("[data-testid=\"input\"]").click(timeout=5000)

            page.locator("[data-testid=\"input\"]").fill(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            with page.expect_navigation():
                try:
                    page.locator("[data-testid=\"doc-exit-edit-button\"]").click(timeout=5000)
                except Exception:
                    page.locator("[data-testid=\"doc-publish-button\"]").click(timeout=5000)
        except Exception:
            continue

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
