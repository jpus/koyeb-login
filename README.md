## koyeb自动化批量保号，每周五自动登录一次面板，并且发送消息到Telegram

### 将代码fork到你的仓库并运行的操作步骤

#### 1. Fork 仓库

1. **访问原始仓库页面**：
    - 打开你想要 fork 的 GitHub 仓库页面。

2. **Fork 仓库**：
    - 点击页面右上角的 "Fork" 按钮，将仓库 fork 到你的 GitHub 账户下。

#### 2. 设置 GitHub Secrets

1. **创建 Telegram Bot**
    - 在 Telegram 中找到 `@BotFather`，创建一个新 Bot，并获取 API Token。
    - 示例值: `1234567890:ABCDEFghijklmnopQRSTuvwxyZ`    
    - 获取到你的 Chat ID 方法一，使用第三方电报查看电报用户`ID`就是Chat ID
    - 示例值: `1234567890`    
    - 获取到你的 Chat ID 方法二，可以通过在 Bot 里自己向 Bot 发送一条消息，然后浏览器访问 `https://api.telegram.org/bot<your_bot_token>/getUpdates` 
    - 示例 : `https://api.telegram.org/bot1234567890:ABCDEFghijklmnopQRSTuvwxyZ/getUpdates` 显示chat下的id就是 Chat ID 

2. **配置 GitHub Secrets**
    - 转到你 fork 的仓库页面。
    - 点击 `Settings`，然后在左侧菜单中选择 `Secrets and variables` > `Actions`。
    - 添加以下 Secrets, 上方框为变量名，下文框为变量值，创建完一个变量名和变量值保存后再创建另一个变量名和变量值，以此类推：
        - `KOY_ACC`: 账号1:密码 账号2:密码 账号3:密码 `(账号与密码之间使用;密码与另一帐号之间使用空格)`
        - `TEL_TOK`: 你的 Telegram Bot 的 API Token。
        - `TEL_ID`: 你的 Telegram Chat ID。

#### 3. 启动 GitHub Actions

1. **配置 GitHub Actions**
    - 在你的 fork 仓库中，进入 `Actions` 页面。
    - 如果 Actions 没有自动启用，点击 `Enable GitHub Actions` 按钮以激活它。

2. **运行工作流**
    - GitHub Actions 将会根据你设置的定时任务（例如每三天一次）自动运行脚本。
    - 如果需要手动触发，可以在 Actions 页面手动运行工作流。

### 注意事项

- **保密性**: Secrets 是敏感信息，请确保不要将它们泄露到公共代码库或未授权的人员。
- **更新和删除**: 如果需要更新或删除 Secrets，可以通过仓库的 Secrets 页面进行管理。
