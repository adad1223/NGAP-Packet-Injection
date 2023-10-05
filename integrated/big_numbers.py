import json
def checking_for_big_nos():
    with open('./integrated/packet.json', 'r') as f:
        ngapMessage = json.load(f)
    f.close()
    def numbersbig(js,par,val):
        if isinstance(js, dict):

            for key, value in js.items():
                if(key=='pDUSessionNAS-PDU'):
                    val=value
                val = numbersbig(value,js,val)
        elif isinstance(js, list):
            for i, item in enumerate(js):
            # print(item)
                val = numbersbig(item,js,val)
        elif isinstance(js, int):
            st=str(js)
            if len(st)>20:
                stri="xX"+st
                par[0]=stri
        return val
    val = numbersbig(ngapMessage,None,None)
    return ngapMessage
def converting_string_to_int(ngapMessage):
    # with open('./integrated/packet.json', 'r') as f:
    #     ngapMessage = json.load(f)
    # f.close()
    def numbersbig(js,par,val):
        if isinstance(js, dict):

            for key, value in js.items():
                if(key=='pDUSessionNAS-PDU'):
                    val=value
                val = numbersbig(value,js,val)
        elif isinstance(js, list):
            for i, item in enumerate(js):
            # print(item)
                val = numbersbig(item,js,val)
        elif isinstance(js, str):
            if js[0:2]=="xX":
                js=js[2:]
                js=int(js)
                par[0]=js
        return val
    val = numbersbig(ngapMessage,None,None)
    return ngapMessage
if __name__=="__main__":
    print(checking_for_big_nos())