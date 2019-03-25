import requests
import re

def getHtml(url):
    try:
        r = requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('time out')
        return ''

def getList(html,mList):
    nameList = re.findall(r'<span class="a-size-.+ a-color-base a-text-normal">.+</span>',html)
    for i in nameList:
        name = i.split('>')[1].split('<')[0]
        mList.append(name)
    return mList

def printList(mList):
    for i in mList:
        print(i)
    input()

def main():
    url1 = 'https://www.amazon.com/s?k='
    keyWord = input('Tell me what you want to search:')
    url1 += keyWord+'&page='
    depth = input('How many pages you want to search:')
    mList = []
    for i in range(int(depth)):
        print('{}%'.format(i*100//int(depth)))
        url = url1 + str(i+1)
        html = getHtml(url)
        mList = getList(html,mList)
    printList(mList)

main()
