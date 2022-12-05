#!/bin/python3
import pymysql
import cgi
import cgitb
import assets.functions as f

def showProjectPost():
    imgName = f.getPostName()
    f.startClassedDiv("project_img")
    f.showImg("/proj_img/"+imgName+".png")
    f.endDiv()
    f.showPost("projects", imgName)

#for reference,
#item[0] -> post_id, int
#item[1] -> post_title, string
#item[2] -> post_filepath, string
#item[3] -> post_previewimagepath, string
def showProjectPreview(item):
    f.startClassedDiv("project_img")
    f.showImg("/proj_img/"+item[3])
    f.endDiv()
    f.showClassedDiv("spacer")
    print("<li class='blogreel_item'>")
    print("<a class='blogreel_link' href='/projects.py?post="+item[2].replace(".txt","")+"'>"+item[1]+"</a>")
    file = open("projects/"+item[2], 'r')
    firstLines = '';
    for i in range(3):
        firstLines += file.readline()
    firstLines = firstLines.replace("\n", " ")
    firstLines = firstLines[:200] + '...' if len(firstLines) > 200 else firstLines
    print("<a class='blogreel_preview' href='/projects.py?post="+item[2].replace(".txt",""+"")+"'>")
    print(firstLines)
    print("</a>")
    f.showClassedDiv("blogreel_stopcap")  
    print("</li>")
    f.showClassedDiv("spacer")

def showProjectReel():
    output = None
    connection = None
    cursor = None
    try:
        connection, cursor = f.SQLconnect("projects")
    except Exception as e:
        f.beginParagraph()
        print("Failed to access projects database:")
        print(e)
        f.endParagraph()
        return
    output = f.SQLquery(cursor, connection, "SELECT * FROM posts ORDER BY post_id DESC")
    f.startNamedDiv("blogreel")
    if output is None or len(output) == 0:
        print("No posts here yet!")
    else:
        print("<ol id='blogreel_list'>")
        for item in output:
            showProjectPreview(item)
        print("</ol>")

    f.endDiv()

def main():
    pass

if __name__ == "__main__":
    
    cgitb.enable()
    
    f.startHTML()

    f.sendHTMLheader("Projects")

    f.startBody()

    f.header().display()

    f.beginMainBlock()

    #check if there's "?post=" in the url
    postRequested = f.getPostName()

    if postRequested is '':
        showProjectReel()
    else:
        showProjectPost()

    f.endMainBlock()

    f.endBody()

    f.endHTML()
    
    main()
