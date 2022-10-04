import ibm_db

hostname="125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
uid = "vcr98026"
pwd="ISbDxBtU9PYm8KU6"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="30426"
protocol="TCPIP"
cert="Certificate.crt"
dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
).format(db,hostname,port,uid,cert,pwd)

print(dsn)

try: 
    print("Trying to connect")
  #  db2=ibm_db.connect(dsn,",")
    conn = ibm_db.connect(dsn,"","")     
    print("connected to database")
except:
    print("no connection:", ibm_db.conn_errormsg())