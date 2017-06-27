class cycle():
    def __init__(self,radius):
        self.__radius=radius
    @property
    def diameter(self):
        return 2*self.__radius
    @diameter.setter
    def diameter(self,diameter):
        self.__radius=diameter/2
    @property
    def radius(self):
        return self.__radius