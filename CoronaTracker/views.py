from django.http import HttpResponse
from django.shortcuts import render
import requests as req
from bs4 import BeautifulSoup as bs
def index(request):
    api_link = 'https://www.ndtv.com/coronavirus/india-covid-19-tracker'
    r = req.get(api_link)
    soup = bs(r.content,"html.parser")
    attr_filter = {'class': 'ind-mp_num'}
    result = soup.find_all(None, attr_filter)
    list1 = []
    for i in result:
        list1.append(str(i))
    list2 = []
    c = ""
    for i in list1:
        c = ""
        c = c + i[25:]
        list2.append(c)
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list3 = []
    for j in list2:
        c = ""
        for k in j:
            if k in number:
                c = c + k
            elif k == '<':
                break
            else:
                continue
        list3.append(c)
    info = list3[4:]
    params = {'total':info[0],'active':info[1],'recovered':info[2],'deaths':info[3]}

    return render(request,'CoronaTracker/home.html',params)
