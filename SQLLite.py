import time
import sqlite3

# Prerequisite setup
#   Go to SQLite download page, and download precompiled binaries from Windows section.
#   You will need to download sqlite-shell-win32-*.zip and sqlite-dll-win32-*.zip zipped files.
#   Create a folder C:\>sqlite and unzip above two zipped files in this folder which will give you sqlite3.def, sqlite3.dll and sqlite3.exe files.
#   Add C:\>sqlite in your PATH environment variable and finally go to the command prompt and issue sqlite3 command which should display a result something as below.
#       set PATH=%PATH%;C:\xampp\php

# Connect to database and set variables.
conn = sqlite3.connect('C:/Users/Conor.OBrien/jobs.sqlite')
cur = conn.cursor()
date = time.strftime("%c")
Source = 'ie.indeed.com'


company = "Mint Sauce"
title = "Test Title"
location = "Somewhere over the rainbow"
source = "SQL"
description = "Test Description"

#cur.execute('''INSERT INTO jobs ("unique_id", "title", description, company, date_added, location, link, source) VALUES ( ?, ? , ? , ?, ?, ?, ?, ?)''', (SQL_ID, SQL_Title, SQL_Desc, SQL_Comp, SQL_Date, SQL_Loca, SQL_Desc, SQL_Source ) )
cur.execute(
'''INSERT INTO jobs ("unique_id", "title", "description", "company", "date_added", "location", "link", "source")
VALUES ( ?, ? , ? , ?, ?, ?, ?, ?)''', ("teawd", title, description, company, date, location, source ) )
conn.commit();

    
