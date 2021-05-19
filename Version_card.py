import getpass
import telnetlib
import sys
import time

HOST = "172.16.88.187"
string_GEPON = "GEPON"
string_ena = "enable"
service_card = "cd service"
string_gpon = "gpon"
quebra_linha = "ter l 0"
back = "cd .."
version = "show version"
press_any_key = "aaa"

stdoutOrigin = sys.stdout
sys.stdout = open("log.txt", "w")

def telnet_config(ip, slot, pon, no):
    try:
        # print(ip)
        tn = telnetlib.Telnet(ip, timeout=10)
        #tn.set_debuglevel(99)

        # tn.read_until(b" --Press any key to continue Ctrl+c to stop-- ")

        # tn.write(press_any_key.encode('ascii'))
        tn.read_until(b"Login: ")

        tn.write(string_GEPON.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")

        tn.write(string_GEPON.encode('ascii') + b"\n")
        tn.read_until(b"User> ")

        tn.write(string_ena.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")

        tn.write(string_GEPON.encode('ascii') + b"\n")
        tn.read_until(b"# ")

        tn.write(service_card.encode('ascii') + b"\n")
        tn.read_until(b"service#")

        cmd1 = "telnet slot " + slot
        print(cmd1)
        tn.write(cmd1.encode('ascii') + b"\n")

        cmd2 = "cd service"
        tn.write(cmd2.encode('ascii') + b"\n")
        tn.read_until(b"service# ")

        cmd3 = "ter l 0"
        tn.write(cmd3.encode('ascii') + b"\n")
        tn.read_until(b"service# ")

        cmd4 = "cd .."
        tn.write(cmd4.encode('ascii') + b"\n")
        tn.read_until(b"# ")

        cmd5 = "show version"
        print(cmd5)
        tn.write(cmd5.encode('ascii') + b"\n")
        print(tn.read_until(b"# ").decode('ascii'))
        tn.close()

        print("------" + ip + " ok")

    except:
        print("------" + ip + " connect err")



def main():
    with open('ip.txt', 'r', encoding='utf-8') as f1:
        for line in f1.readlines():
            line = line.strip('\n')
            array = line.split()
            print(array[0] + " " + array[1] + " " + array[2] + " " + array[3])
            telnet_config(array[0], array[1], array[2], array[3])




main()
