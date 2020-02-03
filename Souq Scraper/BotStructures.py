class Item:
    offer = 0
    price = 0
    desc ="NO Desc"
    link = "No Link"
    img  = "NO img"
    def feltring(self,items):
        res = []
        visited = []
        i = Item
        for i in items:
           if not i.desc in visited:
               res.append(i)
               visited.append(i.desc)
        return res          

class Handler:
    def getPages(self,RootURL):
        section = "?section="
        page = "&page="
        cat_sections = []
        for i in range(1 , 100):
            cat_sections.append(RootURL+section+"1"+page+str(i))
            cat_sections.append(RootURL+section+"2"+page+str(i))
        return cat_sections        