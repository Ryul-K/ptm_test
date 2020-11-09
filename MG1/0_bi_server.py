from RPCmanager import RPCmanager
from threading import Thread
from socket import *
from iconsdk.wallet.wallet import KeyWallet
import json
import re


# cx3bb702a5e8ce80f7ac54c465b53c26fbb38cde23 <- 세팅 스마트컨트랙트
# cx8945f622877ac91cfa344c08d7c36440fe377010


def helper_send(sock, data: dict) -> None:
    try:
        serialized = json.dumps(data)
    except(TypeError, ValueError):
        raise Exception('Cannot send JSON-serializable data')

    sock.send(serialized.encode('utf-8'))


def helper_recv(sock: socket) -> dict:
    CONST_RECV_MAX_SIZE = 4096
    data = sock.recv(CONST_RECV_MAX_SIZE)
    if data == b'':
        return ''
    try:
        deserialized = json.loads(data)
    except(TypeError, ValueError):
        raise Exception('Data is not in JSON format')

    return deserialized


class ServerThread(Thread):
    client = None
    dispatcher = None

    def __init__(self, _client, _dispatcher):
        Thread.__init__(self, name='')
        self.client = _client
        self.dispatcher = _dispatcher

    def run(self):
        while (True):
            data = self.recv()
            if data == '':
                self.client.close()
                break

            response = self.dispatcher.dispatch_request(data)
            self.send(response)

    def __del__(self) -> None:
        self.close()

    def accept(self):
        if self.client:
            self.client.close()
        self.client, self.client_addr = self.socket.accept()

        return self

    def send(self, data: dict):
        if not self.client:
            raise Exception('Cannot send data, no client is connected')
        helper_send(self.client, data)

        return self

    def recv(self) -> dict:
        if not self.client:
            raise Exception('Cannot receive data, no client is connected')

        return helper_recv(self.client)

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
        # if self.socket:
        #     self.socket.close()
        #     self.socket = None


class Dispatcher(object):
    def __init__(self, _config_in_json):
        self.rpcm = RPCmanager(_config_in_json)

    def get_BIpubkey(self) -> str:
        pubkey = self.rpcm.key_wallet.public_key

        return pubkey

    def get_BIaddress(self) -> str:
        return self.rpcm.key_wallet.get_address()

    def dispatch_request(self, _request: dict) -> dict:
        interface = _request["interface"]
        parameter = _request["parameter"]

        print(f'get a request: {interface}')

        if interface == 'IF.ID.onboard':
            result = self.call_ID_onboard(parameter)
        elif interface == 'IF.ID.create':
            result = self.call_ID_create()
        elif interface == 'IF.ID.retrieve':
            result = self.call_ID_retrieve()
        elif interface == 'IF.ID.document':
            result = self.call_ID_document(parameter)
        elif interface == 'IF.ID.regist':
            result = self.call_ID_regist(parameter)
        elif interface == 'IF.TR.offer':
            result = self.call_TR_offer(parameter)
        elif interface == 'IF.TR.order':
            result = self.call_TR_order(parameter)
        elif interface == 'IF.TR.accept':
            result = self.call_TR_accept(parameter)
        elif interface == 'IF.TR.finish':
            result = self.call_TR_finish()
        elif interface == 'IF.TR.cancel.offer':
            result = self.call_TR_cancel_offer()
        elif interface == 'IF.TR.cancel.order':
            result = self.call_TR_cancel_order()
        elif interface == 'IF.TR.cancel.accept':
            result = self.call_TR_cancel_accept()
        elif interface == 'IF.TR.browse.deal':
            result = self.call_TR_browse_deal_info(parameter)
        elif interface == 'IF.TR.browse.dealIDSeller':
            result = self.call_TR_browse_ongoing_deal_id(parameter)
        elif interface == 'IF.TR.browse.dealIDBuyer':
            result = self.call_TR_browse_deal_id_buyer(parameter)
        elif interface == 'IF.TR.list.ordered':
            result = self.call_TR_list_ordered(parameter)
        elif interface == 'IF.TR.list.offered':
            result = self.call_TR_list_offered()
        elif interface == 'IF.TR.list.accepted':
            result = self.call_TR_list_accepted()
        elif interface == 'IF.TR.list.finished':
            result = self.call_TR_list_finished()
        elif interface == 'IF.TR.list.canceled':
            result = self.call_TR_list_canceled()
        elif interface == 'IF.TR.list.ongoingEID':
            result = self.call_TR_ongoing_eid_list()
        elif interface == 'IF.TR.production.record':
            result = self.call_TR_production_record(parameter)
        elif interface == 'IF.TR.production.retrieveVolume':
            result = self.call_TR_production_retrieve_volume(parameter)
        elif interface == 'IF.TR.production.retrieveHistory':
            result = self.call_TR_production_retrieve_history(parameter)
        elif interface == 'IF.TR.production.retrieveTotalVolume':
            result = self.call_TR_production_retrieve_total_volume()
        elif interface == 'IF.TR.contractMsg':
            result = self.call_TR_contract_msg(parameter)

        return result

    # error code section: 100
    def call_ID_onboard(self, _params: dict) -> dict:
        return {
            "type": "RES",
            "interface": "IF.ID.onboard",
            "parameter": "True"
        }

    # error code section: 200
    def call_ID_create(self) -> dict:
        set_call = {"name": "create_eid", "params": {"_pubkey": self.get_BIpubkey()}}
        result = self.rpcm.setMethod(set_call, "DIR")

        eid = ''
        error_code = 0

        if result["status"] == "success":
            # list-typed result[message] is considered
            id = re.findall(r'eid:[\w\d:]+', str(result["message"]))[0]
            # eid = id.replace('eid', 'id')
            eid = id
            print(f'created id ==> {eid}')
        else:
            if result["message"]["message"] == 'User(3)':
                error_code = 113  # ID already created
            else:
                error_code = 119  # general error

        return {
            "type": "RES",
            "interface": "IF.ID.create",
            "parameter": {"eid": eid},
            "errno": str(error_code)
        }

    # error code section: 300
    def call_ID_retrieve(self) -> dict:
        get_call = {"name": "get_eid_by_address", "params": {"_address": self.get_BIaddress()}}
        result = self.rpcm.getMethod(get_call, "DIR")

        eid = ''
        error_code = 0

        if result.startswith('{"eid"'):
            id = re.findall(r'eid:[\w\d:]+', result)[0]
            # eid = id.replace('eid', 'id')
            eid = id
            print(f'retrieved id ==> {eid}')
        elif int(result) > 0:
            error_code = 300 + int(result)  # 305: no id for this BI

        print(eid)
        return {
            "type": "RES",
            "interface": "IF.ID.retrieve",
            "parameter": {"eid": eid},
            "errno": str(error_code)
        }

    def call_ID_document(self, _params: str) -> dict:
        error_code = 0
        params_json = {}
        result = ""
        result_json = {}

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        if "eid" in params_json:
            get_call = {"name": "get_doc_by_eid", "params": {"_eid": params_json["eid"]}}
            result = self.rpcm.getMethod(get_call, "DIR")
        else:
            error_code = 401  # invalid parameters

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        print(result_json)

        eid_document = result_json["eid_document"]

        return {
            "type": "RES",
            "interface": "IF.ID.retrieve",
            "parameter": {"eid_document": eid_document},
            "errno": str(error_code)
        }

    def call_ID_regist(self, _params: str) -> dict:
        pass

    # error code section: 400
    def call_TR_offer(self, _params: str) -> dict:
        result = {}
        deal_id = ''
        error_code = 0

        try:
            params = json.loads(_params)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        if ("price" in params) and ("quantity" in params):
            set_call = {"name": "register_deal", "params": {"_price": params["price"], "_kwh": params["quantity"]}}
            result = self.rpcm.setMethod(set_call, "PTM")
        else:
            print(f"incompatible parameters ==> {params}")
            result["status"] = "failure"
            error_code = 401  # invalid parameters

        if result["status"] == "success":
            # list-typed result[message] is considered

            print(result["message"])
            # id = re.findall(r'Registered Deal::[\w\d]+', str(result["message"]))[0]

            # deal_id = id.replace('Registered Deal::', "id:deal:")
            deal_id = result["message"][0]
            print(f'new deal id ==> {deal_id}')
        else:
            if error_code == 0:
                error_code = 404  # only one deal(offer) is allowed, request for more is rejected

        return {
            "type": "RES",
            "interface": "IF.TR.offer",
            "parameter": {"deal_id": deal_id},
            "errno": str(error_code)
        }

    # error code section: 500
    def call_TR_order(self, _params: str) -> dict:
        result = {}
        output = False
        error_code = 0

        try:
            params = json.loads(_params)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        if ("deal" in params) and ("quantity" in params) and ("price" in params):
            set_call = {"name": "request_deal",
                        "params": {"_deal_id": params["deal"], "_price": params["price"], "_kwh": params["quantity"]}}
            result = self.rpcm.setMethod(set_call, "PTM")

            if result["status"] == "success":
                output = True
            else:
                error_code = 504  # order(request)ing more than two deals is not allowed
        else:
            error_code = 501  # invalid parameters

        return {
            "type": "RES",
            "interface": "IF.TR.order",
            "parameter": {"result": output},
            "errno": str(error_code)
        }

    # error code section: 800
    def call_TR_accept(self, _params: str) -> dict:
        error_code = 0
        output = False

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        if "order" in params_json:
            set_call = {"name": "accept_deal", "params": {"_eid": params_json["order"]}}
            result = self.rpcm.setMethod(set_call, "PTM")

            if result["status"] == "success":
                output = True
            else:
                output = False
                error_code = 801  # invalid deal id
        else:
            error_code = 800 + params_json

        return {
            "type": "RES",
            "interface": "IF.TR.accept",
            "parameter": {"result": output},
            "errno": str(error_code)
        }

    # error code section: 1000
    def call_TR_finish(self) -> dict:
        output = False
        error_code = 0

        set_call = {"name": "complete_deal"}
        result = self.rpcm.setMethod(set_call, "PTM")

        if result["status"] == "success":
            output = True
        else:
            error_code = 1016  # code 0x20, message: User(10)

        # if "deal" in params_json:
        #     set_call = {"name": "complete_deal"}
        #     result = self.rpcm.setMethod(set_call, "PTM")
        #
        #     # in case of result["status"] == "failure", result["message"] = {'code': '0x2a', 'message': 'User(10)'}
        #     if result["status"] == "success":
        #         output = 'True'
        #     else:
        #         error_code = 1016  # code: 0x20, message: User(10)
        # else:
        #     error_code = 1001  # invalid parameters

        return {
            "type": "RES",
            "interface": "IF.TR.finish",
            "parameter": {"result": output},
            "errno": str(error_code)
        }

    # error code section: 1300
    def call_TR_cancel_offer(self) -> dict:
        result = {}
        error_code = 0

        # try:
        #     params_json = json.loads(_params)
        # except json.JSONDecodeError as err:
        #     print(f'Error loading JSON: {err.msg}')

        set_call = {"name": "cancel_registered_deal"}
        result = self.rpcm.setMethod(set_call, "PTM")

        # if "deal" in params_json:
        #     set_call = {"name": "cancel_registered_deal"}
        #     result = self.rpcm.setMethod(set_call, "PTM")
        # else:
        #     result["status"] = "failure"
        #     error_code = 1301  # invalid parameters

        if result["status"] == "success":
            output = True
            print(result["message"])
        else:
            output = False
            error_code = 1302  # failed to cancel the deal due to ownership or non-existing deal etc.

        return {
            "type": "RES",
            "interface": "IF.TR.cancel.offer",
            "parameter": {"result": output},
            "errno": str(error_code)
        }

    # error code section: 1400
    def call_TR_cancel_order(self) -> dict:
        result = {}
        error_code = 0

        set_call = {"name": "cancel_requested_deal"}
        result = self.rpcm.setMethod(set_call, "PTM")

        if result["status"] == "success":
            output = True
            print(result["message"])
        else:
            output = False
            error_code = 1302  # failed to cancel the deal due to ownership or non-existing deal etc.

        return {
            "type": "RES",
            "interface": "IF.TR.cancel.order",
            "parameter": {"result": output},
            "errno": str(error_code)
        }

    def call_TR_cancel_accept(self) -> dict:
        result = {}
        error_code = 0

        set_call = {"name": "cancel_accepted_deal"}
        result = self.rpcm.setMethod(set_call, "PTM")

        if result["status"] == "success":
            output = True
            print(result["message"])
        else:
            output = False
            error_code = 1302  # failed to cancel the deal due to ownership or non-existing deal etc.

        return {
            "type": "RES",
            "interface": "IF.TR.cancel.accept",
            "parameter": {"result": output},
            "errno": str(error_code)
        }

    def call_TR_browse_deal_info(self, _params: str) -> dict:
        error_code = 0
        params_json = {}
        result = ""
        result_json = {}

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        if "deal_id" in params_json:
            get_call = {"name": "get_deal_info",
                        "params": {"_deal_id": params_json["deal_id"]}}
            result = self.rpcm.getMethod(get_call, "PTM")
        else:
            error_code = 401  # invalid parameters

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        print(result_json)

        deal_info = result_json["deal_info"]

        return {
            "type": "RES",
            "interface": "IF.ID.retrieve",
            "parameter": {"deal_info": deal_info},
            "errno": str(error_code)
        }

    def call_TR_browse_ongoing_deal_id(self, _params: str) -> dict:
        error_code = 0
        params_json = {}
        result = ""
        result_json = {}

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        if "eid" in params_json:
            get_call = {"name": "get_ongoing_deal_id_by_eid",
                        "params": {"_eid": params_json["eid"]}}
            result = self.rpcm.getMethod(get_call, "PTM")
        else:
            error_code = 401  # invalid parameters

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        ongoing_deal_id = result_json["ongoing_deal_id"]

        return {
            "type": "RES",
            "interface": "IF.ID.retrieve",
            "parameter": {"ongoing_deal_id": ongoing_deal_id},
            "errno": str(error_code)
        }


    def call_TR_browse_deal_id_buyer(self, _params: str) -> dict:
        error_code = 0
        params_json = {}
        result = ""
        result_json = {}

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        if "eid" in params_json:
            get_call = {"name": "get_registered_deal_id_by_requester_eid",
                        "params": {"_eid": params_json["eid"]}}
            result = self.rpcm.getMethod(get_call, "PTM")
        else:
            error_code = 401  # invalid parameters

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        registered_deal_id = result_json["registered_deal_id"]

        return {
            "type": "RES",
            "interface": "IF.ID.retrieve",
            "parameter": {"registered_deal_id": registered_deal_id},
            "errno": str(error_code)
        }

    def call_TR_list_ordered(self, _params: str) -> dict:
        error_code = 0
        params_json = {}
        result = ""
        result_json = {}

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        if "deal_id" in params_json:
            get_call = {"name": "get_requested_deal_info_list_by_deal_id",
                        "params": {"_deal_id": params_json["deal_id"]}}
            result = self.rpcm.getMethod(get_call, "PTM")
        else:
            error_code = 401  # invalid parameters

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        print(result_json)

        requested_deal_info_list = result_json["requested_deal_info_list"]

        return {
            "type": "RES",
            "interface": "IF.ID.retrieve",
            "parameter": {"requested_deal_info_list": requested_deal_info_list},
            "errno": str(error_code)
        }

    def call_TR_list_offered(self) -> dict:
        error_code = 0
        result_json = {}

        get_call = {"name": "get_registered_deal_info_list", "params": {}}
        result = self.rpcm.getMethod(get_call, "PTM")

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        # print(deal_list)
        deal_list = result_json["registered_deal_info_list"]
        return {
            "type": "RES",
            "interface": "IF.TR.browse",
            "parameter": {"registered_deal_info_list": deal_list},
            "errno": str(error_code)
        }

    def call_TR_list_accepted(self) -> dict:
        error_code = 0
        result_json = {}

        get_call = {"name": "get_accepted_deal_info_list", "params": {}}
        result = self.rpcm.getMethod(get_call, "PTM")

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        # print(deal_list)
        deal_list = result_json["accepted_deal_info_list"]
        return {
            "type": "RES",
            "interface": "IF.TR.browse",
            "parameter": {"accepted_deal_info_list": deal_list},
            "errno": str(error_code)
        }

    def call_TR_list_finished(self) -> dict:
        error_code = 0
        result_json = {}

        get_call = {"name": "get_completed_deal_info_list", "params": {}}
        result = self.rpcm.getMethod(get_call, "PTM")

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        # print(deal_list)
        deal_list = result_json["completed_deal_info_list"]
        return {
            "type": "RES",
            "interface": "IF.TR.browse",
            "parameter": {"completed_deal_info_list": deal_list},
            "errno": str(error_code)
        }

    def call_TR_list_canceled(self) -> dict:
        error_code = 0
        result_json = {}

        get_call = {"name": "get_canceled_deal_info_list", "params": {}}
        result = self.rpcm.getMethod(get_call, "PTM")

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        # print(deal_list)
        deal_list = result_json["canceled_deal_info_list"]
        return {
            "type": "RES",
            "interface": "IF.TR.browse",
            "parameter": {"canceled_deal_info_list": deal_list},
            "errno": str(error_code)
        }

    def call_TR_ongoing_eid_list(self) -> dict:
        deal_list = []
        error_code = 0

        get_call = {"name": "get_ongoing_eid_list", "params": {}}
        result = self.rpcm.getMethod(get_call, "PTM")

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        # print(deal_list)
        ongoing_eid_list = result_json["ongoing_eid_list"]
        return {
            "type": "RES",
            "interface": "IF.TR.browse",
            "parameter": {"ongoing_eid_list": ongoing_eid_list},
            "errno": str(error_code)
        }

    def call_TR_production_record(self, _params: str) -> dict:
        error_code = 0
        output = False

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        if "kwh" in params_json and "time" in params_json:
            set_call = {"name": "record_power_production",
                        "params": {"_kwh": params_json["kwh"], "_time": params_json["time"]}}
            result = self.rpcm.setMethod(set_call, "PGM")

            if result["status"] == "success":
                output = True
            else:
                output = False
                error_code = 801  # invalid deal id
        else:
            error_code = 800 + params_json

        return {
            "type": "RES",
            "interface": "IF.TR.production.record",
            "parameter": {"result": output},
            "errno": str(error_code)
        }

    def call_TR_production_retrieve_volume(self, _params: str) -> dict:
        error_code = 0
        params_json = {}
        result = ""
        result_json = {}

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        if "eid" in params_json:
            get_call = {"name": "get_total_production_by_eid",
                        "params": {"_eid": params_json["eid"]}}
            result = self.rpcm.getMethod(get_call, "PGM")
        else:
            error_code = 401  # invalid parameters

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        eid_total_production = result_json["eid_total_production"]

        return {
            "type": "RES",
            "interface": "IF.TR.production.retrieveVolume",
            "parameter": {"eid_total_production": eid_total_production},
            "errno": str(error_code)
        }

    def call_TR_production_retrieve_history(self, _params: str) -> dict:
        error_code = 0
        params_json = {}
        result = ""
        result_json = {}

        try:
            params_json = json.loads(_params)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        if "eid" in params_json:
            get_call = {"name": "get_production_history_by_eid",
                        "params": {"_eid": params_json["eid"]}}
            result = self.rpcm.getMethod(get_call, "PGM")
        else:
            error_code = 401  # invalid parameters

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as json_err:
            print(f'Error loading JSON: {json_err.msg}')

        production_history = result_json["production_history"]

        return {
            "type": "RES",
            "interface": "IF.TR.production.retrieveHistory",
            "parameter": {"production_history": production_history},
            "errno": str(error_code)
        }

    def call_TR_production_retrieve_total_volume(self) -> dict:
        error_code = 0
        result_json = {}

        get_call = {"name": "get_total_production", "params": {}}
        result = self.rpcm.getMethod(get_call, "PGM")

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError as err:
            print(f'Error loading JSON: {err.msg}')

        # print(deal_list)
        total_production = result_json["total_production"]

        return {
            "type": "RES",
            "interface": "IF.TR.browse",
            "parameter": {"total_production": total_production},
            "errno": str(error_code)
        }

    def call_TR_contract_msg(self, _params: str) -> dict:
        pass


# Blockchain Interface (BI), acting as a server, receives request from PTM
if __name__ == "__main__":
    backlog = 5
    config = open("config.json").read()

    try:
        config_in_json = json.loads(config)
    except json.JSONDecodeError as err:
        print(f'Error loading JSON: {err.msg}')

    #    test_set_call = {"name": "create_eid", "params": {"_pubkey": dispatcher.get_pubkey()}}
    #    dispatcher.rpcm.setMethod(test_set_call)
    #    test_get_call = {"name": "get_eid_by_address", "params": {"_address": dispatcher.get_address()}}
    #    dispatcher.rpcm.getMethod(test_get_call)

    # dispatcher.call_ID_create()
    # dispatcher.call_ID_retrieve()
    # dispatcher.call_TR_offer('{"price":"50", "quantity":"200", "hour":"1"}')
    # dispatcher.call_TR_order('{"deal":"0xccf4146f46d9fcb4474a4c4b356aa165d41af9c1d0284a1ab431f0d8945b06a2", "quantity":"10"}')
    # dispatcher.call_TR_browse_offer_list()
    # dispatcher.call_TR_browse_order_list('{"deal":"0xccf4146f46d9fcb4474a4c4b356aa165d41af9c1d0284a1ab431f0d8945b06a2"}')

    # dispatcher.call_TR_accept('{"deal": "0xccf4146f46d9fcb4474a4c4b356aa165d41af9c1d0284a1ab431f0d8945b06a2", "order": "eid:bems:4ebd680f2cc1f76bdf65b5b2c2afc0d64c553279"}')
    # dispatcher.call_TR_check('{"deal": "0xccf4146f46d9fcb4474a4c4b356aa165d41af9c1d0284a1ab431f0d8945b06a2"}')

    # dispatcher.call_TR_ongoing_list()
    # dispatcher.call_TR_finish('{"deal": "0xccf4146f46d9fcb4474a4c4b356aa165d41af9c1d0284a1ab431f0d8945b06a2"}')

    # dispatcher.call_TR_cancel_offer('{"deal": "0x07a27baa8660502127b298f1c2137f96786f355e5b2c08c0eb6e010008a33a57"}')
    #     self.socket.bind(('', port))
    #     self.socket.listen(self.backlog)

    port = config_in_json["BI Server Port"]
    socket = socket(AF_INET, SOCK_STREAM)
    socket.bind(('', port))
    socket.listen(backlog)

    while True:
        client, client_addr = socket.accept()

        dispatcher = Dispatcher(config_in_json)
        server = ServerThread(client, dispatcher)
        server.start()
