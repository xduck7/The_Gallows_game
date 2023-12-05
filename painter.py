import turtle as tr

def head():
    tr.circle(20)

def body():
    tr.right(90)
    tr.forward(50)

def legs():
    tr.left(45)
    tr.forward(40)
    tr.back(40)
    tr.right(90)
    tr.forward(40)
    tr.back(40)
    tr.left(45)

def arms():
    tr.back(35)
    tr.right(90)
    tr.forward(30)
    tr.back(60)
    tr.forward(30)
    tr.title("GAME OVER")

def create_player():
    head()
    body()
    legs()
    arms()

def create_chair():
    tr.up()
    tr.left(90)
    tr.forward(65)
    tr.right(90)
    tr.down()
    tr.back(45)
    tr.forward(90)
    tr.left(90)
    tr.forward(20)

    tr.up()
    tr.left(90)
    tr.forward(90)
    tr.down()
    #print(tr.pos()) #для отладки

    tr.left(90)
    tr.forward(20)

def vertical_stick():
    tr.up()
    tr.left(90)
    tr.forward(110)
    tr.right(90)
    tr.down()
    tr.forward(200)

def horizontal_stick():
    tr.right(90)
    tr.forward(100)
    tr.back(20)

def rope():
    tr.right(90)
    tr.forward(120)

def loop():
    tr.right(135)            
    for loop in range(2):
        tr.circle(15,90)
        tr.circle(2,90)

def remove_chair():
    tr.up()
    tr.setposition(-45, -100)
    tr.down()
    tr.right(45)
    
    tr.color("white")

    tr.forward(20)
    tr.right(90)
    tr.forward(90)
    tr.right(90)
    tr.forward(20)
    print("GAME OVER!")

"""create_player()
create_chair()
vertical_stick()
horizontal_stick()
rope()
loop()
remove_chair()"""

def actions(hp):
    match hp:
        case 4:
            vertical_stick()
        case 3:
            horizontal_stick()
        case 2:
            rope()
        case 1:
            loop()
        case 0:
            remove_chair()
