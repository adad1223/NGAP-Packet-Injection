from pycrate_mobile.NAS import *
from pycrate_asn1dir import NGAP
import json
class_name = 'DownlinkNASTransport'
def getting_mandatory_optional(class_name):
    try:
        op=class_name
        op+="IEs"
        class_obj = getattr(NGAP.NGAP_PDU_Contents, op)
    except:
        class_name+="_IEs"
        class_obj = getattr(NGAP.NGAP_PDU_Contents, class_name)
    x = class_obj.__dict__
    y=(x['_val'].__dict__)
    z=(y['_rv'])
    di={}
    for i in z:
        print(i['id'])
        print(i['presence'])
        di[i['id']]=i['presence']
    return di
if __name__=="__main__":
    print(getting_mandatory_optional('InitialUEMessage'))
# print((NGAP.NGAP_Constants._obj_.PDUSessionResourceSetupListSUReq))
# a=((NGAP.NGAP_Constants.PDUSessionResourceSetupRequestTransfer_IEs.__dict__))
# print(a)
# print(type(NGAP.NGAP_PDU_Contents.PDUSessionResourceSetupResponseIEs.to_json))
# print(x.'root'])
# x= NGAP.NGAP_PDU_Contents.PDUSessionResourceSetupResponseIEs.to_json
# print(json.loads(x))
# print(type(x))
# print((NGAP.NGAP_PDU_Contents.x))
