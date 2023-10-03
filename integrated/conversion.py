# import jsonpickle
# import json

import json
def nested_list_to_json(data):
    def nested_list_to_json(data):
        if isinstance(data, list):
            if len(data) == 2 and isinstance(data[0], str):
                return {data[0]: nested_list_to_json(data[1])}
            else:
                return [nested_list_to_json(item) for item in data]
        else:
            return data

# Your data
# data = ["main", ["5GMMHeader ", ["EPD ", 126], ["spare ", 0], ["SecHdr ", 0], ["Type ", 94]], ["IMEISV ", ["T ", 119], ["L ", 9], ["5GSID ", ["Digit1 ", 4], ["Odd ", 0], ["Type ", 5], ["Digits ", "s\\x80a!\\x85aQ\\xf1"]]], ["NASContainer ", ["T ", 113], ["L ", 35], ["5GMMRegistrationRequest ", ["5GMMHeader ", ["EPD ", 126], ["spare ", 0], ["SecHdr ", 0], ["Type ", 65]], ["NAS_KSI ", ["NAS_KSI ", ["TSC ", 0], ["Value ", 7]]], ["5GSRegType ", ["5GSRegType ", ["FOR ", 1], ["Value ", 1]]], ["5GSID ", ["L ", 13], ["5GSID ", ["spare ", 0], ["Fmt ", 0], ["spare ", 0], ["Type ", 1], ["Value ", ["PLMN ", "\\x00\\xf1\\x10"], ["RoutingInd ", "\\x00\\x00"], ["spare ", 0], ["ProtSchemeID ", 0], ["HNPKID ", 0], ["Output ", "!Ce\\x87Y"]]]]], ["5GMMCap ", ["T ", 16], ["L ", 1], ["5GMMCap ", ["SGC ", 0], ["5G-HC-CP-CIoT ", 0], ["N3Data ", 0], ["5G-CP-CIoT ", 0], ["RestrictEC ", 0], ["LPP ", 0], ["HOAttach ", 0], ["S1Mode ", 0]]], ["UESecCap ", ["T ", 46], ["L ", 4], ["UESecCap "...
# 
# Convert to JSON

# Print JSON


    # data = ["main", ["5GMMHeader ", ["EPD ", 126], ["spare ", 0], ["SecHdr ", 0], ["Type ", 94]], ["IMEISV ", ["T ", 119], ["L ", 9], ["5GSID ", ["Digit1 ", 4], ["Odd ", 0], ["Type ", 5], ["Digits ", "s\\x80a!\\x85aQ\\xf1"]]], ["NASContainer ", ["T ", 113], ["L ", 35], ["5GMMRegistrationRequest ", ["5GMMHeader ", ["EPD ", 126], ["spare ", 0], ["SecHdr ", 0], ["Type ", 65]], ["NAS_KSI ", ["NAS_KSI ", ["TSC ", 0], ["Value ", 7]]], ["5GSRegType ", ["5GSRegType ", ["FOR ", 1], ["Value ", 1]]], ["5GSID ", ["L ", 13], ["5GSID ", ["spare ", 0], ["Fmt ", 0], ["spare ", 0], ["Type ", 1], ["Value ", ["PLMN ", "\\x00\\xf1\\x10"], ["RoutingInd ", "\\x00\\x00"], ["spare ", 0], ["ProtSchemeID ", 0], ["HNPKID ", 0], ["Output ", "!Ce\\x87Y"]]]]], ["5GMMCap ", ["T ", 16], ["L ", 1], ["5GMMCap ", ["SGC ", 0], ["5G-HC-CP-CIoT ", 0], ["N3Data ", 0], ["5G-CP-CIoT ", 0], ["RestrictEC ", 0], ["LPP ", 0], ["HOAttach ", 0], ["S1Mode ", 0]]], ["UESecCap ", ["T ", 46], ["L ", 4], ["UESecCap ", ["5G-EA0 ", 1], ["5G-EA1_128 ", 1], ["5G-EA2_128 ", 1], ["5G-EA3_128 ", 1], ["5G-EA4 ", 0], ["5G-EA5 ", 0], ["5G-EA6 ", 0], ["5G-EA7 ", 0], ["5G-IA0 ", 1], ["5G-IA1_128 ", 1], ["5G-IA2_128 ", 1], ["5G-IA3_128 ", 1], ["5G-IA4 ", 0], ["5G-IA5 ", 0], ["5G-IA6 ", 0], ["5G-IA7 ", 0], ["EEA0 ", 1], ["EEA1_128 ", 1], ["EEA2_128 ", 1], ["EEA3_128 ", 1], ["EEA4 ", 0], ["EEA5 ", 0], ["EEA6 ", 0], ["EEA7 ", 0], ["EIA0 ", 1], ["EIA1_128 ", 1], ["EIA2_128 ", 1], ["EIA3_128 ", 1], ["EIA4 ", 0], ["EIA5 ", 0], ["EIA6 ", 0], ["EIA7 ", 0]]], ["NSSAI ", ["T ", 47], ["L ", 2], ["NSSAI ", ["SNSSAI ", ["Len ", 1], ["SNSSAI ", ["SST ", 1]]]]], ["5GSUpdateType ", ["T ", 83], ["L ", 1], ["5GSUpdateType ", ["spare ", 0], ["EPS-PNB-CIoT ", 0], ["5GS-PNB-CIoT ", 0], ["NG-RAN-RCU ", 0], ["SMSRequested ", 0]]]]]
    json_data = nested_list_to_json(data)
    return(json.dumps(json_data, indent=4))


