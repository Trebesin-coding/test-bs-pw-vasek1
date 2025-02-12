from playwright.sync_api import sync_playwright



def main():

     with sync_playwright() as p:
         login = "Jarmil"
         password = "Admin123"

         browser = p.chromium.launch(headless=False)
         page = browser.new_page()

         page.goto("https://js-trebesin.github.io/playwright-exam/")
         page.fill('input[id="login"]',login)
         page.fill('input[id="pass"]',password)
         page.click('button[class="login-btn"]')
         
         jarmil = page.locator('div[class="psst"]').text_content()

         print(jarmil)

         input("vypni")

         browser.close()
    

if __name__ == "__main__":
    main()
