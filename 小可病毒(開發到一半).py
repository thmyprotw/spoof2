import webbrowser
for i in range(10):
    urL='https://drive.google.com/file/d/1EVcYWOzKNYWaxTpLfkvg863dFoEmz1aO/view?usp=share_link'#彩蛋
    chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new(urL)