import network, badge, ugfx, usocket as socket

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("revspace-pub-2.4ghz")
sta_if.isconnected()

badge.init()
ugfx.init()

CONTENT = """\
HTTP/1.0 200 OK
Hello #{} from MicroPython!
"""

curIP = sta_if.ifconfig()[0]
ai = socket.getaddrinfo(curIP,8080)
addr = ai[0][4]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(5)
counter=0

print('Acces at: ', curIP, ':8080')

ugfx.clear();
ugfx.string(10,10,curIP + '8080/text',"PermanentMarker22",0)
ugfx.flush()


while True:
    res = s.accept()
    client_s = res[0]
    client_addr = res[1]
    print("Client address:", client_addr)
    req = client_s.recv(4096)
    client_s.send(bytes(CONTENT.format(counter), "ascii"))
    client_s.close()
    parts = req.decode('ascii').split(' ')
    parts[1] = parts[1][1:]
    if parts[1] == 'exit':
      break
    if parts[1] != 'favicon.ico':
        print('data:', parts[1])
        ugfx.clear();
        ugfx.string(10,10,parts[1],"PermanentMarker22",0)
        ugfx.flush()
    counter += 1

