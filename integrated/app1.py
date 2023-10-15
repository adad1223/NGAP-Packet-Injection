from flask import Flask, request,redirect,flash
import pyshark
from flask_cors import CORS, cross_origin
from app2 import *
from urllib.parse import parse_qs
import requests
import json
from scapy.all import *
from pycrate_asn1rt.utils import *
from final import final_decode,value,update_list
from getting_nas import gettingNAS,updatingNAS,getting_msg_type
from big_numbers import checking_for_big_nos,converting_string_to_int,checking_mandatory_fields
from pycrate_mobile.NAS5G import *
from pycrate_mobile.NAS import *
from pycrate_asn1dir import NGAP
from new import getting_packet_attr
app1= Flask(__name__)
CORS(app1, support_credentials=True)
a=None
def convert_strings_to_bytes(i):
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
    c = pyshark.FileCapture("ui.pcap",display_filter='ngap', use_json=True, include_raw=True)
    my_packets = c[i]
    scapy_packet = IP(my_packets.get_raw_packet())
    raw_data = scapy_packet[SCTPChunkData].data
    x = NGAP.NGAP_PDU_Descriptions.NGAP_PDU
    x.from_aper(raw_data)
    z=x.get_val()
    ngap_messages = convert_bytes_to_strings(z[1])
    json_string = json.dumps(ngap_messages)
    c.close()
    return json_string
ngapMessage = None
@app1.before_request
#@cross_origin(supports_credentials=True)
def load_ngap_message():
    global ngapMessage
    # checking_for_big_nos()
    with open('./integrated/packet.json', 'r') as f:
        ngapMessage = json.load(f)
    f.close()
    # def convert_to_bytes(js,par,val):
    #     if isinstance(js, dict):

    #         for key, value in js.items():
    #             if(key=='pDUSessionNAS-PDU'):
    #                 val=value
    #             val = convert_to_bytes(value,js,val)
    #     elif isinstance(js, list):
    #         # print(js[0])
    #         for i, item in enumerate(js):
    #             print(item)
    #             val = convert_to_bytes(item,js,val)
    #     # elif isinstance(js, str):
    #         # if(js=='NAS-PDU'):
    #             # val=par[1]
    #         # elif(js=='pDUSessionNAS-PDU'):
    #         #     print(par)
            
    #     return val
    # val = convert_to_bytes(ngapMessage,None,val)
    # print(val)
@app1.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def index():
    # flash('This is a flash message')
    return '''
    <!DOCTYPE html>
    <html>
    <head>
    
    <title>5G Network Monitoring</title>
    <body>
    <h1>5G Network Monitoring</h1>
    <a href="/integrated">Select the packet number required to edit</a><br>
    <a href="/process_header">Modify the selected packet</a><br>
    </body>
    </html>
    '''
a=5
print(ngapMessage)
@app1.route('/integrated', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def integrated():
    global a
    if request.method == 'POST':
        # packet_number = request.form['packet_number']
        data = request.args
        print(data)
        index = data.get('index')
        a=index
        # form_data = data.decode('utf-8') 
        # parsed_data = parse_qs(data)
        # packet_number = parsed_data.get('listItem', [None])[0]
        # print(packet_number)
        # print(packet_number)
        # # print(type(packet_number))
        packet_number=a
        packet_number=int(packet_number)
        # packet_number=int(packet_number)
        with open('./integrated/1.txt', 'w') as f:
            f.write(a)
        js=convert_strings_to_bytes((packet_number))
        js=json.loads(js)
        print(type(js))
        with open('./integrated/packet.json', 'w') as f:
            print(js)
            json.dump(js, f,ensure_ascii=False)
        f.close()

        return js


    else:
        lst=getting_packet_attr()
        return lst

@app1.route('/process_header', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def process_header():
    print(ngapMessage)
    if request.method == 'POST':
        try:
            d = pyshark.FileCapture("ui.pcap",display_filter='ngap', use_json=True, include_raw=True)
            with open('./integrated/1.txt', 'r') as f:
                x=f.read()
                x=int(x)
            my_packet = d[x]
            js = request.get_json()
            print(js)
            # print(js)
            js=converting_string_to_int(js)
            scapy_packet = IP(my_packet.get_raw_packet())
            x = NGAP.NGAP_PDU_Descriptions.NGAP_PDU
            x.from_aper(scapy_packet[SCTPChunkData].data)
            z=x.get_val()
            hey=[None]*2
            hey[0]=z[0]
            hey[1]=z[1]
            print(z[1])
            print("\n")
            print("\n")
            js=convert_to_bytes(js)
            js=change_data_structures(js,hey[1])
            print(js)
            init_msg_pdu_modify_req=NGAP.NGAP_PDU_Descriptions.SuccessfulOutcome
            try:
                init_msg_pdu_modify_req.set_val(js)
            except Exception as e:
                init_msg_pdu_modify_req = NGAP.NGAP_PDU_Descriptions.InitiatingMessage
                init_msg_pdu_modify_req.set_val(js)
            buf=init_msg_pdu_modify_req.to_aper()
            buf=b'\x00'+buf
            print(buf)
            scapy_packet[SCTPChunkData].data=buf
            scapy_packet[IP].dst="192.168.100.114"
            send(scapy_packet)
            
            # print(oo)
            d.close()
            return "Packet Sent"
        
        except Exception as e:
            print(e)
            print("hello")
            return 'Error In the changes you made'
    elif request.method=='GET':
            ngapMessage=checking_for_big_nos()
            mandatedic=checking_mandatory_fields()
            
            return [json.dumps(ngapMessage),json.dumps(mandatedic)]
@app1.route('/save', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def save():
    if request.method=='POST':
        d = pyshark.FileCapture("ui.pcap",display_filter='ngap', use_json=True, include_raw=True)
        with open('./integrated/1.txt', 'r') as f:
            x=f.read()
            x=int(x)
        my_packet = d[x]
        js = request.get_json()
        scapy_packet = IP(my_packet.get_raw_packet())
        x = NGAP.NGAP_PDU_Descriptions.NGAP_PDU
        x.from_aper(scapy_packet[SCTPChunkData].data)
        z=x.get_val()
        hey=[None]*2
        hey[0]=z[0]
        hey[1]=z[1]
        print(z[1])
        print("\n")
        print(js)
        print("\n")
        js=convert_to_bytes(js)
        js=change_data_structures(js,hey[1])
        print(js)
        init_msg_pdu_modify_req=NGAP.NGAP_PDU_Descriptions.SuccessfulOutcome
        try:
            init_msg_pdu_modify_req.set_val(js)
        except Exception as e:
            init_msg_pdu_modify_req = NGAP.NGAP_PDU_Descriptions.InitiatingMessage
            init_msg_pdu_modify_req.set_val(js)
        buf=init_msg_pdu_modify_req.to_aper()
        buf=b'\x00'+buf
        print(buf)
        scapy_packet[SCTPChunkData].data=buf
        scapy_packet[IP].dst="192.168.100.114"
        wrpcap("Saved_Modified_Packets.pcap",scapy_packet,append=True)
        # wrpcap("Saved_Modified_Packets.pcap",scapy_packet)
        d.close()
        print("Packet Saved")

        return "Saved"
    elif request.method=='GET':
        return 'Saved'

@app1.route('/recievebytes', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def recievebytes():
    if request.method=='POST':
        nasby=request.get_json()
        nasby=nasby['data']
        print(nasby)
        u=nasby.encode('utf-8')
        string_value = u.decode('unicode_escape')
        nasby=string_value
        ngapMessage1=final_decode(nasby)
        return ngapMessage1        
@app1.route('/decode', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def decode():
    global a
    with open('./integrated/packet.json', 'r') as f:
            ngapMessage = json.load(f)
    # ngapMessage=checking_for_big_nos()
    # f.close()
    # print(ngapMessage)
    nasby=gettingNAS(ngapMessage)
    ngapMessage1=final_decode(nasby)
    # print(ngapMessage1)

    if request.method=='GET':
        return ngapMessage1
#             return '''

#      <!DOCTYPE html>
# <html>
# <head>
#     <title>NGAP Message</title>
# </head>
# <body>
#     <h1>NGAP Message</h1>
#     <div id="ngap-message"></div>
#     <script>
#  const ngapMessage = ''' + (ngapMessage1) + ''';

# function displayObject(obj, container, parentObj, parentKey) {
#     if (typeof obj === "object") {
#         const table = document.createElement('table');
#         table.border = '1';
#         for (const key in obj) {
#             const tr = document.createElement('tr');
#             const th = document.createElement('th');
#             th.textContent = key;
#             tr.appendChild(th);
#             const td = document.createElement('td');
#             displayObject(obj[key], td, obj, key);
#             tr.appendChild(td);
#             table.appendChild(tr);
#         }
#         container.appendChild(table);
#     } else if (Array.isArray(obj)) {
#         const ul = document.createElement('ul');
#         for (let i = 0; i < obj.length; i++) {
#             const li = document.createElement('li');
#             displayObject(obj[i], li, obj, i);
#             ul.appendChild(li);
#         }
#         container.appendChild(ul);
#     } else {
#         const input = document.createElement('input');
#         input.type = 'text';
#         input.value = obj;
#         input.addEventListener('input', function() {
#             if (typeof obj === 'number') {
#                 parentObj[parentKey] = Number(this.value);
#             } else {
#                 parentObj[parentKey] = this.value;
#             }
#         });
#         container.appendChild(input);
#     }
# }
#     const container = document.getElementById('ngap-message');
#     displayObject(ngapMessage, container, ngapMessage, 'ngapMessage');

#     </script>
#     <button id='btn'>Submit</button>
#         <button id=btn1>
#     <a href="/process_header">Go Back</a>
# </button>
#     <script>
#     const submitButton = document.getElementById('btn');
#     submitButton.addEventListener('click', function() {
#     fetch('http://127.0.0.1:5002/decode', {
#         method: 'POST',
#         headers: {
#             'Content-Type': 'application/json'
#         },
#         body: JSON.stringify(ngapMessage)
#     }).then(response=>response.text()).then(data=>alert(data));
# });
#     </script>
# </body>
# </html>
# '''
    elif request.method=="POST":
        with open('./integrated/packet.json', 'r') as f:
            ngapMessage = json.load(f)
        nasby=gettingNAS(ngapMessage)
        u=nasby.encode('latin-1')
        string_value = u.decode('unicode_escape')
        u=string_value.encode('latin-1')
        nasby=u
        # print(nasby)
        msg,err =parse_NAS5G(nasby)
        a=None
        try:
            print(msg[3].get_val())
            y=(msg[3].get_val())
            Msg, err = parse_NAS5G(y)
            a=True
            if Msg==None:
                a=False
                Msg=msg

            print("\n")

        except Exception as e:
            print("hey")
            a=False
            Msg=msg
            print(e)
            print("NO Encrypted message")
            pass
        js = request.get_json()
        print("\n")
        js=convert_to_bytes(js)
        p=[]
        value(js,p)
        valuest=Msg.get_val()
        update_list(p,valuest)
        Msg.set_val(valuest)
        b=Msg.to_bytes()
        if a:
            msg[3].set_val(b)
        else:
            msg.set_val(valuest)
        print(msg.to_bytes())
        a=msg.to_bytes()
        a=repr(a)[2:-1]
        ngapMessage=updatingNAS(ngapMessage,a)
        with open('./integrated/packet.json', 'w') as f:
            json.dump(ngapMessage, f,ensure_ascii=False)
        f.close()
        return "Packet Decoded Successfully"
        # return a
# @app1.route('/', methods=['POST'])
# def handle_post():
#     print(ngapMessage)
#     if request.method == 'POST':
#         try:
#             d = pyshark.FileCapture("ui.pcap",display_filter='ngap', use_json=True, include_raw=True)
#             with open('./integrated/1.txt', 'r') as f:
#                 x=f.read()
#                 x=int(x)
#             my_packet = d[x]
#             js = request.get_json()
#             print(js)
#             # print(js)
#             js=converting_string_to_int(js)
#             scapy_packet = IP(my_packet.get_raw_packet())
#             x = NGAP.NGAP_PDU_Descriptions.NGAP_PDU
#             x.from_aper(scapy_packet[SCTPChunkData].data)
#             z=x.get_val()
#             hey=[None]*2
#             hey[0]=z[0]
#             hey[1]=z[1]
#             print(z[1])
#             print("\n")
#             print("\n")
#             js=convert_to_bytes(js)
#             js=change_data_structures(js,hey[1])
#             print(js)
#             init_msg_pdu_modify_req=NGAP.NGAP_PDU_Descriptions.SuccessfulOutcome
#             try:
#                 init_msg_pdu_modify_req.set_val(js)
#             except Exception as e:
#                 init_msg_pdu_modify_req = NGAP.NGAP_PDU_Descriptions.InitiatingMessage
#                 init_msg_pdu_modify_req.set_val(js)
#             buf=init_msg_pdu_modify_req.to_aper()
#             buf=b'\x00'+buf
#             print(buf)
#             scapy_packet[SCTPChunkData].data=buf
#             scapy_packet[IP].dst="192.168.100.114"
#             send(scapy_packet)
            
#             # print(oo)
#             d.close()
#             return "Packet Sent"
        
#         except Exception as e:
#             print(e)
#             print("hello")
#             return 'Error In the changes you made'
if __name__ == '__main__':
        
        app1.run(host='127.0.0.1', port=5002)

