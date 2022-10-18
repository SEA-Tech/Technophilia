import pandas as pd
data_xls=pd.read_excel('Blood donation sample data.xlsx','Hospital',na_filter=True)
data_xls=data_xls.values.tolist()
print(data_xls[0])

import psycopg2

connection=psycopg2.connect(user="technophilia",password="technophilia@2022",host="technophilia.postgres.database.azure.com",port=5432,database="astraverse")
cursor=connection.cursor()
qry=('''INSERT INTO pages_hospital(id,name,contact,address,pincode,city,country,description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);''')
for li in data_xls:
    cursor.execute(qry,(li[0],li[1],li[3],li[4],li[5],li[6],'india',li[2]))
connection.commit()
cursor.close()

connection.close()

""" ,op,on,ap,an,bp,bn,abp,abn,image %s,%s,%s,%s,%s,%s,%s,%s,%s ' ',' ',' ',' ',' ',' ',' ',' ',' ' """


    
