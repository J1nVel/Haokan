import json
from flask import Flask
from Haokan import Haokan

#client = MongoClient("127.0.0.1",27017)
#db = client['haokan']
#collection = db['shipin']

app=Flask(__name__)
haokan=Haokan()
@app.route('/flush')
def flush():
    return json.dumps(haokan.flush_parse())
#    r = collection.find()
#    y = {}
#    idd = 0
#    for i in r:
#        
#        if i == '':
#            break
#        else:
#            idd = idd+1
#            idr = str(idd)
#            y[idr] = i
#    return str(y).replace("\'","\"").replace('ObjectId(','').replace(')','')
@app.route('/comment_and_video')
def comment_and_video():
    return json.dumps(haokan.comment_and_videoinfo())
@app.route('/userinfo')
def userinfo():
    return json.dumps(haokan.userinfo())

app.run(host='localhost',port=5000)





