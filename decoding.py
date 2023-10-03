import json
import re
from flask import Flask, request,flash
from scapy.all import *
import pyshark
from pycrate_asn1rt.utils import *
from pycrate_asn1dir import NGAP
from pycrate_mobile.NAS5G import *
from pycrate_mobile.NAS import *
from nas2 import nested
from conversion import nested_list_to_json
app = Flask(__name__)
# nasPDUBytes=None
with open('/Users/anishrishi/Documents/internship/integrated/2.txt','r') as f:
    nasPDUBytes=f.read()
u=nasPDUBytes.encode('latin-1')
string_value = u.decode('unicode_escape')
u=string_value.encode('latin-1')
nasPDUBytes=u
print(u)
# nasPDUBytes =b'~\x02\\\xc5-]\x03~\x00h\x01\x00G.\x01\x01\xc2\x11\x00\t\x01\x00\x0611\x01\x01\xff\x01\x06\x04A\x89\x04A\x89)\x05\x01\xc0\xa8d\x02"\x01\x01y\x00\x06\x01 A\x01\x01\t{\x00\x0f\x80\x00\r\x04\x08\x08\x08\x08\x00\r\x04\x08\x08\x04\x04%\t\x08internet\x12\x01'
msg,err =parse_NAS5G(nasPDUBytes)
a=None
show(msg)
try:
    print(msg[3].get_val())
    y=(msg[3].get_val())
    # print(y)
    Msg, err = parse_NAS5G(y)
    a=True
    if Msg==None:
        a=False
        Msg=msg
    # print("hi")
    # show(msg[3])
    # print(Msg.get_val())
    # print()
    # print("*****************")
    # print("\n")
    # print(msg.to_bytes())
    # msg[0].set_val(196)
    # (msg[0][0].set_val(196))
    # print("\n")
    # ol=[[196, 0, 0, 94], [119, 9, [4, 0, 5, b's\x80a!\x85aQ\xf1']], [113, 35, [[196, 0, 0, 65], [[0, 7]], [[1, 1]], [13, [0, 0, 0, 1, [b'\x00\xf1\x10', b'\x00\x00', 0, 0, 0, b'!Ce\x87Y']]], [16, 1, [0, 0, 0, 0, 0, 0, 0, 0]], [46, 4, [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]], [47, 2, [[1, [1]]]], [83, 1, [0, 0, 0, 0, 0]]]]]
    # Msg.set_val(ol)
    # b=Msg.to_bytes()
    # show(Msg)
    # print(b)
    # hex_str=hexlify(b).decode('utf-8')
    # hex_str="0x"+hex_str
    # show(msg)

    # print(msg.to_bytes())
    # msg[3].set_val(b)
    print("\n")
    # show(Msg)
    # print(msg.to_bytes())
except Exception as e:
    print("hey")
    a=False
    Msg=msg
    print(e)
    # print(msg.get_val())
    print("NO Encrypted message")
    pass
def get_name(obj):
    # print("*****************")
    obj=str(obj)
    t=""
    for i in obj:
        if i=='<' or i=='>':
            continue
        else:
            if i==":":
                break
            t+=i
    return t

lo=[]
def recursion(obj, parent):
    try:
        for i in obj:
            kk=get_name(i)
            # print(kk)
            lo.append(kk)
            # print(i)
            recursion(i, obj)
    except Exception as e:
        return
recursion(Msg,None)
show(Msg)
jj=nested(Msg.get_val(),lo)
ngapMessage1=nested_list_to_json(jj)

# ol=['main', ['5GMMHeader ', ['EPD ', 126], ['spare ', 0], ['SecHdr ', 0], ['Type ', 94]], ['IMEISV ', ['T ', 119], ['L ', 9], ['5GSID ', ['Digit1 ', 4], ['Odd ', 0], ['Type ', 5], ['Digits ', 's\\x80a!\\x85aQ\\xf1']]], ['NASContainer ', ['T ', 113], ['L ', 35], ['5GMMRegistrationRequest ', ['5GMMHeader ', ['EPD ', 126], ['spare ', 0], ['SecHdr ', 0], ['Type ', 65]], ['NAS_KSI ', ['NAS_KSI ', ['TSC ', 0], ['Value ', 7]]], ['5GSRegType ', ['5GSRegType ', ['FOR ', 1], ['Value ', 1]]], ['5GSID ', ['L ', 13], ['5GSID ', ['spare ', 0], ['Fmt ', 0], ['spare ', 0], ['Type ', 1], ['Value ', ['PLMN ', '\\x00\\xf1\\x10'], ['RoutingInd ', '\\x00\\x00'], ['spare ', 0], ['ProtSchemeID ', 0], ['HNPKID ', 0], ['Output ', '!Ce\\x87Y']]]], ['5GMMCap ', ['T ', 16], ['L ', 1], ['5GMMCap ', ['SGC ', 0], ['5G-HC-CP-CIoT ', 0], ['N3Data ', 0], ['5G-CP-CIoT ', 0], ['RestrictEC ', 0], ['LPP ', 0], ['HOAttach ', 0], ['S1Mode ', 0]]], ['UESecCap ', ['T ', 46], ['L ', 4], ['UESecCap ', ['5G-EA0 ', 1], ['5G-EA1_128 ', 1], ['5G-EA2_128 ', 1], ['5G-EA3_128 ', 1], ['5G-EA4 ', 0], ['5G-EA5 ', 0], ['5G-EA6 ', 0], ['5G-EA7 ', 0], ['5G-IA0 ', 1], ['5G-IA1_128 ', 1], ['5G-IA2_128 ', 1], ['5G-IA3_128 ', 1], ['5G-IA4 ', 0], ['5G-IA5 ', 0], ['5G-IA6 ', 0], ['5G-IA7 ', 0], ['EEA0 ', 1], ['EEA1_128 ', 1], ['EEA2_128 ', 1], ['EEA3_128 ', 1], ['EEA4 ', 0], ['EEA5 ', 0], ['EEA6 ', 0], ['EEA7 ', 0], ['EIA0 ', 1], ['EIA1_128 ', 1], ['EIA2_128 ', 1], ['EIA3_128 ', 1], ['EIA4 ', 0], ['EIA5 ', 0], ['EIA6 ', 0], ['EIA7 ', 0]]], ['NSSAI ', ['T ', 47], ['L ', 2], ['NSSAI ', ['SNSSAI ', ['Len ', 1], ['SNSSAI ', ['SST ', 1]]]]], ['5GSUpdateType ', ['T ', 83], ['L ', 1], ['5GSUpdateType ', ['spare ', 0], ['EPS-PNB-CIoT ', 0], ['5GS-PNB-CIoT ', 0], ['NG-RAN-RCU ', 0], ['SMSRequested ', 0]]]]]]
ol=jj
@app.route('/', methods=['GET'])
def index():
    return '''
     <!DOCTYPE html>
<html>
<head>
    <title>NGAP Message</title>
</head>
<body>
    <h1>NGAP Message</h1>
    <div id="ngap-message"></div>
    <script>
 const ngapMessage = ''' + (ngapMessage1) + ''';

function displayObject(obj, container, parentObj, parentKey) {
    if (typeof obj === "object") {
        const table = document.createElement('table');
        table.border = '1';
        for (const key in obj) {
            const tr = document.createElement('tr');
            const th = document.createElement('th');
            th.textContent = key;
            tr.appendChild(th);
            const td = document.createElement('td');
            displayObject(obj[key], td, obj, key);
            tr.appendChild(td);
            table.appendChild(tr);
        }
        container.appendChild(table);
    } else if (Array.isArray(obj)) {
        const ul = document.createElement('ul');
        for (let i = 0; i < obj.length; i++) {
            const li = document.createElement('li');
            displayObject(obj[i], li, obj, i);
            ul.appendChild(li);
        }
        container.appendChild(ul);
    } else {
        const input = document.createElement('input');
        input.type = 'text';
        input.value = obj;
        input.addEventListener('input', function() {
            if (typeof obj === 'number') {
                parentObj[parentKey] = Number(this.value);
            } else {
                parentObj[parentKey] = this.value;
            }
        });
        container.appendChild(input);
    }
}
    const container = document.getElementById('ngap-message');
    displayObject(ngapMessage, container, ngapMessage, 'ngapMessage');

    </script>
    <button id='btn'>Submit</button>
    <script>
    const submitButton = document.getElementById('btn');
    submitButton.addEventListener('click', function() {
    fetch('http://127.0.0.1:5000', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(ngapMessage)
    });
});
    </script>
</body>
</html>
'''
# def updating(js,ngapMessage):
#     for i in range(len(ngapMessage)):
#         if type(ngapMessage[i]) is list:
#             updating(js,ngapMessage[i])
#         elif type(ngapMessage[i]) is dict:
#             for key in ngapMessage[i]:
#                 if key in js:
#                     ngapMessage[i][key]=js[key]
#         else:
#             if ngapMessage[i] in js:
#                 ngapMessage[i]=js[ngapMessage[i]]
#     return ngapMessage
# def change_data_structures(js, hey):
#     def change_structure(js, hey):
#         if isinstance(hey, dict):
#             for key, value in hey.items():
#                 if key in js:
#                     js[key] = change_structure(js[key], value)
#             return js
#         elif isinstance(hey, list) or isinstance(hey, tuple):
#             return type(hey)([change_structure(js[i], hey[i]) for i in range(len(hey))])
#         else:
#             return js
#     return change_structure(js, hey)
def values(js):
    if type(js)==list:
        for i in range(len(js)):
            if type(js[i])==list:
                values(js[i])
            elif type(js[i])==dict:
                for key in js[i]:
                    if key in js:
                        js[i][key]=js[key]
            else:
                if js[i] in js:
                    js[i]=js[js[i]]
def value(obj, par):
    if isinstance(obj, list):
        temp = []
        for i in obj:
            value(i, temp)
        if len(temp) > 0 and isinstance(temp[0], list):
            par.append(temp)
        else:
            par.extend(temp)
    elif isinstance(obj, dict):
        for i in obj.values():
            if isinstance(i, int) or isinstance(i, bytes):
                par.append(i)
            else:
                value(i, par)
    return
def convert_to_bytes(js):
    if isinstance(js, dict):
        for key, value in js.items():
            js[key] = convert_to_bytes(value)
    elif isinstance(js, list):
        for i, item in enumerate(js):
            js[i] = convert_to_bytes(item)
    elif isinstance(js, str):
        js=js.strip()
        if bool(re.match('^[0-9a-zA-Z0-9\-]*$', js)) == False:
            u=js.encode('latin-1')
            string_value = u.decode('unicode_escape')
            u = string_value.encode('latin-1')
            js=u
    return js
            
def update_list(l1, l2):
    iterator = iter(l1)
    def helper(sublist):
        for i, v in enumerate(sublist):
            if isinstance(v, list):
                helper(v)
            else:
                sublist[i] = next(iterator)
    helper(l2)
@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        js = request.get_json()
        # print(js)
        print("\n")
        js=convert_to_bytes(js)
        # print(js)
        p=[]
        value(js,p)
        valuest=Msg.get_val()
        update_list(p,valuest)
        # print(valuest)
        Msg.set_val(valuest)
        b=Msg.to_bytes()
        if a:
            msg[3].set_val(b)
        else:
            msg.set_val(valuest)
        print(msg.to_bytes())

            





        return 'POST request handled'
    else:
        return 'GET request handled'

if __name__ == '__main__':

    app.run(debug=True)