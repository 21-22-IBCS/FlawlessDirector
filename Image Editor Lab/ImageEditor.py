from graphics import*
from Button import*

def brighten(cats):
    for i in range(0,cats.getWidth()):
        for j in range(0,cats.getHeight()):
            getP = cats.getPixel(i,j)
            r,g,b = getP[0] + 10, getP[1] + 10, getP[2] + 10
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255

            cats.setPixel(i,j, color_rgb(r,g,b))
            
def darken(cats):
    for i in range(0,cats.getWidth()):
        for j in range(0,cats.getHeight()):
            getP = cats.getPixel(i,j)
            r,g,b = getP[0] - 10, getP[1] - 10, getP[2] - 10
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0

            cats.setPixel(i,j, color_rgb(r,g,b))
            
def blurr(cats):
    for i in range(0,cats.getWidth()-1):
        for j in range(0,cats.getHeight()-1):
                
            r = int((cats.getPixel(i,j)[0]+cats.getPixel(i-1,j)[0]+cats.getPixel(i+1,j)[0]+cats.getPixel(i,j-1)[0]+cats.getPixel(i,j+1)[0])/5)
            g = int((cats.getPixel(i,j)[1]+cats.getPixel(i-1,j)[1]+cats.getPixel(i+1,j)[1]+cats.getPixel(i,j-1)[1]+cats.getPixel(i,j+1)[1])/5)
            b = int((cats.getPixel(i,j)[2]+cats.getPixel(i-1,j)[2]+cats.getPixel(i+1,j)[2]+cats.getPixel(i,j-1)[2]+cats.getPixel(i,j+1)[2])/5)
            cats.setPixel(i,j, color_rgb(r,g,b))
def contrast(cats):
    for i in range(0,cats.getWidth()):
        for j in range(0,cats.getHeight()):
            getP = cats.getPixel(i,j)
            total = getP[0] + getP[1] + getP[2]
            if (total > (255*3)/2):
                r,g,b = getP[0]+10, getP[1]+10, getP[2]+10
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                cats.setPixel(i,j, color_rgb(r,g,b))
                continue
            if(total < (255*3)/2):
                r,g,b = getP[0]-10, getP[1]-10, getP[2]-10
                if r < 0:
                    r = 0
                if g < 0:
                    g = 0
                if b < 0:
                    b = 0
                cats.setPixel(i,j, color_rgb(r,g,b))
                continue

            cats.setPixel(i,j, color_rgb(r,g,b))
            

            cats.setPixel(i,j, color_rgb(r,g,b))
def specialFilter(cats):
    for i in range(0,cats.getWidth()):
        for j in range(0,cats.getHeight()):
            getP = cats.getPixel(i,j)
            r,g,b = 255-getP[0], 255 - getP[1], 255-getP[2]
            cats.setPixel(i,j, color_rgb(r,g,b))

def spiral(cats):
    x = cats.getWidth()-1
    y = cats.getHeight()-1

    for i in range(cats.getWidth()*cats.getHeight()-1):
        current = cats.getPixel(x,y)
        
        
                

def main():

    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "white", "Show", Point(150, 40), 45)
    hi = Button(win, "white", "Hide", Point(300, 40), 45)
    res = Button(win, "white", "Reset", Point(450, 40), 45)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 150), 45)
    blur = Button(win, "white", "Blur", Point(720, 250), 45)
    cont = Button(win, "white", "Contrast", Point(720, 350), 45)
    filt = Button(win, "white", "Filter", Point(720, 450), 45)
    

    cats = Image(Point(400,300), "Cats.png")
    orig = cats.clone()


    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            print(cats.getWidth()
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if cont.isClicked(m):
            contrast(cats)
        if filt.isClicked(m):
            specialFilter(cats)
        if res.isClicked(m):
            cats = orig.clone()
            cats.undraw()
            cats.draw(win)
        
        
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()
