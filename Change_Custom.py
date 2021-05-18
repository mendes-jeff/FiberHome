import getpass
import telnetlib

HOST = "172.16.88.187"
string_GEPON = "GEPON"
string_ena = "enable"
service_card = "cd service"
string_gpon = "gpon"
mode_fac = "cd factory"
enter_fac = "enter factory mode"
exit_fac = "exit factory mode"


def telnet_config(ip, slot, pon, no):
    try:
        # print(ip)
        tn = telnetlib.Telnet(ip, timeout=10)
        tn.set_debuglevel(99)

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

        tn.write(service_card.encode('ascii') + b"\n")
        tn.read_until(b"# ")

        cmd2 = "telnet data ponno " + pon + " onuno " + no
        print(cmd2)
        tn.write(cmd2.encode('ascii') + b"\n")

        tn.read_until(b"Login: ")

        tn.write(string_gpon.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")

        tn.write(string_gpon.encode('ascii') + b"\n")
        tn.read_until(b"User> ")

        tn.write(string_ena.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")

        tn.write(string_gpon.encode('ascii') + b"\n")
        tn.read_until(b"# ")

        tn.write(mode_fac.encode('ascii') + b"\n")
        tn.read_until(b"factorydir#")

        tn.write(enter_fac.encode('ascii') + b"\n")
        tn.read_until(b"factorydir#")

        cmd3 = "set custom BZ_ALGAR"
        print(cmd3)
        tn.write(cmd3.encode('ascii') + b"\n")

        cmd4 = "set report_product_code 0"
        print(cmd4)
        tn.write(cmd4.encode('ascii') + b"\n")

        cmd5 = "cd .."
        print(cmd5)
        tn.write(cmd5.encode('ascii') + b"\n")

        cmd6 = "reboot"
        print(cmd6)
        tn.write(cmd6.encode('ascii') + b"\n")

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
