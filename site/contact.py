#!/bin/python3
import pymysql
import cgitb
cgitb.enable()
import assets.functions as f

f.startHTML()

f.sendHTMLheader("Contact")

f.startBody()

f.header().display()

f.beginMainBlock()

f.beginParagraph()
f.sendFileContents("assets/contact.txt")
f.endParagraph()

f.endMainBlock()

f.endBody()

f.endHTML()
