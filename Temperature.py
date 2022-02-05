import urllib.request
from tkinter import *
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
check = 0

@sched.scheduled_job('interval', seconds=5)
def timed_job():
    page = urllib.request.urlopen("https://www.bbc.com/weather/292223")
    fullHtml = (page.read())
    text = str(fullHtml)

    pattern = "<span aria-hidden=\"true\">(.*?)</span>"
    substring = re.findall(pattern, text)

    str1 = " "
    substring = str1.join(substring)

    temperature = substring[0: 2]

    print(substring)
    print(temperature)

    file = "A:\\IntelliJ Idea\\CS Taster\\src\\temperature.txt"
    f = open(file, "w")
    f.write(temperature)
    f.close()

#sched.configure(options_from_ini_file)
sched.start()