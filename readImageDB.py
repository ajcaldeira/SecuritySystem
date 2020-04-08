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
def ReadImage(img_date):
    print(img_date)
    con = pymysql.connect('localhost', 'root', DB_PASS, 'security')
    with con:    
        cur = con.cursor() 
        cur.execute("SELECT AES_DECRYPT(unhex(image),'" + ENC_KEY + "') AS decImg from images WHERE date = %s", 
            (img_date))
        rows = cur.fetchall()
        for row in rows:
            print("here: {0}".format(row[0]))
        cur.close()
        print("closing")

if __name__== "__main__":
    ReadImage(str(sys.argv[1]))