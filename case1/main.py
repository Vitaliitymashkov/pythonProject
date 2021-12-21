from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "95.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

print('test')