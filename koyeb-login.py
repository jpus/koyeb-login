from playwright.sync_api import sync_playwright
import os
import requests

def send_telegram_message(message):
    bot_token = os.environ.get('TEL_TOK')
    chat_id = os.environ.get('TEL_ID')

    if not bot_token or not chat_id:
        return {"error": "Telegram token or chat ID is not set"}

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

def login_koyeb(email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 访问Koyeb登录页面
        page.goto("https://app.koyeb.com/auth/signin")

        # 输入邮箱和密码
        page.fill('input[name="email"]', email)
        page.fill('input[name="password"]', password)

        # 点击登录按钮并等待加载
        page.click('button[type="submit"]')

        try:
            # 等待可能的错误消息
            error_message = page.wait_for_selector('.MuiAlert-message', timeout=5000)
            if error_message:
                error_text = error_message.inner_text()
                return f"账号 {email} 登录失败: {error_text}"
        except:
            pass  # 忽略错误消息没有出现的异常

        # 检查是否成功跳转到仪表板
        try:
            page.wait_for_url("https://app.koyeb.com/", timeout=5000)
            return f"账号 {email} 登录成功!"
        except:
            return f"账号 {email} 登录失败: 未能跳转到仪表板页面"
        finally:
            browser.close()

if __name__ == "__main__":
    accounts = os.environ.get('KOY_ACC', '').split()

    if not accounts:
        error_message = "没有配置任何账号"
        send_telegram_message(error_message)
        print(error_message)
    else:
        login_statuses = []
        for account in accounts:
            try:
                email, password = account.split(';')
                status = login_koyeb(email, password)
                login_statuses.append(status)
                print(status)
            except Exception as e:
                login_statuses.append(f"账号 {account} 登录失败: {str(e)}")

        message = "Koyeb登录状态:\n\n" + "\n".join(login_statuses)
        result = send_telegram_message(message)
        print("消息已发送到Telegram:", result)
