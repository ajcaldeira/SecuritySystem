#DOCS: http://zetcode.com/db/mysqlpython/
import pymysql
import return_pass
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