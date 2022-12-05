#!/bin/python3
import pymysql
import cgi
import cgitb
import assets.functions as f

def showBlogPost(name):
    f.showPost("blogposts", name)

#for reference,
#item[0] -> post_id, int
#item[1] -> post_title, string
#item[2] -> post_filepath, string
def showReelItem(item):
    print("<li class='blogreel_item'>")
    print("<a class='blogreel_link' href='/blog.py?post="+item[2].replace(".txt","")+"'>"+item[1]+"</a>")
    file = open("blogposts/"+item[2], 'r')
    firstLines = '';
    for i in range(3):
        firstLines += file.readline()
    firstLines = firstLines.replace("\n", " ")
    firstLines = firstLines[:200] + '...' if len(firstLines) > 200 else firstLines
    print("<a class='blogreel_preview' href='/blog.py?post="+item[2].replace(".txt",""+"")+"'>")
    print(firstLines)
    print("</a>")
    f.showClassedDiv("blogreel_stopcap")  
    print("</li>")
    f.showClassedDiv("spacer")

def showBlogReel(count):
    output = None
    connection = None
    cursor = None
    try:
        connection, cursor = f.SQLconnect("blog")
    except Exception as e:
        f.beginParagraph()
        print("Failed to access blog database:")
        print(e)
        f.endParagraph()
        return
    output = f.SQLquery(cursor, connection, "SELECT * FROM posts ORDER BY post_id DESC")
    f.startNamedDiv("blogreel")
    if output is None or len(output) == 0:
        print("No posts here yet!")
    else:
        f.showClassedDiv("spacer")
        print("<ol id='blogreel_list'>")
        if count == 0:
            for item in output:
                showReelItem(item)
        else:
            try:
                for i in range(3):
                    showReelItem(output[i])
            except:
                print("</ol>")
                f.beginParagraph()
                print("No more posts to show!")
                f.endParagraph()
                f.endDiv()
                return

            print("</ol>")
            f.beginParagraph()
            print("More on the blog!")
            f.endParagraph()
            f.endDiv()
            return

        print("</ol>")

    f.endDiv()

def main():
    pass

if __name__ == "__main__":
    
    cgitb.enable()
    
    f.startHTML()

    f.sendHTMLheader("Blog")

    f.startBody()

    f.header().display()

    f.beginMainBlock()

    postRequested = f.getPostName()

    if postRequested is '':
        showBlogReel(0)
    else:
        showBlogPost(postRequested)

    f.endMainBlock()

    f.endBody()

    f.endHTML()
    
    main()
