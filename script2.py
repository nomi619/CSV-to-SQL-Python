import pymysql

connection = pymysql.connect(host="localhost",user="root",passwd="",database="test" )
cursor = connection.cursor()

cursor.execute("ALTER TABLE medicine \
  ADD difference float(40)  \
    AFTER Retail_Price;")

cursor.execute("Update medicine \
  set difference=Retail_Price-Trade_Price ")

  
connection.commit()    
connection.close()