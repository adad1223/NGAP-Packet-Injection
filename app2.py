
import json
import re
from flask import Flask, request
from scapy.all import *
import pyshark
from pycrate_asn1rt.utils import *
from pycrate_asn1dir import NGAP
app = Flask(__name__)
ngapMessage = None
@app.before_request
def load_ngap_message():
    global ngapMessage
    with open('/Users/anishrishi/Documents/internship/integrated/packet.json', 'r') as f:
        ngapMessage = json.load(f)
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
 const ngapMessage = ''' + json.dumps(ngapMessage) + ''';

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
def change_data_structures(js, hey):
    def change_structure(js, hey):
        if isinstance(hey, dict):
            for key, value in hey.items():
                if key in js:
                    js[key] = change_structure(js[key], value)
            return js
        elif isinstance(hey, list) or isinstance(hey, tuple):
            return type(hey)([change_structure(js[i], hey[i]) for i in range(len(hey))])
        else:
            return js
    return change_structure(js, hey)
def convert_to_bytes(js):
    if isinstance(js, dict):
        for key, value in js.items():
            js[key] = convert_to_bytes(value)
    elif isinstance(js, list):
        for i, item in enumerate(js):
            js[i] = convert_to_bytes(item)
    elif isinstance(js, str):
        if(js=='NAS-PDU'):
            print()
        if(bool(re.match('^[a-z-A-Z0-9]*$',js))==False):
            u=js.encode('latin-1')
            string_value = u.decode('unicode_escape')
            u = string_value.encode('latin-1')
            js=u
    return js

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
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
        scapy_packet[IP].dst="192.168.10.204"
        send(scapy_packet)
        d.close()
        return 'POST request handled'
    else:
        return 'GET request handled'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)