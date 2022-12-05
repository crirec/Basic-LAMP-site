#!/bin/python3
import pymysql as sql
import cgi

class navBar:
    def __init__(self):
        self.items = ["Home", "Projects", "Contact","Blog"]
        self.links = ["index.py","projects.py","contact.py","blog.py"]
    def display(self):
        print("<nav id='navbar'>")
        print("<ul id='navbar_list'>")
        for i in range(len(self.items)):
            try:
                link = self.links[i]
            except:
                link = "/"
            print("<li><a href='"+ link +"' class='navbar_link'>"+self.items[i]+"</a></li>")
        print("</ul>")
        print("</nav>")

class header:
    def __init__(self):
        self.nav = navBar()
    def display(self):
        print("<div class='header'>")
        self.nav.display()
        print("</div>")

def beginParagraph():
    print("<div class='paragraph'>")
    print("<p>")

def endParagraph():
    print("</p>")
    print("</div>")
    
def showNamedDiv(name):
    print("<div id='"+name+"'></div>")
def showClassedDiv(name):
    print("<div class='"+name+"'></div>")
def startNamedDiv(name):
    print("<div id='"+name+"'>")
def startClassedDiv(name):
    print("<div class='"+name+"'>")
def showImg(name):
    print("<img src='"+name+"'>")
    
def endDiv():
    print("</div>")

def beginMainBlock():
    print("<div id='mainBlock'>")

def endMainBlock():
    endDiv()

def startHTML():
    print("Content-Type: text/html\n")
    print("<html lang='en'>")

def endHTML():
    print("</html>")

def startBody():
    print("<body>")

def endBody():
    print("</body>")

def sendHTMLheader(title):
    print("<head>")
    print("<meta charset='UTF-8'/>")
    print("<meta name='viewport' content='width=device-width,initial-scale=1.0'/>")
    print("<title>"+title+"</title>")
    print("<link rel='stylesheet' href='/styles.css'/>")
    print("<script src='/main.js'></script>")
    print("</head>")

def sendFileContents(filepath):
    file = []
    try:
        file = open(filepath, "r") 
    except:
        print("File " + filepath + " could not be opened or does not exist.")
    else:
        contents = file.read()
        contents = contents.replace("\n","<br>")
        print(contents)
    
def SQLquery(cursor, connection, query):
    cursor.execute(query)
    connection.commit()
    out = None
    try:
        out = cursor.fetchall()
    except:
        return ''
    else:
        return out

def SQLconnect(database):
    connection = sql.connect(
        db=database,
        user='user',
        passwd='',
        host='localhost'
    )
    cursor = connection.cursor() #cursors act as query handlers in pymysql
    return connection, cursor

def sanitize(name):
    #sanitization. every special character other than . - or _ so that filenames are excluded 
    removed_characters=['/','\\','#','*',':','(',')','&','^','%','$','@','!',',','+','=','|',']','[','?','`','~',';','<','>','\'','\"']
    newName = name
    for c in removed_characters:
        newName = newName.replace(c,'')
    return newName[:255]

def getPostName():
    post = cgi.FieldStorage().getvalue('post')
    if post is None:
        return ''
    return sanitize(post)

def showPost(sourcedir, name):
    sendFileContents(sourcedir+'/'+name+".txt")