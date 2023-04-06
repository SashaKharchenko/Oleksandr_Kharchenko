class Text:
    def __init__(self, content=None, lang=None):
        self.content=content
        self.lang=lang

    def input(self):
        self.content=input("content=")
        self.lang=input("language=")

    def output(self):
        print(self.content)

class Font:
    def __init__(self, name=None, kegel=False,
                 semibold=False, italic=False, underline=False):
        self.name=name
        self.kegel=kegel
        self.semibold=semibold
        self.italic=italic
        self.underline=underline

    def input(self):
        self.name=input("name=")
        self.kegel=bool(input("kegel="))
        self.semibold=bool(input("semi-bold="))
        self.italic=bool(input("italic="))
        self.underline=bool(input("underline="))

    def output(self):
        s=self.name
        if self.kegel:
            s+=", kegel"
        if self.semibold:
            s+=", semi-bold"
        if self.italic:
            s+=", italic"
        if self.underline:
            s+=", underline"
        print(s)

class Textin(Text, Font):
    def __init__(self,colour=None,content=None, lang=None, name=None, kegel=False,
                 semibold=False, italic=False, underline=False):
        self.colour=colour
        Text.__init__(self, content, lang)
        Font.__init__(self, name, kegel, semibold, italic, underline)

    def input(self):
        self.colour=input("colour=")
        Text.input(self)
        Font.input(self)
        
    def output(self):
        print(self.colour)
        Font.output(self)
        Text.output(self)
if __name__=="__main__":
    f=open("file185.txt")
    lines=f.readlines()
    f.close()
    texts=[]
    fonts=[]
    textins=[]
    for i,line in enumerate(lines):
        lang=input(f"lang{i+1}=")
        texts.append(Text(line,lang))
        font=Font()
        font.input()
        fonts.append(font)
        colour=input(f"colour{i+1}=")
        textins.append(Textin(colour, texts[i].content, texts[i].lang,
                              fonts[i].name, fonts[i].kegel, fonts[i].semibold, fonts[i].italic,
                              fonts[i].underline))
    for t in textins:
        t.output()
        
        
