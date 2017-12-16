class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width  = width
        self.height = height
        self.update()

    def origin(self):
        return (self.relativeWidth // 2, self.relativeHeight // 2)

    def update(self):
        self.relativeWidth  = self.x + self.width
        self.relativeHeight = self.y + self.height

    def relativeSize(self):
        return (self.relativeWidth, self.relativeHeight)

    def getX(self):
        return self.x

    def setX(self, xCoord):
        self.x = xCoord
        self.update()

    def getY(self):
        return self.y

    def setY(self, yCoord):
        self.y = yCoord
        self.update()

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width
        self.update()

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height
        self.update()

