from graphics import *
import winsound

def main():
    #frontend
    win = GraphWin("Akilibobo",1000,650)
    win.setCoords(0,0,20,20)
    win.setBackground("Black")
    
    lkj = Rectangle(Point(1.82,15),Point(17.2,5)).draw(win)
    lkj.setFill(color_rgb(148,87,235))
    lkj.setOutline(color_rgb(75,0,130))

    Saa = Image(Point(8,12.5),"Saa.gif").draw(win)
    Saa.setPixel(10,20,"Blue")

    Skidi = Image(Point(15.5,12.5),"Spidi.gif").draw(win)
    Skidi.setPixel(10,20,"Blue")

    mnb = Rectangle(Point(2.5,9.5),Point(16.5,5.5)).draw(win)
    mnb.setFill("White")

    own = Text(Point(10,10),"KwaKeyz 1.0").draw(win)
    own.setSize(18)
    own.setTextColor("white")
    own.setFace("courier")

    jkl = Polygon(Point(1.82,15),Point(2.2,15.3),Point(17.5,15.3),Point(17.2,15)).draw(win)
    jkl.setFill(color_rgb(75,0,130))
    jkl.setOutline(color_rgb(148,87,235))

    asd = Polygon(Point(17.5,15.3),Point(17.5,5.5),Point(17.2,5),Point(17.2,15)).draw(win)
    asd.setFill(color_rgb(75,0,130))
    asd.setOutline(color_rgb(148,87,235))

    Key = Rectangle(Point(2.5,9.5),Point(2.9,5.5)).draw(win)
    
    
    Acc_k = Rectangle(Point(2.8,9.5),Point(3,7)).draw(win)
    Acc_k.setFill("Black")
    Acc1_k = Rectangle(Point(5.6,9.5),Point(5.8,7)).draw(win)
    Acc1_k.setFill("Black")
    Acc2_k = Rectangle(Point(8.4,9.5),Point(8.6,7)).draw(win)
    Acc2_k.setFill("Black")
    Acc3_k = Rectangle(Point(11.2,9.5),Point(11.4,7)).draw(win)
    Acc3_k.setFill("Black")
    Acc4_k = Rectangle(Point(14,9.5),Point(14.2,7)).draw(win)
    Acc4_k.setFill("Black")

    
    

    
    
    k = 0.4
    for i in range(33):
        a = Key.clone()
        a.move(k ,0)
        k+=0.4
        a.draw(win)
        

    h = 0.4
    for j in range(1):
        o = Acc_k.clone()
        o.move(h,0)
        o.draw(win)
        h+=0.4
        for xh in range(3):
            l = o.clone()
            l.move(h,0)
            l.draw(win)
            h+=0.4
    h = 0.4
    for j in range(1):
        o = Acc1_k.clone()
        o.move(h,0)
        o.draw(win)
        h+=0.4
        for xh in range(3):
            l = o.clone()
            l.move(h,0)
            l.draw(win)
            h+=0.4
    h = 0.4
    for j in range(1):
        o = Acc2_k.clone()
        o.move(h,0)
        o.draw(win)
        h+=0.4
        for xh in range(3):
            l = o.clone()
            l.move(h,0)
            l.draw(win)
            h+=0.4
    h = 0.4
    for j in range(1):
        o = Acc3_k.clone()
        o.move(h,0)
        o.draw(win)
        h+=0.4
        for xh in range(3):
            l = o.clone()
            l.move(h,0)
            l.draw(win)
            h+=0.4
    h = 0.4
    for j in range(1):
        o = Acc4_k.clone()
        o.move(h,0)
        o.draw(win)
        h+=0.4
        for xh in range(3):
            l = o.clone()
            l.move(h,0)
            l.draw(win)
            h+=0.4

    def play():
        s_d = win.getKey()
  
        if s_d == "q":
            Key.setFill("Peachpuff")
            winsound.PlaySound("C",winsound.SND_FILENAME)
            Key.setFill("white")
        elif s_d == "a":
            Acc_k.setFill("Grey")
            winsound.PlaySound("C#",winsound.SND_FILENAME)
            Acc_k.setFill("Black")
        elif s_d == "w":
            a.setFill("Blue")
            winsound.PlaySound("D",winsound.SND_FILENAME)
            a.setFill("white")
        elif s_d == "s":
            winsound.PlaySound("D#",winsound.SND_FILENAME)
        elif s_d == "e":
            winsound.PlaySound("E",winsound.SND_FILENAME)
        elif s_d == "r":
            winsound.PlaySound("F",winsound.SND_FILENAME)
        elif s_d == "f":
            winsound.PlaySound("F#",winsound.SND_FILENAME)
        elif s_d == "t":
            winsound.PlaySound("G",winsound.SND_FILENAME)
        elif s_d == "g":
            winsound.PlaySound("G#",winsound.SND_FILENAME)
        elif s_d == "y":
            winsound.PlaySound("A",winsound.SND_FILENAME)
        elif s_d == "h":
            winsound.PlaySound("B",winsound.SND_FILENAME)

    
    for star in range(100):
        play()
        
            

            
        
        
main()



