from graphics import*
from noise import pnoise2
import numpy as np

class Terrain():
    def __init__ (self, win:GraphWin):
        self.win = win
        self.width = win.getWidth()
        self.heigth = win.getHeight()
        self.generate()

    def draw(self, win:GraphWin):
        self.drawnT = []
        for i in range(len(self.t)-1):
            p = Point(i, self.t[i])
            p2 = Point(i+1, self.t[i+1])
            line = Line(p, p2)
            line.setOutline("Green")
            line.draw(win)
            self.drawnT.append(line)

    def undraw(self):
        for l in self.drawnT:
            l.undraw()
            
    def getInternalPoints(self):
        self.generateInternalPoints()
        return self.internalPoints

    def generateInternalPoints(self):
        self.internalPoints = []
        for x in range(self.width):
            for y in range(self.heigth):
                if y > self.t[x]:
                    self.internalPoints.append((x,y))

    def average(self, t):
        points = t.getPoints()
        if len(points) != len(self.t):
            return []

        arr2 = []
        for i in range(len(points)):
            y = (points[i]+self.t[i])/2
            arr2.append(y)

        self.t = arr2

    def generate(self):
        self.perlin_array((self.heigth, self.width))
        self.t = self.t[0:self.width]

        tempArr = []
        for v in self.t:
            tempArr.append(v*(self.heigth/3)+(self.heigth*2/3))
        self.t = tempArr

    def getPoints(self):
        return self.t

    def perlin_array(self, shape = (200, 200),
			scale=100, octaves = 1, 
			persistence = 0.5, 
			lacunarity = 2.0, 
			seed = None): #Open source from https://engineeredjoy.com/blog/perlin-noise/

        if not seed:
            seed = np.random.randint(0, 100)

        arr = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                arr[i][j] = pnoise2(i / scale,
                                            j / scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=1024,
                                            repeaty=1024,
                                            base=seed)
        max_arr = np.max(arr)
        min_arr = np.min(arr)
        norm_me = lambda x: (x-min_arr)/(max_arr - min_arr)
        norm_me = np.vectorize(norm_me)
        arr = norm_me(arr)

        arr2 = []
        for v in arr:
            arr2.append(v[0])
        self.t = arr2