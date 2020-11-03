from socket import *
import json
import os
import time
from iconsdk.wallet.wallet import KeyWallet
from datetime import datetime

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
    "parameter": '{"price":"", "quantity":""}'
}


def tr_offer(price, quantity):
    print("\nIF_TR_OFFER")
    request_json = IF_TR_offer
    parameter_json = {"price": str(price), "quantity": str(quantity)}
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


IF_TR_browse_dealID = {
    "type": "REQ",
    "interface": "IF.TR.browse.dealID",
    "parameter": '{"eid": ""}'
}


def tr_browse_dealID(eid):
    print("\nIF_TR_BROWSE_DEALID")
    request_json = IF_TR_browse_dealID
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
    port = 5555 #test-2
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
    # print("==JSON===== " + str(eid_json))
    # print("==EXTRACT== " + str(eid))
    # print("==TYPE===== " + str(type(eid)))

    # offer deal (IF.TR.offer) price, quantity
    deal_id_json = tr_offer("3000", "200")
    deal_id = deal_id_json["deal_id"]
    # print("==JSON===== " + str(deal_id_json))
    # print("==EXTRACT== " + str(deal_id))



    # print("==TYPE===== " + str(type(deal_id)))
    # get owner's offered deal id
    # eid_json = id_retrieve()
    # eid = eid_json["eid"]
    offered_deal_id_json = tr_browse_dealIDSeller(eid)
    # offered_deal_id_json = tr_browse_dealID(eid)
    offered_deal_id = offered_deal_id_json["ongoing_deal_id"]
    # print("===== deal id: " + str(offered_deal_id_json))
    # print("===== deal id: " + offered_deal_id)

    deal_info_json = tr_browse_deal(offered_deal_id)  #time stamp 딕셔너리 관리, deal_info_time_json
    deal_info_time = deal_info_json["deal_info"]["txTimestamp"]
    now = deal_info_time[0:10]
    date = datetime.fromtimestamp(int(now)).strftime('%Y%m%d%H%M%S')
    deal_info_time_json = {'registerd' : date}
    # print(str(deal_info_time_json))

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

    count = 0
    while count < 1000:
        count = count + 1

        deal_info_json = tr_browse_deal(offered_deal_id)
        deal_info_ordered = deal_info_json["deal_info"]["ordered"]

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
        if deal_info_ordered == "True":
            print("Accept")
            deal_info_time = deal_info_json["deal_info"]["txTimestamp"]
            now = deal_info_time[0:10]
            date = datetime.fromtimestamp(int(now)).strftime('%Y%m%d%H%M%S')
            deal_info_time_json['ordered'] = date
            print(str(deal_info_time_json))
            time.sleep(1)
            break

        print("=== NOT Ordered ===")
        time.sleep(1)
        continue


    # get ordered list to offered deal (IF.TR.ordered)
    # offered_deal_id = "0xacf19f6ad4b35734e3e2abfd05680b013634e1c07d4ff8d2246f7812749a5b67"
    ordered_list_json = tr_list_ordered(offered_deal_id)  # order ID 조회
    ordered_list = ordered_list_json["requested_deal_info_list"]
    # print("==EXTRACT== " + str(ordered_list[0]))
    # print("==TYPE===== " + str(type(ordered_list[0])))
    acceptingID_info = ordered_list[0]

    # accept deal (IF.TR.accept)# 주문 수락

    accept_result_json = tr_accept(acceptingID_info['buyer_eid'])
    accept_result = accept_result_json["result"]
    # print("==JSON===== " + str(accept_result_json))
    # print("==EXTRACT== " + str(accept_result))
    # print("==TYPE===== " + str(type(accept_result)))

    # finish deal (IF.TR.finish) #거래종료
    finish_result_json = tr_finish()
    finish_result = finish_result_json["result"]
    # print("==JSON===== " + str(finish_result_json))
    # print("==EXTRACT== " + str(finish_result))
    # print("==TYPE===== " + str(type(finish_result)))

    deal_info_json = tr_browse_deal(offered_deal_id) #거래 조회
    # print("==JSON===== " + str(deal_info_json))
    # print("==EXTRACT== " + str(deal_info))

    # get ongoing eid list (IF.TR.list.ongoingEID)
    # ongoing_eid_list_json = tr_list_ongoingEID()
    # ongoing_eid_list = ongoing_eid_list_json["ongoing_eid_list"]
    # print("    JSON    =" + str(ongoing_eid_list_json))
    # print("  EXTRACT   =" + str(ongoing_eid_list))
    # print("    TYPE    = " + str(type(ongoing_eid_list)))

    # get finished deal list (IF.TR.list.finished)
    # finished_deal_list_json = tr_list_finished()
    # finished_deal_list = finished_deal_list_json["completed_deal_info_list"]
    # print("==JSON===== " + str(finished_deal_list_json))
    # print("==EXTRACT== " + str(finished_deal_list))
    # print("==TYPE===== " + str(type(finished_deal_list)))

    # get ongoing eid list (IF.TR.list.ongoingEID)
    # ongoing_eid_list_json = tr_list_ongoingEID()
    # ongoing_eid_list = ongoing_eid_list_json["ongoing_eid_list"]
    # print("    JSON    =" + str(ongoing_eid_list_json))
    # print("  EXTRACT   =" + str(ongoing_eid_list))
    # print("    TYPE    = " + str(type(ongoing_eid_list)))

    # accept deal (IF.TR.accept)
    # buyer_eid = "eid:bems:0001a25ce4b8d6c3bf64c7fdbfb323b46e9f3f854ac443765f0"
    # accept_result_json = tr_accept(buyer_eid)
    # accept_result = accept_result_json["result"]
    # print("==JSON===== " + str(accept_result_json))
    # print("==EXTRACT== " + str(accept_result))
    # print("==TYPE===== " + str(type(accept_result)))

    # finish deal (IF.TR.finish)
    # finish_result_json = tr_finish()
    # finish_result = finish_result_json["result"]
    # print("==JSON===== " + str(finish_result_json))
    # print("==EXTRACT== " + str(finish_result))
    # print("==TYPE===== " + str(type(finish_result)))

    # cancel order deal
    # cancel_order_result = tr_cancel_order()
    # print("===== cancel order result: " + str(cancel_order_result))

    # get ordered deal list
    # ordered_list = tr_list_ordered(offer_deal_id)
    # print("===== ordered list: " + str(ordered_list))

    client.close()
    print("Client closed")
