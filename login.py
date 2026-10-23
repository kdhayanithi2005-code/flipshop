#!C:\Python312\python.exe
import cgi
import mysql.connector

print("content-text:text\n\r\n\r")
print("<html>")
print("<body>")
mydata=cgi.FieldStorage()

fname=mydata.getvalue("username")
lname=mydata.getvalue("userlname")
mnom=mydata.getvalue("mob")
gmailid=mydata.getvalue("id")
dateob=mydata.getvalue("dob")
ae=mydata.getvalue("ag")
gent=mydata.getvalue("gender")
bldg=mydata.getvalue("bgroup")
panc=mydata.getvalue("panca")
adds=mydata.getvalue("add")
pinc=mydata.getvalue("pin")
dist=mydata.getvalue("dis")

print("<center>")

print("<h1>Flip Shop</h1>")

print("<table>")
print(f"<tr><td><h3>FirstName:</h3></td> <td><h3>{fname}</h3></td></tr>")
print(f"<tr><td><h3>LastName:</h3></td><td><h3>{lname}</h3></td></tr>")
print(f"<tr><td><h3>Mobile No:</h3></td><td><h3>{mnom}</h3></td></tr>")
print(f"<tr><td><h3>Gmail i'd:</h3></td><td><h3>{gmailid}</h3></td></tr>")
print(f"<tr><td><h3>Date Of Birth:</h3></td><td><h3>{dateob}</h3></td></tr>")
print(f"<tr><td><h3>Age:</h3></td><td><h3>{ae}</h3></td></tr>")
print(f"<tr><td><h3>Genter:</h3></td><td><h3>{gent}</td></h3></tr>")
print(f"<tr><td><h3>BloodGroup:</h3></td><td><h3>{bldg}</h3></td></tr>")
print(f"<tr><td><h3>Pancar:</h3></td><td><h3>{panc}</h3></td></tr>")
print(f"<tr><td><h3>Address:</h3></td><td><h3>{adds}</h3></td><tr>")
print(f"<tr><td><h3>Pin Code:</h3></td><td><h3>{pinc}</h3></td><tr>")
print(f"<tr><td><h3>District:</h3></td><td><h3>{dist}</h3></td><tr>")

print("</table>")
print("<a href='./index.html'>Back to home</a>")
print("</center>")

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database2"

)
cursor=db.cursor()
sql="INSERT INTO table1(FIRSTNAME, LASTNAME, MOBILE, GMAIL,BIRTHDATE, AGE, GENTER, BLOODGROUP, PANCARD, ADDRESS, PINCODE, DISTRICT)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(fname,lname,mnom,gmailid,dateob,ae,gent,bldg,panc,adds,pinc,dist)
cursor.execute(sql,val)
db.commit()


print("</body>")
print("</html>")