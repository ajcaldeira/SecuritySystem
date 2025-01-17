#DOCS: http://zetcode.com/db/mysqlpython/
import sys
sys.path.append("/home/pi/.local/lib/python3.7/site-packages/pymysql")
import pymysql
import os
import env
ENC_KEY = os.getenv('ENC_KEY')
DB_PASS = os.getenv('DB_PASS')
def WriteImage(img_data,date):
    con = pymysql.connect('localhost', 'root', DB_PASS, 'security')
    with con:    
        cur = con.cursor() 
        cur.execute("INSERT INTO images (image, date) VALUES (HEX(AES_ENCRYPT(%s,'" + ENC_KEY + "')),%s)", 
            (img_data, date))
        con.commit()
        cur.close()
    print(date) #output img name for next part (reading)
