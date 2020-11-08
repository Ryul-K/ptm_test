from socket import *
import json
import os
import time
from iconsdk.wallet.wallet import KeyWallet

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

    # load_keywallet("19ae0ce4e74da7ffcd4317898ad0ed34363902888b927919f32d7046dcbdecfb")
    # print(get_keywallet().get_private_key())


    # connect to BI server
    client = Client()
    client.connect(host, port)
    print("Client connected")

    # get EID (IF.ID.retrieve)
    eid_json = id_retrieve()
    eid = eid_json["eid"]
    #print("==JSON===== " + str(eid_json))
    # print("==EXTRACT== " + str(eid))
    #print("==TYPE===== " + str(type(eid)))

    # get offered deal list (IF.TR.list.offered)
    offered_deal_list_json = tr_list_offered()  #제안된 거래 리스트 불러
    offered_deal_list = offered_deal_list_json["registered_deal_info_list"]
    #print("==JSON===== " + str(offered_deal_list_json))
    # print("==EXTRACT== " + str(offered_deal_list))
    #print("==TYPE===== " + str(type(offered_deal_list)))

    # get orderingID (searching min, price addr) # 동일한 가격을 경우, timestamp라던지, kwh값이라던지 선택
    min_price_list = list(offered_deal_list[i]['price'] for i in range(len(offered_deal_list))) # 가격에 따른 리스트업.
    min_price_list_index = min_price_list.index(max(min_price_list))
    orderingID_json = offered_deal_list[min_price_list_index]
    #elements; 'deal_id', 'state', 'seller_eid', 'price', 'kwh', 'ordered')
    # print("==EXTRACT== " + str(orderingID_json))

    # order deal (IF.TR.order)  #가져온 리스트를 기반으로 order
    order_result_json = tr_order(orderingID_json['deal_id'], orderingID_json['kwh'], orderingID_json['price'])
    order_result = order_result_json["result"]
    # print("==JSON===== " + str(order_result_json))
    # print("==EXTRACT== " + str(order_result))
    # print("==TYPE===== " + str(type(order_result)))

    # get owner's ordered deal id
    offered_deal_id_json = tr_browse_dealIDBuyer(eid)  #내 주문에 대한 deal_id 확보
    offered_deal_id = offered_deal_id_json["registered_deal_id"]
    # print("===== deal id: " + offered_deal_id)

    # print("==TYPE===== " + str(type(browse_deal_json)))

    count = 0
    while count < 1000: # accept 대
        count = count + 1

        browse_deal_json = tr_browse_deal(offered_deal_id)
        browse_deal_info = browse_deal_json['deal_info']
        ordering_state = browse_deal_info['state']
        # print("==JSON===== " + str(browse_deal_json))
        # print("==EXTRACT== " + str(ordering_state))
        # print("==TYPE===== " + str(type(ordering_state)))

        if ordering_state == "accepted":
            print("great")
            print("accept")
            time.sleep(1)
            break

        print("=== NOT Accepted ===")
        time.sleep(1)
        continue


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


    client.close()
    print("Client closed")
