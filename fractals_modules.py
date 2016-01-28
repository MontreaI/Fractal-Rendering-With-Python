# A simple fractals program adapted from
# Kirby Urner's code found at http://tkinter.unpythonic.net/wiki/FractalImage
# --- modified to provide coordinate positions upon mouse click
# --- modified to allow rendering of either Julia or Mandelbrot

from Tkinter import *
import random

class Julia:
    def __init__(self, n=64, minx = -2, maxx = 1, miny = -1.5, maxy = 1.5):
        self.size = (500,500)
        self.n = n
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.xwidth = self.maxx - self.minx
        self.ywidth = self.maxy - self.miny
        
        self.im = PhotoImage(width=500, height=500)
        self.rgb = []
        self.make_colours()

    def __call__(self,z):
        self.z = z
        self.compute()

    def make_colours(self):
        for i in range(self.n):
            r = i*11%200 + 55
            g = i*5%200 + 55
            b = i*7%200 + 55
            colour = '#%02x%02x%02x' %(r,g,b)
            self.rgb.append(colour)
            
    def compute(self):
        print "Computing %s..." % self.__class__.__name__
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                xp,yp = self.getcoords(x,y)                
                dotcolor = self.fractal(xp,yp)
                self.im.put(dotcolor,to=(x,y))

    def fractal(self,x,y):
        n = self.n
        z = self.z
        o = complex(x,y)
        dotcolor = 0  # default, convergent
        for trials in range(n):
            if abs(o) <= 2.0:
                o = o**2 + z
            else:
                dotcolor = trials
                break  # diverged
        return self.rgb[dotcolor]            

    def getcoords(self,x,y):
        percentx = x/float(self.size[0])
        percenty = y/float(self.size[1])
        xp = self.minx + percentx * (self.xwidth)
        yp = self.maxy - percenty * (self.ywidth)
        return (xp,yp)
    
class Mandelbrot(Julia):
    def fractal(self,x,y):
        n = self.n
        z = complex(x,y)
        o = complex(0,0)
        dotcolor = 0  # default, convergent
        for trials in range(n):
            if abs(o) <= 2.0:
                o = o**2 + z
            else:
                dotcolor = trials
                break  # diverged
        return self.rgb[dotcolor]

def callback(event,l_left,u_right):
    width = u_right[0] - l_left[0]
    height = u_right[1] - l_left[1]
    posx = l_left[0]+width/500*event.x   #image is 500 pixels wide
    posy = u_right[1]-height/500*event.y  #image is 500 pixels high
    print "Clicked at X:", posx, "Y:", posy
    
def renderJulia(n,minx,miny,maxx,maxy):  
    root = Tk()
    f = Julia(n,minx,maxx,miny,maxy)
    f(complex(-0.74543,0.11301))
    f.compute()
    l = Label(root, image=f.im)
    lleft = [minx,miny]
    uright = [maxx,maxy]
    l.bind("<Button-1>", lambda event, l_left=lleft, u_right=uright: callback(event,l_left,u_right))
    l.pack()
    root.title('%s' %(f.__class__.__name__))
    root.mainloop()

def renderMandelbrot(n,minx,miny,maxx,maxy):
    root = Tk()
    f = Mandelbrot(n, minx, maxx, miny, maxy)
    f(complex(-0.74543,0.11301))
    f.compute()
    l = Label(root, image=f.im)
    lleft = [minx,miny]
    uright = [maxx,maxy]
    l.bind("<Button-1>", lambda event, l_left=lleft, u_right=uright: callback(event,l_left,u_right))
    l.pack()
    root.title('%s' %(f.__class__.__name__))
    root.mainloop()
