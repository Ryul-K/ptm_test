import requests, json, os, time, subprocess
from socket import *
from iconsdk.wallet.wallet import KeyWallet
from datetime import datetime
from tqdm import tqdm
from pyprnt import prnt

headers = {'Content-Type': 'application/json; charset=utf-8'} #EMS 데이터 타입 # cookies = {'session_id': 'sorryidontcare'}

# response.status_code
# response.text


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
            response_json = res.json()
            # prnt(response_json)
            # device에 대한 정보 받아와서 보여주
            return response_json #response_json
        except:
            print("Device 기록에 실패했습니다.")
    elif target_Data == "regist" :
        try:
            target['rq_param_parameter'] = eid
            res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            # print('\n status_code : ' + str(res.status_code))
            response_json = res.json()
            # prnt(response_json)
            # device에 대한 정보 받아와서 보여주
            return response_json#response_json
        except:
            print("Device 등록에 실패했습니다.")

    elif target_Data == "params" :
        try:
            res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            # print('\n status_code : ' + str(res.status_code))
            response_json = res.json()
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
            target['rq_param_parameter']['dep2_rq_param_id'] = deal_info_completed["deal_id"]
            target['rq_param_parameter']['dep2_rq_param_seller'] = deal_info_completed["seller_eid"]
            target['rq_param_parameter']['dep2_rq_param_buyer'] = deal_info_completed["buyer_eid"]
            target['rq_param_parameter']['dep2_rq_param_price'] = deal_info_completed["price"]
            target['rq_param_parameter']['dep2_rq_param_quantity'] = deal_info_completed["kwh"]
            target['rq_param_parameter']['dep2_rq_param_tr_st_time'] = datetime.fromtimestamp(int(deal_info_completed["txTimestamp"][0:10]) + tmp_config_json["start_delay"]).strftime('%Y%m%d%H%M%S')
            #complete 되고 tmp_config_json["start_delay"] = 300초 만큼 딜레이 후 전력 거래 시#
            target['rq_param_parameter']['dep2_rq_param_tr_ed_time'] = ""
            target['rq_param_time'] = datetime.fromtimestamp(int(str(time.time())[0:10])).strftime('%Y%m%d%H%M%S')

            res = requests.post(ems_url, headers=headers, data=json.dumps(target))
            # print('\n status_code : ' + str(res.status_code))
            response_json = res.json()
            # prnt(response_json)
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

    return response["parameter"]


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

    port = config_set_json["BI Server Port"]
    host = config_set_json["BI host"] # "3.35.52.24"
    print("Client Start")
    # keywallet setting
    # create_keywallet()
    # load_keywallet("19ae0ce4e74da7ffcd4317898ad0ed34363902888b927919f32d7046dcbdecfb")
    # print(get_keywallet().get_private_key())

    # create keywallet
    create_keywallet()

    # connect to BI server
    client = Client()
    client.connect(host, port)
    print("Client connected")

    # create EID (IF.ID.create)
    eid_json = id_create()
    eid = eid_json["eid"]
    # print("==JSON===== " + str(eid_json))
    # print("==EXTRACT== " + str(eid))
    # print("==TYPE===== " + str(type(eid)))

    # get EID (IF.ID.retrieve)
    # eid_json = id_retrieve()
    # eid = eid_json["eid"]
    # print("==JSON===== " + str(eid_json))
    # print("==EXTRACT== " + str(eid))
    # print("==TYPE===== " + str(type(eid)))

    # get EID Document (IF.ID.document)
    eid_document_json = id_document(eid)
    eid_document = eid_document_json["eid_document"]
    # print("==JSON===== " + str(eid_document_json))
    # print("==EXTRACT== " + str(eid_document))
    # print("==TYPE===== " + str(type(eid_document)))

    client.close()
    print("Client closed")
