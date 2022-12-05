Tested on Ubuntu 20.04 + Apache2 2.4.52 + MySQL ver 8.0.31 + Python 3.10.6

This configuration requires a MySQL configuration with databases mirroring the included sql files. To create those databases with the default posts included here, activate the following commands(WILL OVERWRITE DATABASES NAMED "blog" AND "projects"):
1. sudo mysql -u root -p blog < blog.sql
2. sudo mysql -u root -p projects < projects.sql

Things to change on install:
1. assets/functions.py has a function called SQLconnect(), change the username and password variables to reflect your MySQL configuration
2. add real projects by adding a new text file to site/projects/ and an image to site/proj_img before updating your SQL database to reflect it.
3. add real blog posts the same way but without an image and adding the text file to site/blogposts
4. configure base website text inside the .txt files which can be found in /assets/
5. move everything in the directory "site" to your website's home directory
6. change the directories in site/.htaccess to correspond to your website's home directory
7. make python pages executable to make them accessible with "chmod +x FILE.py" replacing file with the file name and path to affect
