#Find text from sites from in between <p> </p> or ""
#Transfer text to a text file for easier search

import urllib.request
from tkinter import *

#Enter URL
URL = ""


def listToString(susbtring):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(substring))

def listToString2(check):
    # initialize an empty string
    str2 = " "

    # return string
    return (str2.join(check))

def listToString3(final):
    # initialize an empty string
    str3 = " "

    # return string
    return (str3.join(final))

def stringToList(substring):
    substring = list(substring.split("."))
    return substring

def splitA1(check):
    substring = list(check.split("<a>"))
    return substring

def splitA2(check):
    substring = list(check.split("</a>"))
    return substring


page = urllib.request.urlopen(URL)
fullHtml = (page.read())
text = str(fullHtml)

pattern = "<p(.*?)</p>"

substring = re.findall(pattern, text)

substring = listToString(substring)


pattern2 = "<a(.*?)</a>"

check = re.findall(pattern2, substring)

check = listToString2(check)

check = splitA1(check)
#check = splitA2(check)
print(check)

if str(check) in substring:
    substring.remove(check)

substring = stringToList(substring)

b = len(substring)

print(b)


while b > 1:
    b = (int(b) - 1)

    substring.insert(b, "\n")

    if b == 1:
        break

    else:
        continue

print(substring)



f = open("text.txt", "w")

for line in substring:
    f.write(line)
    f.write('\n')

f.close()

