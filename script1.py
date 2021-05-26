import pandas as pd
import pymysql

read_tsv = pd.read_csv("medicene.tsv", delimiter="\t")
pd.options.display.max_columns = len(read_tsv.columns)

connection = pymysql.connect(host="localhost",user="root",passwd="",database="test" )

cursor = connection.cursor()
# Query for creating table


ArtistTableSql = """CREATE TABLE Medicine(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
Regno VARCHAR(100),
Brand TEXT(200),
Ingrediants TEXT(200),
Dosage_Form TEXT(20),
Packing VARCHAR(6),
Trade_Price FLOAT(40),
Retail_Price FLOAT(40)
)"""
cursor.execute(ArtistTableSql)

# Query for inserting rows
for i in range(0,len(read_tsv)):
    insert_query="INSERT INTO Medicine(Regno,Brand,Ingrediants,Dosage_Form,Packing,Trade_Price,Retail_Price) \
         VALUES (\"%s\", \"%s\",\"%s\",\"%s\",\"%s\",%f,%f )" % \
         (read_tsv.iloc[i,0],read_tsv.iloc[i,1],read_tsv.iloc[i,2],read_tsv.iloc[i,3],read_tsv.iloc[i,4],read_tsv.iloc[i,5],read_tsv.iloc[i,6])
    #print(insert_query)
    cursor.execute(insert_query)                                                                                         

connection.commit()    
connection.close()