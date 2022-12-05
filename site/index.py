#!/bin/python3
import pymysql
import cgitb
import assets.functions as f
from blog import showBlogReel

def main():
    cgitb.enable()

    f.startHTML()

    f.sendHTMLheader("Website")

    f.startBody()

    f.header().display()

    f.beginMainBlock()

    f.showImg("index.png")
    print("<br>")
    print("<a class='caption' href='https://www.pexels.com/photo/green-pine-trees-covered-with-fogs-under-white-sky-during-daytime-167699/'>Image courtesy of Lum3n on pexels.com</a>")

    f.beginParagraph()

    print("<br>")

    f.sendFileContents('assets/index.txt')

    f.endParagraph()
    
    print("<br>")
    
    showBlogReel(1) 
    
    f.endMainBlock()

    f.endBody()

    f.endHTML()

if __name__ == "__main__":
    main()
