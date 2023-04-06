from random import randint
class ArtWork:

    def __init__(self,title=None,year=None,author=None,genre=None):
        '''
        self.create(title,year,author,genre)
        '''
        self.title=title
        self.year=year
        self.author=author
        self.genre=genre
        
    '''
    def create(self,title=None,year=None,author=None,genre=None):
        self.title=title
        self.year=year
        self.author=author
        self.genre=genre
    '''
    def input(self):
        self.title=input("title=")
        self.year=input("year=")
        self.author=input("author=")
        self.genre=input("genre=")

    def output(self):
        print(self.title,self.year,self.author,self.genre)

class Technique:

    def __init__(self,name=None,material=None):
        self.name=name
        self.material=material
        '''
        self.create(self,name,material)
        '''
    '''
    def create(self,name=None,material=None):
        self.name=name
        self.material=material
    '''
    def input(self):
        self.name=input("name=")
        self.material=input("material=")

    def output(self):
        print(self.name, self.material)

class Painting(ArtWork, Technique):

    def __init__(self,title=None,year=None,author=None,genre=None,name=None,material=None,width=None,height=None,price=None):
        self.create(title, year, author, genre, name, material, width,height,price)

    def create(self,title=None,year=None,author=None,genre=None,name=None,material=None,width=None,height=None,price=None):
        ArtWork.__init__(self, title,year,author,genre)
        Technique.__init__(self, name ,material)
        self.width=width
        self.height=height
        self.price=price

    def input(self):
        ArtWork.input(self)
        Technique.input(self)
        #self.artwork.input()
        #self.technique.input()
        self.width=input("width=")
        self.height=input("height=")
        self.price=float(input("price="))

    def output(self):
        ArtWork.output(self)
        Technique.output(self)
        print(self.width, self.height,self.price)
        
if __name__=="__main__":
    n=int(input("n="))
    painting_list=[]
    for _ in range(n):
        painting=Painting()
        painting.input()
        painting_list.append(painting)

    for painting in painting_list:
        painting.output()

    m=int(input("m="))
    lst=[]

    for _ in range(m):
        l=input("Учасник=")
        lst.append(l)
        
    price=0
    for painting in painting_list:
        prices={l:randint(1,1000) for l in lst}
        max_price=max(prices.values())
        for k, v in prices.items():
            if max_price==v:
                print(f"Клієнт {k} купив карину {painting.title} за {max_price} грн")
                break
    
