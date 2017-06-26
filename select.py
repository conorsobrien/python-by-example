import sqlite3

# Connect to database.
conn = sqlite3.connect('C:/sqlite/sqlite-tools-win32-x86-3160200/sqlite-tools-win32-x86-3160200/jobs')
cur = conn.cursor()
cur.execute('''SELECT source_link FROM jobs where source="jobs.ie"''')
all_rows = cur.fetchall()
test = "https://www.jobs.ie/ApplyForJob.aspx?Id=1589405"
processed_links=[]
for row in all_rows:
    print(type(row))
    print(row[0])
    processed_links.append(row[0])
    
print(processed_links)

if test in processed_links:
    print("Done Already")
else:
    print("Processing")

#cur.execute('SELECT source_link FROM jobs WHERE source="jobs.ie"')
#all_rows = c.fetchall()
#print('2):', all_rows)

conn.close()
