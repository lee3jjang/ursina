from ursina import *

app = Ursina()

window.borderless = False
window.color = color._20

Text.default_font = 'fonts/DBGothicM.ttf'

gold = 0
gold_text = Text(text=str(gold), x=-0.02, y=0.2, scale=2, background=True)
button = Button(text='Click!', color=color.orange, scale=0.2)

def button_click():
    global gold
    gold += 1
    gold_text.text = str(gold)

button.on_click = button_click

auto_button_1 = Button(text='1G/초 (가격: 10G)', x=0.3, scale=0.2, disabled=True, cost=10, earn=1)

def auto_plus_gold(plus=1, interval=1):
    global gold
    gold += plus
    
    invoke(auto_plus_gold, plus, delay=interval)



def get_auto_gold():
    global gold

    if gold >= auto_button_1.cost:
        gold -= auto_button_1.cost

        invoke(auto_plus_gold, plus=1, interval=1) 

auto_button_1.on_click = get_auto_gold

def update():
    global gold
    gold_text.text = str(gold)

    if gold >= auto_button_1.cost:
        auto_button_1.disabled = False
        auto_button_1.color = color.green
    else:
        auto_button_1.disabled = True
        auto_button_1.color = color.gray

app.run()