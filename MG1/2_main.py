from socket import *
from iconsdk.wallet.wallet import KeyWallet
import requests, json, os, time, subprocess
from datetime import datetime
from tqdm import tqdm
from pyprnt import prnt

headers = {'Content-Type': 'application/json; charset=utf-8'} #EMS 데이터 타입 # cookies = {'session_id': 'sorryidontcare'}

# response.status_code
# response.text


class buyer_regist_error(Exception):
    pass
class cancel_order(Exception):
    pass
class cancel_offer(Exception):
    pass
class offer_error(Exception):
    pass

def send_ptm_data_to_ems (target_Data) :
    response_json = {}
    with open("config.json") as f:
        tmp_config_json = json.loads(f.read())

    target = tmp_config_json[target_Data]
    ems_url = tmp_config_json["EMS Server URL"] + target['url']
    # print(ems_url)
    if target_Data == "device":
        try:
            target['rq_param_send_time'] = datetime.fromtimestamp(int(str(time.time())[0:10])).strftime('%Y%m%d%H%M%S')
            res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            # print('\n status_code : ' + str(res.status_code))
            print('PTM ==> EMS: ')
            prnt(target)
            time.sleep(1)

            response_json = res.json()
            print('EMS ==> PTM: ')
            prnt(response_json)
            # prnt(response_json)
            # device에 대한 정보 받아와서 보여주
            return response_json #response_json
        except:
            print("Device 기록에 실패했습니다.")
    elif target_Data == "regist" :
        try:
            target['rq_param_parameter'] = eid
            target['rq_param_time'] = datetime.fromtimestamp(int(str(time.time())[0:10])).strftime('%Y%m%d%H%M%S')
            res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            # print('\n status_code : ' + str(res.status_code))
            print('PTM ==> EMS: ')
            prnt(target)
            time.sleep(1)

            response_json = res.json()
            print('EMS ==> PTM: ')
            prnt(response_json)

            # prnt(response_json)
            # device에 대한 정보 받아와서 보여주
            return response_json#response_json
        except:
            print("Device 등록에 실패했습니다.")

    elif target_Data == "params" :
        try:
            res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            # print('\n status_code : ' + str(res.status_code))
            print('PTM ==> EMS: ')
            prnt(target)
            time.sleep(1)

            response_json = res.json()
            print('EMS ==> PTM: ')
            prnt(response_json)
            # prnt(response_json)
            # device에 대한 정보 받아와서 보여주
            return response_json
            # res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            #print('\n status_code : ' + str(res.status_code))
            #prnt(res.json())
            #response_json = res.json()
            # stateOfcharge = stateParams['rs_stateParameter'][0]['stateOfcharge'] 응답 받고 수신값
            # genRatio = stateParams['rs_stateParameter'][0]['genRatio']
            # lossRatio = stateParams['rs_stateParameter'][0]['lossRatio']
            # print('\n SoC : ' + str(stateOfcharge))
            # print('\n genRatio : ' + str(genRatio))
            # print('\n lossRatio : ' + str(lossRatio))
            #return print(target)#response_json
        except:
            print("EMS Data loading에 실패했습니다.")

    elif target_Data == "contractMsg" :
        try:
            print(deal_info_completed["kwh"])
            print(tmp_config_json["tx_electrical_energy"])
            print(type(deal_info_completed["kwh"]))
            print(type(tmp_config_json["tx_electrical_energy"]))
            tmp_ed_time_h = int(deal_info_completed["kwh"]) / tmp_config_json["tx_electrical_energy"]
            print(tmp_ed_time_h)
            tmp_ed_time_sec = tmp_ed_time_h * 3600
            print(tmp_ed_time_sec)
            target['rq_param_parameter']['dep2_rq_param_id'] = deal_info_completed["deal_id"]
            target['rq_param_parameter']['dep2_rq_param_seller'] = deal_info_completed["seller_eid"]
            target['rq_param_parameter']['dep2_rq_param_buyer'] = deal_info_completed["buyer_eid"]
            target['rq_param_parameter']['dep2_rq_param_price'] = deal_info_completed["price"]
            target['rq_param_parameter']['dep2_rq_param_quantity'] = deal_info_completed["kwh"]
            target['rq_param_parameter']['dep2_rq_param_tr_st_time'] = datetime.fromtimestamp(int(deal_info_completed["txTimestamp"][0:10]) + tmp_config_json["start_delay"] - tmp_config_json["safety_delay"]).strftime('%Y%m%d%H%M%S')
            #complete 되고 tmp_config_json["start_delay"] = 300초 만큼 딜레이 후 전력 거래 시#
            target['rq_param_parameter']['dep2_rq_param_tr_ed_time'] = datetime.fromtimestamp(int(deal_info_completed["txTimestamp"][0:10]) - tmp_config_json["safety_delay"] + tmp_ed_time_sec).strftime('%Y%m%d%H%M%S')
            target['rq_param_time'] = datetime.fromtimestamp(int(str(time.time())[0:10])).strftime('%Y%m%d%H%M%S')

            res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            # print('\n status_code : ' + str(res.status_code))
            print('PTM ==> EMS: ')
            prnt(target)
            time.sleep(1)
            
            response_json = res.json()
            print('EMS ==> PTM: ')
            prnt(response_json)
            # device에 대한 정보 받아와서 보여주
            return response_json
            #res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            #print('\n status_code : ' + str(res.status_code))
            #prnt(res.json())
            #response_json = res.json()
            # return print(target)#response_json
        except:
            print("Contract Msg 전송에 실패했습니다.")

IF_ID_onboard = {
    "type": "REQ",
    "interface": "IF.ID.onboard",
    "parameter": "password"
}

# EID management smart contract part
IF_ID_create = {
    "type": "REQ",
    "interface": "IF.ID.create",
    "parameter": ""
}

IF_ID_retrieve = {
    "type": "REQ",
    "interface": "IF.ID.retrieve",
    "parameter": ""
}

IF_ID_document = {
    "type": "REQ",
    "interface": "IF.ID.document",
    "parameter": '{"eid":""}'
}


def id_create():
    print("\nIF_ID_CREATE")
    request_json = IF_ID_create
    print('PTM ==> BI: ' )
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('PTM ==> BI: ')
    prnt(response)

    return response["parameter"]


def id_retrieve():
    # print("\nIF_ID_RETRIEVE")
    request_json = IF_ID_retrieve
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


def id_document(eid):
    print("\nIF_ID_DOCUMENT")
    request_json = IF_ID_document
    parameter_json = {"eid": str(eid)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


# power trade management smart contract part
IF_TR_offer = {
    "type": "REQ",
    "interface": "IF.TR.offer",
    "parameter": '{"quantity":"", "price":""}'
}


def tr_offer(quantity, price):
    print("\nIF_TR_OFFER")
    request_json = IF_TR_offer
    parameter_json = {"quantity": str(price), "price": str(quantity)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response


IF_TR_order = {
    "type": "REQ",
    "interface": "IF.TR.order",
    "parameter": '{"deal": "", "quantity": "", "price": ""}'
}


def tr_order(deal_id, quantity, price):
    print("\nIF_TR_ORDER")
    request_json = IF_TR_order
    parameter_json = {"deal": str(deal_id), "quantity": str(quantity), "price": str(price)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_accept = {
    "type": "REQ",
    "interface": "IF.TR.accept",
    "parameter": '{"deal": "", "order": ""}'
}


def tr_accept(buyer_eid):
    print("\nIF_TR_ACCEPT")
    request_json = IF_TR_accept
    parameter_json = {"order": str(buyer_eid)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_finish = {
    "type": "REQ",
    "interface": "IF.TR.finish",
    "parameter": ""
}


def tr_finish():
    print("\nIF_TR_FINISH")
    request_json = IF_TR_finish
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_cancel_offer = {
    "type": "REQ",
    "interface": "IF.TR.cancel.offer",
    "parameter": ""
}


def tr_cancel_offer():
    print("\nIF_TR_CANCEL_OFFER")
    request_json = IF_TR_cancel_offer
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_cancel_order = {
    "type": "REQ",
    "interface": "IF.TR.cancel.order",
    "parameter": ""
}


def tr_cancel_order():
    print("\nIF_TR_CANCEL_ORDER")
    request_json = IF_TR_cancel_order
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_cancel_accept = {
    "type": "REQ",
    "interface": "IF.TR.cancel.accept",
    "parameter": ""
}


def tr_cancel_accept():
    print("\nIF_TR_CANCEL_ACCEPT")
    request_json = IF_TR_cancel_accept
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_browse_deal = {
    "type": "REQ",
    "interface": "IF.TR.browse.deal",
    "parameter": '{"deal_id": ""}'
}


def tr_browse_deal(deal_id):
    # print("\nIF_TR_BROWSE_DEAL")
    request_json = IF_TR_browse_deal
    parameter_json = {"deal_id": str(deal_id)}
    request_json["parameter"] = json.dumps(parameter_json)
    # print('PTM ==> BI: ')
    # prnt(request_json)
    client.send(request_json)
    response = client.recv()
    # print('BI ==> PTM: ')
    # prnt(response)

    return response["parameter"]


IF_TR_browse_dealIDBuyer = {
    "type": "REQ",
    "interface": "IF.TR.browse.dealIDBuyer",
    "parameter": '{"eid": ""}'
}


def tr_browse_dealIDBuyer(eid):
    print("\nIF_TR_BROWSE_DEALIDBUYER")
    request_json = IF_TR_browse_dealIDBuyer
    parameter_json = {"eid": str(eid)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]



IF_TR_browse_dealIDSeller = {
    "type": "REQ",
    "interface": "IF.TR.browse.dealIDSeller",
    "parameter": '{"eid": ""}'
}




def tr_browse_dealIDSeller(eid):
    print("\nIF_TR_BROWSE_DEALIDSELLER")
    request_json = IF_TR_browse_dealIDSeller
    parameter_json = {"eid": str(eid)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_list_offered = {
    "type": "REQ",
    "interface": "IF.TR.list.offered",
    "parameter": ""
}


def tr_list_offered():
    print("\nIF_TR_LIST_OFFERED")
    request_json = IF_TR_list_offered
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_list_ordered = {
    "type": "REQ",
    "interface": "IF.TR.list.ordered",
    "parameter": '{"deal_id": ""}'
}


def tr_list_ordered(deal_id):
    print("\nIF_TR_LIST_ORDERED")
    request_json = IF_TR_list_ordered
    parameter_json = {"deal_id": str(deal_id)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_list_accepted = {
    "type": "REQ",
    "interface": "IF.TR.list.accepted",
    "parameter": ""
}


def tr_list_accepted():
    print("\nIF_TR_LIST_ACCEPTED")
    request_json = IF_TR_list_accepted
    # print('PTM ==> BI: ')
    # prnt(request_json)
    client.send(request_json)
    response = client.recv()
    # print('BI ==> PTM: ')
    # prnt(response)

    return response["parameter"]


IF_TR_list_finished = {
    "type": "REQ",
    "interface": "IF.TR.list.finished",
    "parameter": ""
}


def tr_list_finished():
    print("\nIF_TR_LIST_FINISHED")
    request_json = IF_TR_list_finished
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_list_canceled = {
    "type": "REQ",
    "interface": "IF.TR.list.canceled",
    "parameter": ""
}


def tr_list_canceled():
    print("\nIF_TR_LIST_CANCELED")
    request_json = IF_TR_list_canceled
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_list_ongoingEID = {
    "type": "REQ",
    "interface": "IF.TR.list.ongoingEID",
    "parameter": ""
}


def tr_list_ongoingEID():
    print("\nIF_TR_LIST_ONGOINGEID")
    request_json = IF_TR_list_ongoingEID
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_production_record = {
    "type": "REQ",
    "interface": "IF.TR.production.record",
    "parameter": '{"kwh": "", "time": ""}'
}


def tr_production_record(kwh, production_time):
    print("\nIF_TR_PRODUCTION_RECORD")
    request_json = IF_TR_production_record
    parameter_json = {"kwh": str(kwh), "time": str(production_time)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_production_retrieveVolume = {
    "type": "REQ",
    "interface": "IF.TR.production.retrieveVolume",
    "parameter": '{"eid": ""}'
}


def tr_production_retrieveVolume(eid):
    print("\nIF_TR_PRODUCTION_RETRIEVEVOLUME")
    request_json = IF_TR_production_retrieveVolume
    parameter_json = {"eid": str(eid)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_production_retrieveHistory = {
    "type": "REQ",
    "interface": "IF.TR.production.retrieveHistory",
    "parameter": '{"eid": ""}'
}


def tr_production_retrieveHistory(eid):
    print("\nIF_TR_PRODUCTION_RETRIEVEHISTORY")
    request_json = IF_TR_production_retrieveHistory
    parameter_json = {"eid": str(eid)}
    request_json["parameter"] = json.dumps(parameter_json)
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


IF_TR_production_retrieveTotalVolume = {
    "type": "REQ",
    "interface": "IF.TR.production.retrieveTotalVolume",
    "parameter": '{"eid": ""}'
}


def tr_production_retrieveTotalVolume():
    print("\nIF_TR_PRODUCTION_RETRIEVETOTALVOLUME")
    request_json = IF_TR_production_retrieveTotalVolume
    print('PTM ==> BI: ')
    prnt(request_json)
    client.send(request_json)
    response = client.recv()
    print('BI ==> PTM: ')
    prnt(response)

    return response["parameter"]


def helper_send(sock, data):
    try:
        serialized = json.dumps(data)
    except(TypeError, ValueError):
        raise Exception('Cannot send JSON-serializable data')

    sock.send(serialized.encode('utf-8'))


def helper_recv(sock):
    CONST_RECV_MAX_SIZE = 4096
    data = sock.recv(CONST_RECV_MAX_SIZE)
    try:
        deserialized = json.loads(data)
    except(TypeError, ValueError):
        raise Exception('Data is not in JSON format')

    return deserialized


def get_keywallet():
    config = open("config.json").read()
    try:
        config_in_json = json.loads(config)
    except json.JSONDecodeError as err:
        print(f'Error loading JSON: {err.msg}')

    key_wallet = KeyWallet.load(config_in_json["KeyWallet"]["File"], config_in_json["KeyWallet"]["Password"])
    return key_wallet


def create_keywallet():
    created_keywallet = KeyWallet.create()
    if os.path.isfile(r"keystore"):
        os.remove(r"keystore")

    created_keywallet.store("./keystore", "Test1234$")


def load_keywallet(_pvkey):
    loaded_keywallet = KeyWallet.load(bytes.fromhex(_pvkey))
    if os.path.isfile(r"keystore"):
        os.remove(r"keystore")

    loaded_keywallet.store("./keystore", "Test1234$")


class Client(object):
    socket = None

    def __del__(self):
        self.close()

    def connect(self, host, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((host, port))

        self.socket.setblocking(True)
        return self

    def send(self, data):
        if not self.socket:
            raise Exception('Need a connection first before sending data')
        helper_send(self.socket, data)
        return self

    def recv(self):
        if not self.socket:
            raise Exception('Need a connection first before receiving data')
        return helper_recv(self.socket)

    def recv_and_close(self):
        data = self.recv()
        self.close()
        return data

    def close(self):
        if self.socket:
            self.socket.close()
            self.socket = None


# PTM, acting as a client, makes requests to Blockchain Interface (BI)
if __name__ == "__main__":
    with open("config.json") as config_set:
        config_set_json = json.loads(config_set.read())

    print('\033\n\n\n[36m' + '설정 값을 확인하세요' + '\033[0m\n\n\n')
    prnt(config_set_json)

    time.sleep(5)

    port = config_set_json["BI Server Port"]
    host = config_set_json["BI host"] # "3.35.52.24"
    print("Client Start")

    # connect to BI server
    client = Client()
    client.connect(host, port)
    print("Client connected")



    # stateOfcharge = float(input("SoC lv: "))

    # while True:
    while True:
        with open("config.json") as config_set:
            config_set_json = json.loads(config_set.read())
        print("loading EMS Data ...\n")
        stateParams=send_ptm_data_to_ems ("params")
        stateOfcharge = round(float(stateParams['rs_stateParameter'][0]['stateOfcharge']))
        genRatio = round(float(stateParams['rs_stateParameter'][0]['genRatio']))
        lossRatio = round(float(stateParams['rs_stateParameter'][0]['lossRatio']))

        #상태 기
        record_result_json = tr_production_record(round(stateOfcharge), str(time.time())[0:10]) #genRatio float타입은 에러생김
        record_result = record_result_json["result"]

        if stateOfcharge <= config_set_json["low SoC lv"] : #구매자상태
            time.sleep(10)
            print('\n### MODE: BUYER STATE ###\n')
            # get EID (IF.ID.retrieve)
            eid_json = id_retrieve()
            eid = eid_json["eid"]
            #print("==JSON===== " + str(eid_json))
            # print("==EXTRACT== " + str(eid))
            #print("==TYPE===== " + str(type(eid)))

            # get offered deal list (IF.TR.list.offered)
            offered_deal_list_json = tr_list_offered()  #제안된 거래 리스트 불러
            offered_deal_list = offered_deal_list_json["registered_deal_info_list"]
            # print(type(offered_deal_list[0]["ordered"]))
            false = "False"
            maket_cnt = 0
            for i in range(0, len(offered_deal_list)):
                if false in offered_deal_list[i]["ordered"]:
                    maket_cnt += 1
            if maket_cnt >= 1:
                try:
                    # get orderingID (searching min, price addr) # 동일한 가격을 경우, timestamp라던지, kwh값이라던지 선택
                    min_price_list = list(offered_deal_list[i]['price'] for i in range(len(offered_deal_list))) # 가격에 따른 리스트업.
                    # prnt(min_price_list)
                    min_price_list_index = min_price_list.index(min(min_price_list))
                    orderingID_json = offered_deal_list[min_price_list_index]
                    # prnt(min_price_list_index)
                    prnt(orderingID_json)
                    #elements; 'deal_id', 'state', 'seller_eid', 'price', 'kwh', 'ordered')
                    # print("==EXTRACT== " + str(orderingID_json))

                    # order deal (IF.TR.order)  #가져온 리스트를 기반으로 order
                    order_result_json = tr_order(orderingID_json['deal_id'], orderingID_json['kwh'], orderingID_json['price'])
                    order_result = order_result_json["result"]
                    print(order_result)
                    print(type(order_result))
                    if order_result == False:
                        raise buyer_regist_error()

                    # print("==JSON===== " + str(order_result_json))
                    # print("==EXTRACT== " + str(order_result))
                    # print("==TYPE===== " + str(type(order_result)))

                    # get owner's ordered deal id
                    offered_deal_id_json = tr_browse_dealIDBuyer(eid)  #내 주문에 대한 deal_id 확보
                    offered_deal_id = offered_deal_id_json["registered_deal_id"]
                    # print("===== deal id: " + offered_deal_id)
                    # print("==TYPE===== " + str(type(browse_deal_json)))
                    tmp_accepted = 0
                    for count in tqdm(range(1,config_set_json["accepted delay set"]), desc="Waiting for Accept", mininterval=1):

                        browse_deal_json = tr_browse_deal(offered_deal_id)
                        browse_deal_info = browse_deal_json['deal_info']
                        ordering_state = browse_deal_info['state']
                        # print("==JSON===== " + str(browse_deal_json))
                        # print("==EXTRACT== " + str(ordering_state))
                        # print("==TYPE===== " + str(type(ordering_state)))

                        if ordering_state == "accepted": #
                            tmp_accepted = 1
                            print("accept")
                            time.sleep(1)

                            accepted_list_json = tr_list_accepted()
                            # accepted_list = accepted_list_json[" "]
                            print(str(accepted_list_json))

                            # ordered_list_json = tr_list_ordered(offered_deal_id)  # order ID 조회
                            # ordered_list = ordered_list_json["requested_deal_info_list"]

                            deal_info_json = tr_browse_deal(offered_deal_id) #거래 조회
                            deal_info_completed = deal_info_json["deal_info"]
                            prnt(deal_info_completed)
                            send_ptm_data_to_ems('contractMsg') #Accept 이후 contractMsg를 통해 EMS에 결과 정보 전thd

                            config_set_json["low SoC lv"] -= 5
                            with open("./config.json", 'w') as f1:
                                json.dump(config_set_json, f1, indent=4)
                            time.sleep(1)
                            break

                        # print("=== NOT Accepted ===")
                        time.sleep(1)
                        continue
                    if not tmp_accepted == 1:
                        raise cancel_order()

                except cancel_order:
                    print("거래가 성사되지 않았습니다.")
                    cancel_result_json = tr_cancel_order()
                    cancel_result = cancel_result_json["result"]
                    prnt(cancel_result_json)

                except buyer_regist_error:
                    print("이미 거래 중 상태입니다.")
                    print("기존 거래를 취소합니다.")
                    cancel_result_json = tr_cancel_order()
                    cancel_result = cancel_result_json["result"]
                    cancel_result_json = tr_cancel_offer()
                    cancel_result = cancel_result_json["result"]
                    prnt(cancel_result_json)
            else :
                print("There are no products available for trading.")
            #print("==JSON===== " + str(offered_deal_list_json))
            # print("==EXTRACT== " + str(offered_deal_list))
            #print("==TYPE===== " + str(type(offered_deal_list)))



            # accepted_list #여기를 조건문 처리해서 마무리되게하고 전체 flow 반복되게하면 되지않으까?



            # accepted_list_json = tr_list_accepted()
            # print(str(accepted_list_json))

            # finish deal (IF.TR.finish)
            # finish_result_json = tr_finish()
            # finish_result = finish_result_json["result"]
            # print("==JSON===== " + str(finish_result_json))
            # print("==EXTRACT== " + str(finish_result))
            # print("==TYPE===== " + str(type(finish_result)))

            # cancel ordered deal (IF.TR.cancel.order)
            # cancel_result_json = tr_cancel_order()
            # cancel_result = cancel_result_json["result"]
            # print("==JSON===== " + str(cancel_result_json))
            # print("==EXTRACT== " + str(cancel_result))
            # print("==TYPE===== " + str(type(cancel_result)))


            # get EID Document (IF.ID.document)
            # eid_document_json = id_document(eid)
            # eid_document = eid_document_json["eid_document"]
            # print("==JSON===== " + str(eid_document_json))
            # print("==EXTRACT== " + str(eid_document))
            # print("==TYPE===== " + str(type(eid_document)))


            # client.close()
            # print("Client closed")









        elif stateOfcharge >= config_set_json["high SoC lv"] : #판매자상태
            try:
                print('\n### MODE: SELLER STATE ###\n')
                # get EID (IF.ID.retrieve)
                eid_json = id_retrieve()
                eid = eid_json["eid"]
                # print("BEMS ID: ", eid[9:])
                # print("==JSON===== " + str(eid_json))
                # print("==EXTRACT== " + str(eid))
                # print("==TYPE===== " + str(type(eid)))

                send_ptm_data_to_ems("regist")

                # offer deal (IF.TR.offer) price, quantity
                deal_id_json = tr_offer("1500", "5") #  price는 한전가격으로? //SoC 용량, pcs 용량 고려해서 연산해보//
                deal_id = deal_id_json["parameter"]["deal_id"]
                if deal_id_json["errno"] == "404":
                    raise offer_error()

                print("")
                offered_deal_id_json = tr_browse_dealIDSeller(eid)
                # offered_deal_id_json = tr_browse_dealID(eid)
                offered_deal_id = offered_deal_id_json["ongoing_deal_id"]
                # print("===== deal id: " + str(offered_deal_id_json))
                # print("===== deal id: " + offered_deal_id)
                tmp_ordered = 0
                for count in tqdm(range(1,config_set_json["contract delay set"]), desc="Waiting for orders", mininterval=1):

                    deal_info_json = tr_browse_deal(offered_deal_id)
                    deal_info = deal_info_json["deal_info"]["ordered"]

                    if deal_info == "True":
                        print()
                        ordered_list_json = tr_list_ordered(offered_deal_id)  # order ID 조회
                        ordered_list = ordered_list_json["requested_deal_info_list"]

                        acceptingID_info = ordered_list[0]
                        accept_result_json = tr_accept(acceptingID_info['buyer_eid'])
                        accept_result = accept_result_json["result"]


                        deal_info_json = tr_browse_deal(offered_deal_id) #거래 조회
                        deal_info_completed = deal_info_json["deal_info"]
                        prnt(deal_info_completed)
                        send_ptm_data_to_ems('contractMsg')

                        tmp_ordered = 1
                        break

                    time.sleep(1)
                    continue

                if not tmp_ordered == 1:
                    raise cancel_offer()
                #end_time계산
                finish_result_json = tr_finish()
                finish_result = finish_result_json["result"]
                config_set_json["high SoC lv"] += int(deal_info_completed["kwh"])
                with open("./config.json", 'w') as f1:
                    json.dump(config_set_json, f1, indent=4)

                time.sleep(1)

            except offer_error:
                print("현재 거래가 진행중입니다.")
                print("기존 거래를 취소합니다.")
                cancel_result_json = tr_cancel_order()
                cancel_result = cancel_result_json["result"]
                cancel_result_json = tr_cancel_offer()
                cancel_result = cancel_result_json["result"]
                prnt(cancel_result_json)

            except cancel_offer:
                cancel_result_json = tr_cancel_offer()
                cancel_result = cancel_result_json["result"]
                prnt(cancel_result_json)

        else : #노말 상태
            print('normal state: SoC lv is normally')
            time.sleep(3)

        # record production (IF.TR.production.record)

        # print("==JSON===== " + str(record_result_json))
        # print("==EXTRACT== " + str(record_result))
        # print("==TYPE===== " + str(type(record_result)))

    client.close()
    print("Client closed")




            # with open("ems_st_msg.json", 'w') as ems_st_msg:
            #     config_set_json = json.loads(config_set.read())



            # print("==JSON===== " + str(deal_id_json))
            # print("==EXTRACT== " + str(deal_id))
            # print("==TYPE===== " + str(type(deal_id)))
            # get owner's offered deal id
            # eid_json = id_retrieve()
            # eid = eid_json["eid"]



            # get ordered list to offered deal (IF.TR.ordered)
            # offered_deal_id = "0x85448150990e25de225a6f0782f549c142ed2608492292d750e2bd49e3b4d14d"
            # ordered_list_json = tr_list_ordered(offered_deal_id)
            # ordered_list = ordered_list_json["requested_deal_info_list"]
            # print("==JSON===== " + str(ordered_list_json))
            # print("==EXTRACT== " + str(ordered_list))
            # print("==TYPE===== " + str(type(ordered_list)))


            # browse deal info (IF.TR.browse.deal)
            # deal_id = "0x39ff7f192972015e3a163ae9b08cbdcbe7b670006fd65c7aa639c6523be25421"
            # deal_info_json = tr_browse_deal('0x4b760dcdd8ce63c9e2e032d638340f40c891fdf3b91c33d0dfe572cf9ac2c173')
            # deal_info = deal_info_json["deal_info"]["ordered"]
            # print("==JSON===== " + str(deal_info_json))
            # print("==EXTRACT== " + str(deal_info))
            # print("==TYPE===== " + str(type(deal_info)))

            # print("==JSON===== " + str(deal_info_json))
            # print("==EXTRACT== " + str(deal_info))
            # print("==TYPE===== " + str(type(deal_info)))

            # browse deal
            # deal_info = tr_browse_deal('0x4b760dcdd8ce63c9e2e032d638340f40c891fdf3b91c33d0dfe572cf9ac2c173')
            # deal_info_ex = deal_info
            # print("==TYPE===== " + str(type(deal_info)))
            # print("===== deal info: " + str(deal_info))

            # call_offer_list
            # call_offer_list_json = tr_list_offered()
            # print("==TYPE===== " + str(type(call_offer_list_json)))
            # call_offer_list = call_offer_list_json["registered_deal_info_list"]
            # print("==JSON===== " + str(call_offer_list_json))
            # print("==EXTRACT== " + str(call_offer_list[1]["deal_id"]))
            # print("==TYPE===== " + str(type(call_offer_list[1])))

            # get ordered deal list
            # ordered_list_json = tr_list_ordered("0xdebbe7ac59853e3e15c8a6a1aee60d0ed491bfe3b6093eff9fafd69ebfcfbd46")
            # ordered_list = ordered_list_json["requested_deal_info_list"]
            # print("===== ordered list: " + str(ordered_list))
            # print("==TYPE===== " + str(type(ordered_list)))

        # if 안으로 들어가도될것같아
            # # get ordered list to offered deal (IF.TR.ordered)
            # # offered_deal_id = "0xacf19f6ad4b35734e3e2abfd05680b013634e1c07d4ff8d2246f7812749a5b67"
            # ordered_list_json = tr_list_ordered(offered_deal_id)  # order ID 조회
            # ordered_list = ordered_list_json["requested_deal_info_list"]
            # # print("==EXTRACT== " + str(ordered_list[0]))
            # # print("==TYPE===== " + str(type(ordered_list[0])))
            # acceptingID_info = ordered_list[0]
            #
            # # accept deal (IF.TR.accept)# 주문 수락
            #
            # accept_result_json = tr_accept(acceptingID_info['buyer_eid'])
            # accept_result = accept_result_json["result"]
            # # print("==JSON===== " + str(accept_result_json))
            # # print("==EXTRACT== " + str(accept_result))
            # # print("==TYPE===== " + str(type(accept_result)))
            #
            # # finish deal (IF.TR.finish) #거래종료
            # finish_result_json = tr_finish()
            # finish_result = finish_result_json["result"]
            #
            # # print("==JSON===== " + str(finish_result_json))
            # # print("==EXTRACT== " + str(finish_result))
            # # print("==TYPE===== " + str(type(finish_result)))
            # # print("==JSON===== " + str(deal_info_json))
            # # print("==EXTRACT== " + str(deal_info))
            #
            # # get ongoing eid list (IF.TR.list.ongoingEID)
            # # ongoing_eid_list_json = tr_list_ongoingEID()
            # # ongoing_eid_list = ongoing_eid_list_json["ongoing_eid_list"]
            # # print("    JSON    =" + str(ongoing_eid_list_json))
            # # print("  EXTRACT   =" + str(ongoing_eid_list))
            # # print("    TYPE    = " + str(type(ongoing_eid_list)))
            #
            # # get finished deal list (IF.TR.list.finished)
            # # finished_deal_list_json = tr_list_finished()
            # # finished_deal_list = finished_deal_list_json["completed_deal_info_list"]
            # # print("==JSON===== " + str(finished_deal_list_json))
            # # print("==EXTRACT== " + str(finished_deal_list))
            # # print("==TYPE===== " + str(type(finished_deal_list)))
            #
            # # get ongoing eid list (IF.TR.list.ongoingEID)
            # # ongoing_eid_list_json = tr_list_ongoingEID()
            # # ongoing_eid_list = ongoing_eid_list_json["ongoing_eid_list"]
            # # print("    JSON    =" + str(ongoing_eid_list_json))
            # # print("  EXTRACT   =" + str(ongoing_eid_list))
            # # print("    TYPE    = " + str(type(ongoing_eid_list)))
            #
            # # accept deal (IF.TR.accept)
            # # buyer_eid = "eid:bems:0001a25ce4b8d6c3bf64c7fdbfb323b46e9f3f854ac443765f0"
            # # accept_result_json = tr_accept(buyer_eid)
            # # accept_result = accept_result_json["result"]
            # # print("==JSON===== " + str(accept_result_json))
            # # print("==EXTRACT== " + str(accept_result))
            # # print("==TYPE===== " + str(type(accept_result)))
            #
    # # finish deal (IF.TR.finish)
            # # finish_result_json = tr_finish()
            # # finish_result = finish_result_json["result"]
            # # print("==JSON===== " + str(finish_result_json))
            # # print("==EXTRACT== " + str(finish_result))
            # # print("==TYPE===== " + str(type(finish_result)))
            #
            # # cancel order deal
            # # cancel_order_result = tr_cancel_order()
            # # print("===== cancel order result: " + str(cancel_order_result))
            #
            # # get ordered deal list
            # # ordered_list = tr_list_ordered(offer_deal_id)
            # # print("===== ordered list: " + str(ordered_list))
            #
            # # client.close()
            # # print("Client closed")
            # deal_info_json = tr_browse_deal(offered_deal_id) #거래 조회
            # deal_info_completed = deal_info_json["deal_info"]
            # send_ptm_data_to_ems('contractMsg')

    # 구매 2 판매 1 > 3가지
    # 구매 1 판매 2 > 3가지
    # 구매 1 판매 1 > 6가지

    # EMS Data (stateOfcharge, genRatio, lossRatio; float type)
    # stateOfcharge = stateParams['rs_stateParameter'][0]['stateOfcharge']
    # genRatio = stateParams['rs_stateParameter'][0]['genRatio']
    # lossRatio = stateParams['rs_stateParameter'][0]['lossRatio']

    # f = open("/home/korea/ptm-cli/test-1/keystore", 'r') #file open test 파일 오픈 테스
    # line = f.readline()
    # print(line)
    # f.close()

    #subprocess.run(['/home/korea/ptm-cli/test-1/sub-test.sh'], shell=True) #subprocess


    # offer deal (IF.TR.offer)
    # deal_id_json = tr_offer("200", "200")
    # deal_id = deal_id_json["deal_id"]
    # print("==JSON===== " + str(deal_id_json))
    # print("==EXTRACT== " + str(deal_id))
    # print("==TYPE===== " + str(type(deal_id)))

    # get owner's offered deal id
    # eid_json = id_retrieve()
    # eid = eid_json["eid"]
    # offered_deal_id_json = tr_browse_dealIDSeller(eid)
    # offered_deal_id = offered_deal_id_json["ongoing_deal_id"]
    # print("===== deal id: " + offered_deal_id)

    # get ordered list to offered deal (IF.TR.ordered)
    # offered_deal_id = "0xacf19f6ad4b35734e3e2abfd05680b013634e1c07d4ff8d2246f7812749a5b67"
    # ordered_list_json = tr_list_ordered(offered_deal_id)
    # ordered_list = ordered_list_json["requested_deal_info_list"]
    # print("==JSON===== " + str(ordered_list_json))
    # print("==EXTRACT== " + str(ordered_list))
    # print("==TYPE===== " + str(type(ordered_list)))

    # browse deal info (IF.TR.browse.deal)
    # deal_id = "0x39ff7f192972015e3a163ae9b08cbdcbe7b670006fd65c7aa639c6523be25421"
    # deal_info_json = tr_browse_deal(deal_id)
    # deal_info = deal_info_json["deal_info"]
    # print("==JSON===== " + str(deal_info_json))
    # print("==EXTRACT== " + str(deal_info))
    # print("==TYPE===== " + str(type(deal_info)))

    # browse deal ID by owner EID (IF.TR.browse.dealID)
    # owner_eid = "eid:bems:00019894330b040aec4e015c7b5f8b5121b01c671e4d1e26f60"
    # ongoing_deal_id_json = tr_browse_dealIDSeller(owner_eid)
    # ongoing_deal_id = ongoing_deal_id_json["ongoing_deal_id"]
    # print("==JSON===== " + str(ongoing_deal_id_json))
    # print("==EXTRACT== " + str(ongoing_deal_id))
    # print("==TYPE===== " + str(type(ongoing_deal_id)))

    # get offered deal list (IF.TR.list.offered)
    # offered_deal_list_json = tr_list_offered()
    # offered_deal_list = offered_deal_list_json["registered_deal_info_list"]
    # print("==JSON===== " + str(offered_deal_list_json))
    # print("==EXTRACT== " + str(offered_deal_list))
    # print("==TYPE===== " + str(type(offered_deal_list)))

    # get accepted deal list (IF.TR.list.accepted)
    # accepted_deal_list_json = tr_list_accepted()
    # accepted_deal_list = accepted_deal_list_json["accepted_deal_info_list"]
    # print("==JSON===== " + str(accepted_deal_list_json))
    # print("==EXTRACT== " + str(accepted_deal_list))
    # print("==TYPE===== " + str(type(accepted_deal_list)))

    # get finished deal list (IF.TR.list.finished)
    # finished_deal_list_json = tr_list_finished()
    # finished_deal_list = finished_deal_list_json["completed_deal_info_list"]
    # print("==JSON===== " + str(finished_deal_list_json))
    # print("==EXTRACT== " + str(finished_deal_list))
    # print("==TYPE===== " + str(type(finished_deal_list)))

    # get canceled deal list (IF.TR.list.canceled)
    # canceled_deal_list_json = tr_list_canceled()
    # canceled_deal_list = canceled_deal_list_json["canceled_deal_info_list"]
    # print("==JSON===== " + str(canceled_deal_list_json))
    # print("==EXTRACT== " + str(canceled_deal_list))
    # print("==TYPE===== " + str(type(canceled_deal_list)))

    # accept deal (IF.TR.accept)
    # buyer_eid = "eid:bems:0001a25ce4b8d6c3bf64c7fdbfb323b46e9f3f854ac443765f0"
    # accept_result_json = tr_accept(buyer_eid)
    # accept_result = accept_result_json["result"]
    # print("==JSON===== " + str(accept_result_json))
    # print("==EXTRACT== " + str(accept_result))
    # print("==TYPE===== " + str(type(accept_result)))

    # get ongoing eid list (IF.TR.list.ongoingEID)
    # ongoing_eid_list_json = tr_list_ongoingEID()
    # ongoing_eid_list = ongoing_eid_list_json["ongoing_eid_list"]
    # print("==JSON===== " + str(ongoing_eid_list_json))
    # print("==EXTRACT== " + str(ongoing_eid_list))
    # print("==TYPE===== " + str(type(ongoing_eid_list)))

    # finish deal (IF.TR.finish)
    # finish_result_json = tr_finish()
    # finish_result = finish_result_json["result"]
    # print("==JSON===== " + str(finish_result_json))
    # print("==EXTRACT== " + str(finish_result))
    # print("==TYPE===== " + str(type(finish_result)))

    # cancel offered deal (IF.TR.cancel.offer)
    # cancel_result_json = tr_cancel_offer()
    # cancel_result = cancel_result_json["result"]
    # print("==JSON===== " + str(cancel_result_json))
    # print("==EXTRACT== " + str(cancel_result))
    # print("==TYPE===== " + str(type(cancel_result)))

    # cancel accept deal (IF.TR.cancel.accept)
    # cancel_result_json = tr_cancel_accept()
    # cancel_result = cancel_result_json["result"]
    # print("==JSON===== " + str(cancel_result_json))
    # print("==EXTRACT== " + str(cancel_result))
    # print("==TYPE===== " + str(type(cancel_result)))

    # 생산성관리 스마트 컨트랙트
    # record production (IF.TR.production.record)
    # record_result_json = tr_production_record("200", "1595949857")
    # record_result = record_result_json["result"]
    # print("==JSON===== " + str(record_result_json))
    # print("==EXTRACT== " + str(record_result))
    # print("==TYPE===== " + str(type(record_result)))

    # get eid production retrieve volume
    # eid = "eid:bems:00019894330b040aec4e015c7b5f8b5121b01c671e4d1e26f60"
    # retrieve_result_json = tr_production_retrieveVolume(eid)
    # retrieve_result = retrieve_result_json["eid_total_production"]
    # print("==JSON===== " + str(retrieve_result_json))
    # print("==EXTRACT== " + str(retrieve_result))
    # print("==TYPE===== " + str(type(retrieve_result)))

    # get eid production history
    # eid = "eid:bems:00019894330b040aec4e015c7b5f8b5121b01c671e4d1e26f60"
    # production_history_json = tr_production_retrieveHistory(eid)
    # production_history = production_history_json["production_history"]
    # print("==JSON===== " + str(production_history_json))
    # print("==EXTRACT== " + str(production_history))
    # print("==TYPE===== " + str(type(production_history)))

    # get total production retrieve volume
    # retrieve_result_json = tr_production_retrieveTotalVolume()
    # retrieve_result = retrieve_result_json["total_production"]
    # print("==JSON===== " + str(retrieve_result_json))
    # print("==EXTRACT== " + str(retrieve_result))
    # print("==TYPE===== " + str(type(retrieve_result)))
