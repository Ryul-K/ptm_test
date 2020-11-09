from flask import Flask, request, jsonify
from pyprnt import prnt
import json



app = Flask(__name__)

seller_scenario = {
    "low SoC lv" : 30,
    "high SoC lv" : 55
}
buyer_scenario = {
    "low SoC lv" : 60,
    "high SoC lv" : 80
}
normal_secnario = {
    "low SoC lv" : 30,
    "high SoC lv" : 60
}
success = {
    "state" : "success"
}
@app.route('/scenario', methods = ['POST'])
def startMsg():
    with open("./config.json") as f1:
        config_set_json_1 = json.loads(f1.read())
    prnt(config_set_json_1)
    with open("../MG2/config.json") as f2:
        config_set_json_2 = json.loads(f2.read())
    prnt(config_set_json_2)
    with open("../MG3/config.json") as f3:
        config_set_json_3 = json.loads(f3.read())
    prnt(config_set_json_3)

    try:
        user = request.get_json()#json 데이터를 받아옴
        prnt(user)

        if user["scenario"] == 1 : #MG1: 판매, MG2: 구매, MG3: 노말
            print("MG1 : seller, MG2 : buyer, MG3 : normal")
            config_set_json_1["low SoC lv"] = seller_scenario["low SoC lv"]
            config_set_json_1["high SoC lv"] = seller_scenario["high SoC lv"]
            with open("./config.json", 'w') as f1:
                json.dump(config_set_json_1, f1, indent=4)

            config_set_json_2["low SoC lv"] = buyer_scenario["low SoC lv"]
            config_set_json_2["high SoC lv"] = buyer_scenario["high SoC lv"]
            with open("../MG2/config.json", 'w') as f2:
                json.dump(config_set_json_2, f2, indent=4)

            config_set_json_3["low SoC lv"] = normal_secnario["low SoC lv"]
            config_set_json_3["high SoC lv"] = normal_secnario["high SoC lv"]
            with open("../MG3/config.json", 'w') as f3:
                json.dump(config_set_json_3, f3, indent=4)

            return jsonify(success)

        elif user["scenario"] == 2 : #MG1: 구매, MG2: 판매, MG3: 구 매
            print("MG1 : buyer, MG2 : seller, MG3 : buyer")
            config_set_json_1["low SoC lv"] = buyer_scenario["low SoC lv"]
            config_set_json_1["high SoC lv"] = buyer_scenario["high SoC lv"]
            with open("./config.json", 'w') as f1:
                json.dump(config_set_json_1, f1, indent=4)

            config_set_json_2["low SoC lv"] = seller_scenario["low SoC lv"]
            config_set_json_2["high SoC lv"] = seller_scenario["high SoC lv"]
            with open("../MG2/config.json", 'w') as f2:
                json.dump(config_set_json_2, f2, indent=4)

            config_set_json_3["low SoC lv"] = buyer_scenario["low SoC lv"]
            config_set_json_3["high SoC lv"] = buyer_scenario["high SoC lv"]
            with open("../MG3/config.json", 'w') as f3:
                json.dump(config_set_json_3, f3, indent=4)

            return jsonify(success)

        elif user["scenario"] == 3 : #MG1: 판매, MG2: 구매, MG3: 판매
            print("MG1 : seller, MG2 : buyer, MG3 : seller")
            config_set_json_1["low SoC lv"] = seller_scenario["low SoC lv"]
            config_set_json_1["high SoC lv"] = seller_scenario["high SoC lv"]
            with open("./config.json", 'w') as f1:
                json.dump(config_set_json_1, f1, indent=4)

            config_set_json_2["low SoC lv"] = buyer_scenario["low SoC lv"]
            config_set_json_2["high SoC lv"] = buyer_scenario["high SoC lv"]
            with open("../MG2/config.json", 'w') as f2:
                json.dump(config_set_json_2, f2, indent=4)

            config_set_json_3["low SoC lv"] = seller_scenario["low SoC lv"]
            config_set_json_3["high SoC lv"] = seller_scenario["high SoC lv"]
            with open("../MG3/config.json", 'w') as f3:
                json.dump(config_set_json_3, f3, indent=4)

            return jsonify(success)

        elif user["scenario"] == 4 : #MG1: 판매, MG2: 노말, MG3: 노3
            print("MG1 : seller, MG2 : normal, MG3 : normal")
            config_set_json_1["low SoC lv"] = seller_scenario["low SoC lv"]
            config_set_json_1["high SoC lv"] = seller_scenario["high SoC lv"]
            with open("./config.json", 'w') as f1:
                json.dump(config_set_json_1, f1, indent=4)

            config_set_json_2["low SoC lv"] = normal_secnario["low SoC lv"]
            config_set_json_2["high SoC lv"] = normal_secnario["high SoC lv"]
            with open("../MG2/config.json", 'w') as f2:
                json.dump(config_set_json_2, f2, indent=4)

            config_set_json_3["low SoC lv"] = normal_secnario["low SoC lv"]
            config_set_json_3["high SoC lv"] = normal_secnario["high SoC lv"]
            with open("../MG3/config.json", 'w') as f3:
                json.dump(config_set_json_3, f3, indent=4)

            return jsonify(success)


        # elif user["scenario"] == 2 : #MG1 :
        #     config_set_json["low SoC lv"] = seller_scenario["low SoC lv"]
        #     config_set_json["high SoC lv"] = seller_scenario["high SoC lv"]
        #     with open("config.json", 'w') as f:
        #         json.dump(config_set_json, f, indent=4)
        # elif user["scenario"] == 3 :
        #
        # elif user["scenario"] == 4 :
        #
        #     with open("ems_st_msg.json", 'w') as ems_st_msg:
        #         json.dump(user, ems_st_msg, indent=4)
        #     return jsonify(IF_TR_startMsg)


    except:
        pass
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
