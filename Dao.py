import cx_Oracle
import os
#connectString = os.getenv('db_connect') 
con = cx_Oracle.connect('ibm_ace/adil1234@localhost')


def sample(data):
    try:
       
       return {"First_Name":data.fname,"Last_Name":data.lname,
       "Age":data.age,"Email":data.email,"Cell":data.cell};
    except Exception as e:
       return {"ResponseCode":95,"ResponseDesc":str(x)}; 


def create(data):
    try:
       print(data["fname"]);
       cur = con.cursor()
       statement='insert into ibm_ace.person (SNO,F_NAME,L_NAME,EMAIL,CELL,AGE,SALARY) VALUES (:sno,:fname,:lname,:email,:cell,:age,:salary)';

       int(data["sno"]),data["fname"],data["lname"],data["email"],data["cell"],int(data["age"]),float(data["salary"]);
       tuple1 =(int(data["sno"]),data["fname"],data["lname"],data["email"],data["cell"],int(data["age"]),float(data["salary"]));

       cur.execute(statement,data);
       con.commit();
       cur.close()
       return {"ResponseCode":100,"ResponseDesc":"Success"};
    except Exception as e:
       print(e);
       return {"ResponseCode":95,"ResponseDesc":str(e)}; 

def update(data,sno):
    try:
       print(sno);
       print(data["fname"]);
       print(data["lname"]);
       print(data["email"]);
       cur = con.cursor()
       cur.execute('update ibm_ace.person set F_NAME=:1,'+
       'L_NAME=:2,EMAIL=:3,CELL=:4,AGE=:5,SALARY=:6'+
       'where sno=:7',(data["fname"],data["lname"],data["email"],data["cell"],int(data["age"]),float(data["salary"]),sno));
       con.commit();
       cur.close()
       return {"ResponseCode":100,"ResponseDesc":"Success"};
    except Exception as e:
       print(e);
       return {"ResponseCode":95,"ResponseDesc":str(e)}; 

def delete(sno):
    try:
       cur = con.cursor()
       cur.execute('delete from ibm_ace.person where sno=:sno',{'sno':sno});
       con.commit();
       cur.close()
       return {"ResponseCode":100,"ResponseDesc":"Success"};
    except Exception as e:
       return {"ResponseCode":95,"ResponseDesc":str(e)}; 
def AllData():
    try:
       cur = con.cursor()
       statement = 'select * from ibm_ace.person';
       cur.execute(statement)
       res = cur.fetchall()
       cur.close()
       return res;
    except Exception as e:
       return str(e); 


def specific(sno):
    try:
       cur = con.cursor()
       cur.execute('select * from ibm_ace.person where sno=:sno',{'sno':sno});
       res = json.dumps(cur.fetchone())
       cur.close()
       return res;
    except Exception as e:
       return str(e); 