class Rupee:

    def __init__(self, clean=True,**kwargs):

        for key,value in kwargs.items():
             setattr(self,key,value)

        self.isClean = clean

        if self.isClean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color
    def clean(self):
        self.color = self.clean_color
    def __del__(self):
        print("Rupee Spent")

class Note(Rupee):
    def __init__(self):
        data = {
            "clean_color" : "brown",
            "rusty_color": "dark brown",
            "value": 10
        }
        super().__init__(**data)


one_rupee_note = Note()

print(one_rupee_note.value)
one_rupee_note.rust()
print(one_rupee_note.color)
one_rupee_note.clean()
print(one_rupee_note.color)
