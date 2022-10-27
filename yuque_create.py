from playwright.sync_api import Playwright, sync_playwright
from datetime import datetime
from fire import Fire

def run(playwright: Playwright, url, times, username, password, headless) -> None:
    browser = playwright.chromium.launch(headless=headless, timeout=5000)
    context = browser.new_context(ignore_https_errors=True)

    page = context.new_page()
    page.goto(url)
    page.locator("text=登录 / 注册").click()
    page.locator("text=密码登录").click()
    
    page.locator("[data-testid=\"prefix-phone-input\"]").click()
    page.locator("[data-testid=\"prefix-phone-input\"]").fill(username)
    page.locator("[data-testid=\"loginPasswordInput\"]").click()
    page.locator("[data-testid=\"loginPasswordInput\"]").fill(password)


    page.locator("[data-testid=\"protocolCheckBox\"]").check()
    with page.expect_navigation():
        page.locator("[data-testid=\"btnLogin\"]").click()
        
    for i in range(1, int(times)+1):
        try:
            try:
                # //*[@id="asideHead"]/div[3]
                page.locator('//*[@id="asideHead"]/div[3]').click(timeout=5000)
                with page.expect_navigation():
                    page.locator("text=新建文档").click(timeout=5000)

            except Exception:
                page.locator("[data-testid=\"doc-create-entry\"]").click(timeout=5000)
                with page.expect_navigation():
                    page.locator("[data-testid=\"doc-action-menu-item-create_doc\"] >> text=文档").click(timeout=5000)

            page.wait_for_load_state('domcontentloaded')
            page.locator('//*[@id="lark-text-editor"]/div/div/div[4]/div[1]/div[2]/div/div/div[1]/div/textarea').click()
            page.locator('//*[@id="lark-text-editor"]/div/div/div[4]/div[1]/div[2]/div/div/div[1]/div/textarea').fill(f"{i:04} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f'已创建{i}个页面, 完成度{i/(int(times)):.2%}')
            
            with page.expect_navigation():
                try:
                    page.locator("[data-testid=\"doc-exit-edit-button\"]").click(timeout=5000)
                except Exception:
                    page.locator("[data-testid=\"doc-publish-button\"]").click(timeout=5000)
            page.wait_for_load_state('domcontentloaded')
        except Exception:
            continue

    context.close()
    browser.close()

def main(url = '', times = 10, username = '', password = '', headless = 0):
    with sync_playwright() as playwright:
        run(playwright, url, times, str(username), str(password), bool(headless))


if __name__ == '__main__':
    Fire(main)

