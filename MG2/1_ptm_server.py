from flask import Flask, request, jsonify
from pyprnt import prnt
import json

app = Flask(__name__)

IF_TR_startMsg = {
        "type" : "RES",
        "interface" : "IF.TR.startMsg",
        "parameter" : "",
        "state" : "success"
        }

IF_TR_startMsg_error = {
        "type" : "RES",
        "interface" : "IF.TR.startMsg",
        "parameter" : "",
        "state" : "error"
        }

IF_TR_endMsg = {
        "type" : "RES",
        "interface" : "IF.TR.endMsg",
        "parameter" : "",
        "state" : "success"
        }

IF_TR_endMsg_error = {
        "type" : "RES",
        "interface" : "IF.TR.endMsg",
        "parameter" : "",
        "state" : "error"
        }


@app.route('/b_tr_startMsg', methods = ['POST'])
def startMsg():
    try:
        user = request.get_json()#json 데이터를 받아옴
        prnt(user)
        if user["parameter"]["cm_type"] == "start":
            with open("ems_st_msg.json", 'w') as ems_st_msg:
                json.dump(user, ems_st_msg, indent=4)
            return jsonify(IF_TR_startMsg)
        else :
            return jsonify(IF_TR_startMsg_error)

    except:
        return jsonify(IF_TR_startMsg_error)
    #     f.append(user[""])
    # if user['parameter']['id'] != '' and user['request_time'] != '' and user['parameter']['cm_type'] == 'start' :
        # return jsonify(IF_TR_startMsg)# 받아온 데이터를 다시 전송


@app.route('/b_tr_endMsg', methods = ['POST'])
def endMsg():
    try:
        user = request.get_json()#json 데이터를 받아옴
        prnt(user)
        if user["parameter"]["cm_type"] == "end":
            with open("ems_ed_msg.json", 'w') as ems_ed_msg:
                json.dump(user, ems_ed_msg, indent=4)
            return jsonify(IF_TR_endMsg)
        else :
            return jsonify(IF_TR_endMsg_error)

    except:
        return jsonify(IF_TR_endMsg_error)

if __name__ == "__main__":
    with open("config.json") as config_set:
        config_set_json = json.loads(config_set.read())

    port = config_set_json["PTM Server Port"]
    host = config_set_json["PTM host"]
    print("Client Start")

    app.run(host=host,port=port) # host="0.0.0.0", port=8080
