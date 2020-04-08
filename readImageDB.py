#DOCS: http://zetcode.com/db/mysqlpython/
import sys, getopt
sys.path.append("/home/pi/.local/lib/python3.7/site-packages/pymysql")
import pymysql
import return_pass
import os
import env
import base64
ENC_KEY = os.getenv('ENC_KEY')
DB_PASS = os.getenv('DB_PASS')
WRITE_DIR = '/var/www/html/ThesisMobileApp/temp_img'
def ReadImage(img_date):
    #print(img_date)
    con = pymysql.connect('localhost', 'root', DB_PASS, 'security')
    with con:    
        cur = con.cursor() 
        cur.execute("SELECT AES_DECRYPT(unhex(image),'" + ENC_KEY + "') AS decImg from images WHERE date = %s", 
            (img_date))
        rows = cur.fetchall()
        for row in rows:
            print(str(row[0]))
            imgdata = base64.b64decode(str(row[0]))#this is the decided b64 img
            with open(img_date, 'wb') as f:
                f.write(os.path.join(WRITE_DIR,imgdata, ".png"))
                print(os.path.join(WRITE_DIR,imgdata, ".png"))
            
             
        cur.close()

if __name__== "__main__":
    ReadImage(str(sys.argv[1]))