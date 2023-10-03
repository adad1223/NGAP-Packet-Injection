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
def final_decode(nasPDUBytes):
    u=nasPDUBytes.encode('latin-1')
    string_value = u.decode('unicode_escape')
    u=string_value.encode('latin-1')
    nasPDUBytes=u
    msg,err =parse_NAS5G(nasPDUBytes)
    a=None
    show(msg)
    try:
        y=(msg[3].get_val())
        Msg, err = parse_NAS5G(y)
        a=True
        if Msg==None:
            a=False
            Msg=msg
    except Exception as e:
        print(e)
        a=False
        Msg=msg
        # print(e)
        print("NO Encrypted message")
        pass
    def get_name(obj):
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
                lo.append(kk)
                recursion(i, obj)
        except Exception as e:
            return
    recursion(Msg,None)
    show(Msg)
    jj=nested(Msg.get_val(),lo)
    ngapMessage1=nested_list_to_json(jj)
    return ngapMessage1
ngapMessage1=final_decode('~\x00Ay\x00\r\x01\x00\xf1\x10\x00\x00\x00\x00!Ce\x87Y.\x04\xf0\xf0\xf0\xf0')
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
        if bool(re.match('^[0-9a-zA-Z0-9\-]*$', js)) == False or js=='internet' or js==" ":
            u=js.encode('latin-1')
            string_value = u.decode('unicode_escape')
            u = string_value.encode('latin-1')
            js=u
    return js
            
def update_list(l1, l2):
    # print(l1)
    print("\n")
    # print(l2)
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
    nasPDUBytes='~\x02\\\xc5-]\x03~\x00h\x01\x00G.\x01\x01\xc2\x11\x00\t\x01\x00\x0611\x01\x01\xff\x01\x06\x04A\x89\x04A\x89)\x05\x01\xc0\xa8d\x02"\x01\x01y\x00\x06\x01 A\x01\x01\t{\x00\x0f\x80\x00\r\x04\x08\x08\x08\x08\x00\r\x04\x08\x08\x04\x04%\t\x08internet\x12\x01'
    u=nasPDUBytes.encode('latin-1')
    string_value = u.decode('unicode_escape')
    u=string_value.encode('latin-1')
    nasPDUBytes=u
    msg,err =parse_NAS5G(nasPDUBytes)
    a=None
    show(msg)
    try:
        # print(msg[3].get_val())
        y=(msg[3].get_val())
    # print(y)
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
    if request.method == 'POST':
        js = request.get_json()
        print(js)
        print("\n")
        js=convert_to_bytes(js)
        print(js)
        print("\n")
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