from scapy.all import *
lst=[]
count=0
def call_back(packet):
    global count
    if(packet.haslayer(SCTP)):
        packet[IP].src="192.168.0.1"
        count+=1
        packet[IP].dst="192.168.0.218"
        pkt=IP(packet[IP])
        # print(pkt[SCTPChunkData].data)
        lst.append(pkt)
        send(pkt)
        print(count)
        wrpcap('ui.pcap', lst)
x=input("Enter file name: ")
packet = sniff(offline=x,prn=call_back)
