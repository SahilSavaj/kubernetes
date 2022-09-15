from flask import Flask,request
import json
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route('/',methods=['GET','POST'])
def start():
    if request.method=='GET':
        try:
            response='200'
            body="The Docker is running and data is sucessfully fetched."
        except:
            response='400'
            body="Error hai."
    elif request.method=='POST':
        response='200'
        body='Post request not available.'
    else:
        response='400'
        body='Invalid Request'
    resp={"response":response,"body":body}
    # print(resp)
    return (resp)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')