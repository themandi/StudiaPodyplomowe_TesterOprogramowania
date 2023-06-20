class CatParent():
    def voice(self):
        print("Jestem rodzicem")
class CatKid(CatParent):
    pass
parent = CatParent()
kid = CatKid()

print(kid.voice())