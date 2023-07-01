import gc
import machine
import network
import socket
import webrepl
import sec

# try:
#     import umqtt.simple
# except:
#     import mip
#     mip.install("umqtt.simple")
#     import umqtt.simple


def main():
    adc = machine.ADC(0)

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('listening on', addr)
    while True:
        cl, addr = s.accept()
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        response = f"{adc.read()}"
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n')
        cl.send(response)
        cl.close()



def wifi_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(sec.WIFI_SSID, sec.WIFI_PASS)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)


wifi_connect()
webrepl.start()
gc.collect()
main()