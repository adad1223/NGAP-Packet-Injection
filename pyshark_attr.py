import pyshark
import json
def NAS_ATTR():
    capture = pyshark.FileCapture("ui.pcap", display_filter="ngap")
    packets_list = []
    for packet in capture:
        packet_dict = {
            'layers': {}
        }
        for layer in packet.layers:
            layer_dict = {}
            for field in layer.field_names:
                layer_dict[field] = layer.get_field_value(field)
            packet_dict['layers'][layer.layer_name] = layer_dict
        packets_list.append(packet_dict)
    with open('output.json', 'w') as f:
        json.dump(packets_list, f, indent=4)
    capture.close()
    FGMMdict= {
        65 : "Registration request",
        66 : "Registration accept",
        67 : "Registration complete",
        68 : "Registration reject",
        69 : "MO Deregistration request",
        70 : "MO Deregistration accept",
        71 : "MT Deregistration request",
        72 : "MT Deregistration accept",
        76 : "Service request",
        77 : "Service reject",
        78 : "Service accept",
        79 : "Control plane service request",
    # slice-specific auth
        80 : "Network slice-specific authentication command",
        81 : "Network slice-specific authentication complete",
        82 : "Network slice-specific authentication result",
    # common procedures
        84 : "Configuration update command",
        85 : "Configuration update complete",
        86 : "Authentication request",
        87 : "Authentication response",
        88 : "Authentication reject",
        89 : "Authentiction failure",
        90 : "Authentication result",
        91 : "Identity request",
        92 : "Identity response",
        93 : "Security mode command",
        94 : "Security mode complete",
        95 : "Security Mode reject",
    # misc
        100: "5GMM status",
        101: "Notification",
        102: "Notification response",
        103: "UL NAS transport",
        104: "DL NAS transport",
        193: "PDU session establishment request",
        194: "PDU session establishment accept",
        }
    li=[]
    with open('/Users/anishrishi/Documents/internship/output.json', 'r') as f:
        x = json.load(f)
    for i in x:
        b=list(i['layers']['ngap'].values())
        bb=(b[9])
        try:
            a=(i['layers']['ngap']['nas_5gs_mm_message_type'])
            try:
                l=(i['layers']['ngap']['nas_5gs_sm_message_type'])
                # print(l)
                li.append([b[9],FGMMdict[int(a,16)],FGMMdict[int(l,16)]])
            except:
                li.append([b[9],FGMMdict[int(a,16)]])

        except Exception as e:
            li.append([bb])
    
    return li
if __name__=="__main__":
    print(NAS_ATTR())



