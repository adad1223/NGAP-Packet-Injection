from pycrate_mobile.NAS5G import *
from pycrate_mobile.NAS import *
from pycrate_asn1dir import NGAP
from pycrate_asn1rt.utils import *
from nas2 import nested
def gettingNAS(ngapMessage):
    val=None
    def convert_to_bytes(js,par,val):
        if isinstance(js, dict):

            for key, value in js.items():
                if(key=='pDUSessionNAS-PDU'):
                    val=value
                val = convert_to_bytes(value,js,val)
        elif isinstance(js, list):
            # print(js[0])
            for i, item in enumerate(js):
                val = convert_to_bytes(item,js,val)
        elif isinstance(js, str):
            if(js=='NAS-PDU'):
                val=par[1]
            # elif(js=='pDUSessionNAS-PDU'):
            #     print(par)
            
        return val
    val = convert_to_bytes(ngapMessage,None,val)
    return val
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
def updatingNAS(ngapMessage,value):
    def convert_to_byte(js,par,valu):
        if isinstance(js, dict):
            for key, value in js.items():
                if(key=='pDUSessionNAS-PDU'):
                    value=valu
                val = convert_to_byte(value,js,valu)
        elif isinstance(js, list):
            for i, item in enumerate(js):
                val = convert_to_byte(item,js,valu)
        elif isinstance(js, str):
            if(js=='NAS-PDU'):
                par[1]=valu
        return ngapMessage
    ngapMessage=convert_to_byte(ngapMessage,None,value)
    return ngapMessage
lo=[]
def recursion(obj, parent):
    try:
        for i in obj:
            kk=get_name(i)
            lo.append(kk)
            recursion(i, obj)
    except Exception as e:
        return
def neso(obj,par):
    if isinstance(obj, list):
        # temp = []
        for i in obj:
            neso(i, obj)
    if isinstance(obj,str):
        if obj=='5GMMHeader':
            print(par)

        
def getting_msg_type(nasPDUBytes):
    u=nasPDUBytes.encode('latin-1')
    string_value = u.decode('unicode_escape')
    u=string_value.encode('latin-1')
    nasPDUBytes=u
    msg,err =parse_NAS5G(nasPDUBytes)
    a=None
    # try:
    #     Msg=parse_NAS5G(msg[3].get_val())
    #     x=(msg['5GMMHeader'])
    #     x=x[3]
    #     x=str(x)
    #     if x==None:
    #         x=msg[3][0][3]
    #     print(1)
    # except:
    #     print(2)
    #     y=(msg[3].get_val())
    #     Msg, err = parse_NAS5G(y)
    #     x=Msg['5GMMHeader'][3]
    #     if x==None:
    #         x=Msg[3]['5GMMHeader'][3]
        # recursion(Msg,None)
        # jj=nested(Msg.get_val(),lo)
        # x=str(x)
    try:
        # print(msg[3].get_val())
        y=(msg[3].get_val())
    # print(y)
        Msg, err = parse_NAS5G(y)
        a=True
        if Msg==None:
            a=False
            Msg=msg
        try:
            x=Msg['5GMMHeader'][3]
        except:
            x=Msg[3][0][3]
        print("\n")

    except Exception as e:
        print("hey")
        a=False
        x=msg['5GMMHeader'][3]
        if x==None:
            x=msg[3][0][3]
        Msg=msg
    x=str(x)
    a=False
    stri=""
    for i in x:
        if i=='(':
            a=True
            continue
        if i==')':
            a=False
            continue
        if a==True:
            stri+=i
    print("********")
    print(stri)
    print("********")
    return stri
if __name__=='__main__':
    print(gettingNAS(ngapMessage))