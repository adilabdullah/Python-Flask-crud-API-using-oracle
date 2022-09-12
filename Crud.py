from flask import Flask, request,jsonify
from Dao import AllData,specific,create,update,delete,sample
import json

app = Flask(__name__)


@app.route("/name")
def printName():
    #check user details from db
   # return print_name();
	return {"data":print_name()};
	
def print_name():
   return "This is Adil Abdullah";	
   
@app.route("/all",methods=['GET'])   
def all_data():   
   return jsonify(AllData());
   
   
@app.route("/specific/<sno>",methods=['GET'])   
def specific_data(sno):   
   return jsonify(specific(sno));   
   
@app.route("/insert",methods=['POST'])   
def insert_data():
   record = json.loads(request.data)   
   return jsonify(create(record));   

@app.route("/update/<sno>",methods=['PUT'])   
def update_data(sno):
   record = json.loads(request.data)      
   return jsonify(update(record,sno));   

@app.route("/delete/<sno>",methods=['DELETE'])   
def delete_data(sno):   
   return jsonify(delete(sno));      

@app.route("/sample",methods=['POST'])   
def sample_data(): 
   record = json.loads(request.data)
  #message = json.load(data);
   print(record["First_Name"]);
   print(record["Last_Name"]);
   print(record["Email"]);
   print(record["Age"]);
   print(record["Cell"]); 
   return jsonify(record);
  # print(data);  
  # return sample(data); 

if __name__ == '__main__':
    app.run()  # run our Flask app   