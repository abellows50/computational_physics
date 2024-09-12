from vpython import *
BOXL = 10
BOXW = BOXL/5

global  has_covid
has_covid=False
global covid_chance 
covid_chance = 0.20
covid_test_box = box(pos=vec(0,0,0), height=BOXL, length=BOXW)

def test():
    global has_covid
    has_covid = random() < covid_chance
    print(has_covid)

def changeChance():
    global covid_chance
    covid_chance = covid_chance_slider.value/100
    print(covid_chance)

test = button(text="Run the Test",bind = test)
covid_chance_slider = slider(text="covid chance",min=0,max=100,value=50,bind=changeChance)

while True:
    if has_covid:
        covid_test_box.color = color.red
    else:
            covid_test_box.color = color.green
    rate(10)
    