#!/bin/python3
import pymysql
import cgitb
import assets.functions as f

def main():
	cgitb.enable()
	
	f.startHTML()

	f.sendHTMLheader("Title")

	f.startBody()

	f.header().display()

	f.beginMainBlock()

	#put website here

	f.endMainBlock()

	f.endBody()

	f.endHTML()

main()