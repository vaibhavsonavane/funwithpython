class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


ListofCoordinates = []
input_stream = [[3, 1], [4, 2], [1, 1], [3, 8], [4, 4]]
while input_stream.__len__() != 0:
    x = 10
    y = 10
    for inp in input_stream:
        if inp.__getitem__(0) <= x:
            if inp.__getitem__(0) == x and inp.__getitem__(1) > y:
                x = inp.__getitem__(0)
            else:
                x = inp.__getitem__(0)
                y = inp.__getitem__(1)
    ListofCoordinates.append(Coordinates(x, y))
    input_stream.remove([x, y])

for coordinate in ListofCoordinates:
    print(f"The sorted is {coordinate.x}:{coordinate.y}")
