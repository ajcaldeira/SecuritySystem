#DOCS: http://zetcode.com/db/mysqlpython/
import pymysql
import return_pass
def WriteImage(img_data,date):
    con = pymysql.connect('localhost', 'root', return_pass.GetPass(), 'security')
    with con:    
        cur = con.cursor() 
        cur.execute("INSERT INTO images (image, date) VALUES (HEX(AES_ENCRYPT(%s,'IlvdPuXqiNUa1ONh1V7HOAr1pRBbI7rh')),%s)", 
            (img_data, date))    
        con.commit()
        con.close()
        print("Number of rows updated:",  cur.rowcount)