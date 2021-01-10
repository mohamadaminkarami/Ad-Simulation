class BaseAdvertising:

    def __init__(self, id=0):
        self.__id = id
        self.__clicks = 0
        self.__views = 0

    def describe_me(self):
        return "this ia a Parent Of Ad and Advertiser class that handle methods and fields exist in both"

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    def inc_clicks(self):
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1
