from dnslib import DNSRecord, QTYPE, RR, A
import socket
import base64

HOST, PORT = '0.0.0.0', 5454
HIDDEN_MESSAGE_PART_1 = "CTF_part_1_hidden"  # 部分 flag 内容

# 编码隐藏信息
encoded_message = base64.b64encode(HIDDEN_MESSAGE_PART_1.encode()).decode()

def handle_dns_request(data, addr, sock):
    request = DNSRecord.parse(data)
    reply = request.reply()

    for question in request.questions:
        qname = question.qname
        qtype = QTYPE[question.qtype]
        print(f"Received DNS query: {qname}, type: {qtype}")
        if qtype == 'A':
            reply.add_answer(RR(qname, QTYPE.A, rdata=A('192.168.1.1')))  # 正常 A 记录返回
            reply.add_auth(RR(qname, QTYPE.A, rdata=A('192.168.1.2')))  # 授权 A 记录返回

    # 将编码后的隐藏信息添加到 A 记录中作为子域名的一部分
    hidden_subdomain = f"hidden.{encoded_message}.example.com"
    reply.add_answer(RR(hidden_subdomain, QTYPE.A, rdata=A('10.0.0.1')))
    sock.sendto(reply.pack(), addr)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"DNS Server started on {HOST}:{PORT}")

    while True:
        data, addr = sock.recvfrom(512)
        handle_dns_request(data, addr, sock)
