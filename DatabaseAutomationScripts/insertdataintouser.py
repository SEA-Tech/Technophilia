import pandas as pd
data_xls=pd.read_excel('Blood donation sample data.xlsx','User',na_filter=True)
data_xls=data_xls.values.tolist()
print(data_xls[0])

import psycopg2
from datetime import datetime
dateTimeObj = datetime.now()
connection=psycopg2.connect(user="technophilia",password="technophilia@2022",host="technophilia.postgres.database.azure.com",port=5432,database="astraverse")
cursor=connection.cursor()
qry=('''INSERT INTO pages_donor(id,name,aadhar_no,age,address,blood_group,approved,time_of_donation,hospital_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);''')
for li in data_xls:
    cursor.execute(qry,(li[0],li[1],li[3],li[4],li[5],li[2],False,dateTimeObj,1))
connection.commit()
cursor.close()

connection.close()

""" ,op,on,ap,an,bp,bn,abp,abn,image %s,%s,%s,%s,%s,%s,%s,%s,%s ' ',' ',' ',' ',' ',' ',' ',' ',' ' """


    
