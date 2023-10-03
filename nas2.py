import json

def nested(ol,lo):
    # print(ol)
    # print(lo)
    lo.insert(0,'main')
    count=-1
    def getList(ol):
        nonlocal count
        if(type(ol) is list):
            
            count+=1
            test=count
            newList=[]
            for i in ol:
                # if i==
                newList.append(getList(i))
            return [lo[test],newList]
        else:
            count+=1
            return [lo[count],ol]
    # ol=getList(ol)

    def convert_bytes_to_strings(obj):
        if isinstance(obj, bytes):
            return repr(obj)[2:-1]
        elif isinstance(obj, dict):
            return {k: convert_bytes_to_strings(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_bytes_to_strings(v) for v in obj]
        elif isinstance(obj, tuple):
            return tuple(convert_bytes_to_strings(v) for v in obj)
        else:
            return obj

    ol = getList(ol)
    ol=convert_bytes_to_strings(ol)
    json_str = json.loads(json.dumps(ol))
    return json_str

if __name__=="__main__":
    ol=(nested(ol,lo))
    print(ol)
    

# ol = [[126, 0, 0, 94], [119, 9, [4, 0, 5, b's\x80a!\x85aQ\xf1']], [113, 35, [[126, 0, 0, 65], [[0, 7]], [[1, 1]], [13, [0, 0, 0, 1, [b'\x00\xf1\x10', b'\x00\x00', 0, 0, 0, b'!Ce\x87Y']]], [16, 1, [0, 0, 0, 0, 0, 0, 0, 0]], [46, 4, [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]], [47, 2, [[1, [1]]]], [83, 1, [0, 0, 0, 0, 0]]]]]
# lo = ['5GMMHeader ', 'EPD ', 'spare ', 'SecHdr ', 'Type ', 'IMEISV ', 'T ', 'L ', '5GSID ', 'Digit1 ', 'Odd ', 'Type ', 'Digits ', 'NASContainer ', 'T ', 'L ', '5GMMRegistrationRequest ', '5GMMHeader ', 'EPD ', 'spare ', 'SecHdr ', 'Type ', 'NAS_KSI ', 'NAS_KSI ', 'TSC ', 'Value ', '5GSRegType ', '5GSRegType ', 'FOR ', 'Value ', '5GSID ', 'L ', '5GSID ', 'spare ', 'Fmt ', 'spare ', 'Type ', 'Value ', 'PLMN ', 'RoutingInd ', 'spare ', 'ProtSchemeID ', 'HNPKID ', 'Output ', '5GMMCap ', 'T ', 'L ', '5GMMCap ', 'SGC ', '5G-HC-CP-CIoT ', 'N3Data ', '5G-CP-CIoT ', 'RestrictEC ', 'LPP ', 'HOAttach ', 'S1Mode ', 'UESecCap ', 'T ', 'L ', 'UESecCap ', '5G-EA0 ', '5G-EA1_128 ', '5G-EA2_128 ', '5G-EA3_128 ', '5G-EA4 ', '5G-EA5 ', '5G-EA6 ', '5G-EA7 ', '5G-IA0 ', '5G-IA1_128 ', '5G-IA2_128 ', '5G-IA3_128 ', '5G-IA4 ', '5G-IA5 ', '5G-IA6 ', '5G-IA7 ', 'EEA0 ', 'EEA1_128 ', 'EEA2_128 ', 'EEA3_128 ', 'EEA4 ', 'EEA5 ', 'EEA6 ', 'EEA7 ', 'EIA0 ', 'EIA1_128 ', 'EIA2_128 ', 'EIA3_128 ', 'EIA4 ', 'EIA5 ', 'EIA6 ', 'EIA7 ', 'NSSAI ', 'T ', 'L ', 'NSSAI ', 'SNSSAI ', 'Len ', 'SNSSAI ', 'SST ', '5GSUpdateType ', 'T ', 'L ', '5GSUpdateType ', 'spare ', 'EPS-PNB-CIoT ', '5GS-PNB-CIoT ', 'NG-RAN-RCU ', 'SMSRequested ']
# lo.insert(0, 'main')
# j = k = 0

# def re(obj):
#     global j
#     global k
#     if isinstance(obj,list):
#         obj.insert(0, lo[j])
#         j += 1
#         for i in range(1,len(obj)):
#             if isinstance(obj[i], list):
#                 re(obj[i])
#             else:
#                 obj[i] = [lo[j], obj[i]]
#                 j += 1

# def convert_bytes_to_strings(obj):
#         if isinstance(obj, bytes):
#             return repr(obj)[2:-1]
#         elif isinstance(obj, dict):
#             return {k: convert_bytes_to_strings(v) for k, v in obj.items()}
#         elif isinstance(obj, list):
#             return [convert_bytes_to_strings(v) for v in obj]
#         elif isinstance(obj, tuple):
#             return tuple(convert_bytes_to_strings(v) for v in obj)
#         else:
#             return obj
    
# re(ol)
# # print(ol)