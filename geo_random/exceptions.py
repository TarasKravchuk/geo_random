
class TwoPointsSamePlace(Exception):
    def __init__(self, message= "geometric shape cannot contain 2 points in the same place"):
        print(message)

    #     self.point_1 = point_1
    #     self.point_2 = point_2
    #     self.message = "geometric shape cannot contain 2 points in the same place"
    # def exception_start(self):
    #     if self.point_1 == self.point_2 is True:
    #         raise TwoPointsSamePlace


#TwoPointsSamePlace(point_1, point_2).exception_start()

