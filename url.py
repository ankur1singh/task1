import mysql.connector as c
import requests
import time
con=c.connect(host="localhost",user="sammy",password="password",database="db_name")

response = requests.get('https://status.digitalocean.com/api/v2/summary.json')

cursor=con.cursor()


query="INSERT INTO url_detail (url,status_code,responce_time) values (%s,%s,%s)"
t=(response.url,response.status_code,response.elapsed.total_seconds())
cursor.execute(query,t)
con.commit()
print('add sussessfully')

