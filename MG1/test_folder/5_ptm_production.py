from socket import *
from iconsdk.wallet.wallet import KeyWallet
import requests, json, os, time, subprocess

headers = {'Content-Type': 'application/json; charset=utf-8'} #EMS 데이터 타입
# cookies = {'session_id': 'sorryidontcare'}
url_device = 'http://220.80.195.130:4848/ddevice/device'
url_regist = 'http://220.80.195.130:4848/m_id_regist'
url_params = 'http://220.80.195.130:4848/a_stateparams'
url_contractMsg = 'http://220.80.195.130:4848/m_tr/contractMsg'
# response.status_code
# response.text

data_device = {
    "rq_param_device" : "INV",
    "rq_param_tpm_id" : "5",
    "rq_param_send_time":"20190930153015110"
    }

data_regist = {
    "rq_param_target" : "EMS",
    "rq_param_type" : "REQ",
    "rq_param_interface" : "IF.ID.regist",
    "rq_param_parameter" : "id:bems:dc5f5ca3959409c3292f44e942b9957dd2b4de6c"
    }

data_params = {
    "rq_param_target" : "EMS",
    "rq_param_type" : "REQ",
    "rq_param_interface" : "IF_STATE.stateParams",
    "rq_param_parameter" : "",
    "rq_param_time" : ""
    }

data_contractMsg = {
    "rq_param_target" : "EMS",
    "rq_param_type" : "REQ",
    "rq_param_interface" : "IF.TR.contractMsg",
    "rq_param_parameter" : {
            "dep2_rq_param_id": "0x123218dc498e271d8b66488284bb982f14d87ae61baaf37dce52fc125f05ef60",
            "dep2_rq_param_seller": "3d61d6654a585b2b89b2290b9de3c7c6ab543063",
            "dep2_rq_param_buyer": "6d61d6654a585b2b89b2290b9de3c7c6ab543063",
            "dep2_rq_param_price": 50,
            "dep2_rq_param_quantity": 200,
            "dep2_rq_param_tr_st_time": "20200923165700",
            "dep2_rq_param_tr_ed_time": "20200923175700"
            },
    "rq_param_time" : "20200923160500"
    }

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


def id_retrieve():
    print("\nIF_ID_RETRIEVE")
    request_json = IF_ID_retrieve
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


def id_document(eid):
    print("\nIF_ID_DOCUMENT")
    request_json = IF_ID_document
    parameter_json = {"eid": str(eid)}
    request_json["parameter"] = json.dumps(parameter_json)
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_finish = {
    "type": "REQ",
    "interface": "IF.TR.finish",
    "parameter": ""
}


def tr_finish():
    print("\nIF_TR_FINISH")
    request_json = IF_TR_finish
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_cancel_offer = {
    "type": "REQ",
    "interface": "IF.TR.cancel.offer",
    "parameter": ""
}


def tr_cancel_offer():
    print("\nIF_TR_CANCEL_OFFER")
    request_json = IF_TR_cancel_offer
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_cancel_order = {
    "type": "REQ",
    "interface": "IF.TR.cancel.order",
    "parameter": ""
}


def tr_cancel_order():
    print("\nIF_TR_CANCEL_ORDER")
    request_json = IF_TR_cancel_order
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_cancel_accept = {
    "type": "REQ",
    "interface": "IF.TR.cancel.accept",
    "parameter": ""
}


def tr_cancel_accept():
    print("\nIF_TR_CANCEL_ACCEPT")
    request_json = IF_TR_cancel_accept
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_browse_deal = {
    "type": "REQ",
    "interface": "IF.TR.browse.deal",
    "parameter": '{"deal_id": ""}'
}


def tr_browse_deal(deal_id):
    print("\nIF_TR_BROWSE_DEAL")
    request_json = IF_TR_browse_deal
    parameter_json = {"deal_id": str(deal_id)}
    request_json["parameter"] = json.dumps(parameter_json)
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_list_offered = {
    "type": "REQ",
    "interface": "IF.TR.list.offered",
    "parameter": ""
}


def tr_list_offered():
    print("\nIF_TR_LIST_OFFERED")
    request_json = IF_TR_list_offered
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_list_accepted = {
    "type": "REQ",
    "interface": "IF.TR.list.accepted",
    "parameter": ""
}


def tr_list_accepted():
    print("\nIF_TR_LIST_ACCEPTED")
    request_json = IF_TR_list_accepted
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_list_finished = {
    "type": "REQ",
    "interface": "IF.TR.list.finished",
    "parameter": ""
}


def tr_list_finished():
    print("\nIF_TR_LIST_FINISHED")
    request_json = IF_TR_list_finished
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_list_canceled = {
    "type": "REQ",
    "interface": "IF.TR.list.canceled",
    "parameter": ""
}


def tr_list_canceled():
    print("\nIF_TR_LIST_CANCELED")
    request_json = IF_TR_list_canceled
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_list_ongoingEID = {
    "type": "REQ",
    "interface": "IF.TR.list.ongoingEID",
    "parameter": ""
}


def tr_list_ongoingEID():
    print("\nIF_TR_LIST_ONGOINGEID")
    request_json = IF_TR_list_ongoingEID
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

    return response["parameter"]


IF_TR_production_retrieveTotalVolume = {
    "type": "REQ",
    "interface": "IF.TR.production.retrieveTotalVolume",
    "parameter": '{"eid": ""}'
}


def tr_production_retrieveTotalVolume():
    print("\nIF_TR_PRODUCTION_RETRIEVETOTALVOLUME")
    request_json = IF_TR_production_retrieveTotalVolume
    print(f'PTM ==> BI: {request_json}')
    client.send(request_json)
    response = client.recv()
    print(f'BI ==> PTM: {response}')

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
    print("Client Start")
    port = 5555
    host = "localhost"  # "3.35.52.24"

    # connect to BI server
    client = Client()
    client.connect(host, port)
    print("Client connected")

    stateOfcharge = 60.5
    genRatio = 20.5
    lossRatio = 40.0


    30< soc < 60이면 노말일때 > soc 값 체크하면서 유지?
    soc가 30 이면 구매 >
    soc가 60 이상이면 판매

    구매 2 판매 1 > 3가지
    구매 1 판매 2 > 3가지
    구매 1 판매 1 > 6가지

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

    client.close()
    print("Client closed")
