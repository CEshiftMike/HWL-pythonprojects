class morie():
    def __init__(self):
        # print("Smart, Very eager to impress")
        pass
    def alias(self):
        # print("Steve Jobs")
        return "Steve Jobs"
    def assessment(self):
        return "Smart, Very eager to impress"

class popoy():
    def __init__(self):
        # print("Smart, Mature and patient")
        pass
    def alias(self):
        # print("wowowee")
        return "wowowee"
    def assessment(self):
        return "Smart, Mature and patient"


# for subord in [morie(),popoy()]:
#     # print(type(subord))
#     print(subord.alias())
#     print(subord.assessment())

def sub_speak(subord):
    print(subord.assessment())

sub_speak(morie())