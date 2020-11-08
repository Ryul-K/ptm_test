from time import sleep

from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
import json


class RPCmanager(object):
    def __init__(self, _conf_rpc: dict) -> None:
        # Key Wallet with Password
        self.key_wallet = KeyWallet.load(_conf_rpc["KeyWallet"]["File"], _conf_rpc["KeyWallet"]["Password"])
        # Service Endpoint (URL)
        self.service_endpoint = IconService(HTTPProvider(_conf_rpc["Service Endpoint"]))
        # Smart Contract Address
        self.id_contract_address = _conf_rpc["ID Contract Address"]
        self.ptm_contract_address = _conf_rpc["PTM Contract Address"]
        self.pgm_contract_address = _conf_rpc["PGM Contract Address"]
        # Network ID
        self.nid = int(_conf_rpc["Network ID"])

    def getMethod(self, _method: dict, type: str) -> str:
        if type == "DIR":
            contract_address = self.id_contract_address
        elif type == "PTM":
            contract_address = self.ptm_contract_address
        elif type == "PGM":
            contract_address = self.pgm_contract_address
        else:
            print("Not supported contract type")
            pass

        call = CallBuilder() \
            .from_(self.key_wallet.get_address()) \
            .to(contract_address) \
            .method(_method["name"]) \
            .params(_method["params"]) \
            .build()

        result = self.service_endpoint.call(call)
        print(result)

        return result

    def setMethod(self, _method: dict, type: str) -> dict:
        result = {}
        if type == "DIR":
            contract_address = self.id_contract_address
        elif type == "PTM":
            contract_address = self.ptm_contract_address
        elif type == "PGM":
            contract_address = self.pgm_contract_address
        else:
            print("Not supported contract type")
            result["status"] = "failure"
            result["message"] = ""
            return result

        if not _method.__contains__("params"):
            _method["params"] = ""

        transaction = CallTransactionBuilder() \
            .from_(self.key_wallet.get_address()) \
            .to(contract_address) \
            .step_limit(10000000) \
            .nid(self.nid) \
            .method(_method["name"]) \
            .params(_method["params"]) \
            .build()



        # sign the transaction with key wallet
        signed_tx = SignedTransaction(transaction, self.key_wallet)
        # commit(send) the signed transaction to the service endpoint
        tx_hash = self.service_endpoint.send_transaction(signed_tx)
        sleep(3)  # wait a second for the transaction to be finalized
        tx_result = self.service_endpoint.get_transaction_result(tx_hash)
        print(tx_result)

        if "failure" in tx_result:
            result["status"] = "failure"
            result["message"] = tx_result["failure"]
        else:
            result["status"] = "success"
            result["message"] = tx_result["eventLogs"][0]["data"]

        return result


if __name__ == "__main__":
    rpcm = RPCmanager("config.json")

    test_get_call = {"name": "get_did_by_address", "params": {"_address": rpcm.key_wallet.get_address()}}
    rpcm.getMethod(test_get_call)
#    test_set_call = {"name": "create_did", "params":{"_pubkey": key_wallet.public_key.hex()}}
#    rpcm.setMethod(test_set_call)
