import os, random,requests
from lxml import html
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('celery')
app.config_from_object('django.conf:settings', namespace='CELERY')


choiceList=['book','video']
base_url = "https://www.google.com/search?q="


@app.task()
def schedule(resolution,phone_number):
    choice = random.randint(0, 1)
    choice = choiceList[choice]
    if choice=='book':
        url="{0}i want to {1}&tbm=bks".format(base_url,resolution)
        resp = requests.get(url)
    elif choice=='video':
        url="{0}i want to {1}&tbm=vid".format(base_url,resolution)
    resp = requests.get(url)
    page = html.fromstring(resp.text)
    another_choice = random.randint(0, 9)
    link = page.xpath('//div[@class="kCrYT"][1]/a/@href')[another_choice]
    title = page.xpath('//div[@class="BNeawe vvjwJb AP7Wnd"]/text()')[another_choice]
    if choice=='video':
        link="www.google.com"+link
    #sendtwilio with phone_number
    return title,phone_number
    