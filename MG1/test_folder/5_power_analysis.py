import requests, json, time

headers = {'Content-Type': 'application/json; charset=utf-8'} # cookies = {'session_id': 'sorryidontcare'}
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

ems_Data_json = {
    "device" : {
        "url" : "/ddevice/device",
        "rq_param_device" : "INV",
        "rq_param_tpm_id" : "5",
        "rq_param_send_time":"20190930153015110"
        },
    "regist" : {
        "url" : "/m_id_regist",
        "rq_param_target" : "EMS",
        "rq_param_type" : "REQ",
        "rq_param_interface" : "IF.ID.regist",
        "rq_param_parameter" : "id:bems:dc5f5ca3959409c3292f44e942b9957dd2b4de6c"
        },
    "params" : {
        "url" : "/a_stateparams",
        "rq_param_target" : "EMS",
        "rq_param_type" : "REQ",
        "rq_param_interface" : "IF_STATE.stateParams",
        "rq_param_parameter" : "",
        "rq_param_time" : ""
        },
    "contractMsg" : {
        "url" : "/m_tr/contractMsg",
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

}
# a = str(time.time())[0:10]
# b = int(str(time.time())[0:10] + 300)
# print(a)
# print(b)

print('\033[32m' + '1.안녕' + '\033[0m')
# res = requests.post(url_params, headers=headers, data=json.dumps(data_params))
# print('\n status_code : ' + str(res.status_code))
# print(res.json())
# stateParams= res.json()
# stateOfcharge = stateParams['rs_stateParameter'][0]['stateOfcharge']
# genRatio = stateParams['rs_stateParameter'][0]['genRatio']
# lossRatio = stateParams['rs_stateParameter'][0]['lossRatio']
# print('\n SoC : ' + str(stateOfcharge))
# print('\n genRatio : ' + str(genRatio))
# print('\n lossRatio : ' + str(lossRatio))

######################################################
# res = requests.post(url_device, headers=headers, data=json.dumps(data_device))
# print('\n status_code : ' + str(res.status_code))
# print(res.json())
#
# res = requests.post(url_regist, headers=headers, data=json.dumps(data_regist))
# print('\n status_code : ' + str(res.status_code))
# print(res.json())



#
# res = requests.post(url_contractMsg, headers=headers, data=json.dumps(data_contractMsg))
# print('\n status_code : ' + str(res.status_code))
# print(res.json())

# res = requests.get(url_regist, headers=headers, cookies=cookies)

# res.request # 내가 보낸 request 객체에 접근 가능
# res.status_code # 응답 코드 res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동
# res.json() # json response일 경우 딕셔너리 타입으로 바로 변환

#PTM smartcontract address PTM 스마트컨트랙트 주소
# cxa11cadfb07f5bd947ff066ba580f89b90d606ea3 <- 사용
# cxfddf2eb24426b5801da640b8843d46b80df512d8 <- 사용
# cx5585cf31abeba2f124d0655ec3f6ca3a3b96c784 <- 사
# cx8a8d20c78cb6ffffbc89c3a2b13025015988b11f
# cx9e0a137dd3116a78750d0015691f5b231d85655f
