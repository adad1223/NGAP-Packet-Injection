import json
from pyshark_attr import NAS_ATTR
def getting_packet_attr():
    # def convert_strings_to_bytes(i):
    #     def convert_bytes_to_strings(obj):
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
#         c = pyshark.FileCapture("ui.pcap",display_filter='ngap', use_json=True, include_raw=True)
#         my_packets = c[i]
#         scapy_packet = IP(my_packets.get_raw_packet())

#         raw_data = scapy_packet[SCTPChunkData].data
# # ngap_messages = {'procedureCode': 46, 'criticality': 'ignore', 'value': ('UplinkNASTransport', {'protocolIEs': [{'id': 10, 'criticality': 'reject', 'value': ('AMF-UE-NGAP-ID', 1)}, {'id': 85, 'criticality': 'reject', 'value': ('RAN-UE-NGAP-ID', 1)}, {'id': 38, 'criticality': 'reject', 'value': ('NAS-PDU', b'~\x00W-\x10\xcb\xa3b\x8a\xb6\xe0P\x90\xee\x95\xad5~\xc4\\2')}, {'id': 121, 'criticality': 'ignore', 'value': ('UserLocationInformation', ('userLocationInformationNR', {'nR-CGI': {'pLMNIdentity': b'\x00\xf1\x10', 'nRCellIdentity': (16, 36)}, 'tAI': {'pLMNIdentity': b'\x00\xf1\x10', 'tAC': b'\x00\x00\x01'}, 'timeStamp': b'\xe8Q\x12%'}))}]})}
#         x = NGAP.NGAP_PDU_Descriptions.NGAP_PDU
#         x.from_aper(raw_data)
#         z=x.get_val()
#         ngap_messages = convert_bytes_to_strings(z[1])
#         json_string = json.dumps(ngap_messages)
#         c.close()
#         return json_string
    lst=[]

    # def call_back(my_packets,i):  
        # scapy_packet = IP(my_packets.get_raw_packet())
        # raw_data = scapy_packet[SCTPChunkData].data
        # x = NGAP.NGAP_PDU_Descriptions.NGAP_PDU
        # x.from_aper(raw_data)
        # z=x.get_val()
        # lst.append([z[1]['value'][0]])
    pp=NAS_ATTR()
    pp=json.dumps(pp)
    return pp
        
        # lst[i].append(pp[i])
    # c = pyshark.FileCapture("ui.pcap",display_filter='ngap', use_json=True, include_raw=True)
    # i=0
    # for packet in c:
    #     call_back(packet,i)
    #     i+=1
    # lst=json.dumps(lst)
    # c.close()
    # return lst

if __name__=="__main__":
    print(getting_packet_attr())
