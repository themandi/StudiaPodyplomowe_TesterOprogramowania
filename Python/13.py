class CatParent():
    def voice(s):
        print("Jestem rodzicem")
class CatKid(CatParent):
    def voice(self):
        print("Jestem dzieckiem")

parent = CatParent()
kid = CatKid()

parent.voice()
kid.voice()