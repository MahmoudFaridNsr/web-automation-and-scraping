class Category:
    link = "No link"
    table= "No table" 
class MYSQLConnectionType:
    host = ""
    db =""
    user = ""
    password = ""    

class MySQLFile:
    # print("Sammy the {} has a pet {}!".format("shark", "pilot fish"))
    def getValues(self):
        try:
            fp = open('./Configs/sql.txt', 'r')
            lines = fp.readlines()
            print(" SqL Config Loaded.....")
        finally:
            fp.close()
            hostt = lines[0].split('=')[1]
            dbb = lines[1].split('=')[1] 
            userr = lines[0].split('=')[1]
            passwordd = lines[1].split('=')[1] 
        values = MYSQLConnectionType() 
        values.host  =hostt
        values.db = dbb
        values.user = userr
        values.password = passwordd
        return values   

class Config:
    
    def readCategories(self):
        categories =[]
        try:
            fp = open('./Configs/Config.txt', 'r')
            lines = fp.readlines()
            print(str(len(lines))+ " Category Loaded.....")
        finally:
            fp.close()
           
        for line in lines:
            x = Category()
            var = line.split('|')
            x.link,x.table= var[0],var[1]
            categories.append(x) 
        return categories