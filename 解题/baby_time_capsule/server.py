'''from Crypto.Util.number import bytes_to_long, getPrime
import socketserver
import json

FLAG = b'HTB{--REDACTED--}'


class TimeCapsule():

    def __init__(self, msg):
        self.msg = msg
        self.bit_size = 1024
        self.e = 5

    def _get_new_pubkey(self):
        while True:
            p = getPrime(self.bit_size // 2)
            q = getPrime(self.bit_size // 2)
            n = p * q
            phi = (p - 1) * (q - 1)
            try:
                pow(self.e, -1, phi)
                break
            except ValueError:
                pass

        return n, self.e

    def get_new_time_capsule(self):
        n, e = self._get_new_pubkey()
        m = bytes_to_long(self.msg)
        m = pow(m, e, n)

        return {"time_capsule": f"{m:X}", "pubkey": [f"{n:X}", f"{e:X}"]}


def challenge(req):
    time_capsule = TimeCapsule(FLAG)
    while True:
        try:
            req.sendall(
                b'Welcome to Qubit Enterprises. Would you like your own time capsule? (Y/n) '
            )
            msg = req.recv(4096).decode().strip().upper()
            if msg == 'Y' or msg == 'YES':
                capsule = time_capsule.get_new_time_capsule()
                req.sendall(json.dumps(capsule).encode() + b'\n')
            elif msg == 'N' or msg == "NO":
                req.sendall(b'Thank you, take care\n')
                break
            else:
                req.sendall(b'I\'m sorry I don\'t understand\n')
        except:
            # Socket closed, bail
            return


class MyTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        req = self.request
        challenge(req)


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadingTCPServer(("0.0.0.0", 1337), MyTCPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
'''

from sympy.ntheory.modular import crt
from sympy import integer_nthroot
from Crypto.Util.number import long_to_bytes
#nc 环境 port     三次Y得到time_capsule和pubkey
##加密输出 1
c1 = 0x2D5BFF95F5E4C1A29C6912251389A828DD45A89DC915E1FB6F19D1BC70CE2CF49A8A600C956017DDB55471141C1283E832DE7F87D74A6FFCD8089228A8E25A97BF49B86B48D77BCA2629EF8AA8988E7B13352254596248C2B05ED033A914182DBD42153867EC7190B18035D34A0098EC3BEBE2933055B9337D05B32106210AAF

n1 = 0x636E550EDFA733E5D8531CE0B8283DF85447C606EFE44609E9E62F639219AD7B3D0D489D0F47325D64DE031BFB5C90C0EFB0FBEC8F1D04B3B336E0ABBBDA6634B2BAB24DCD74E3561FA635FA72E599F1EE522FF124DABB53035DEC0F6F1C9439AFDAF30144BE79386D11D90AFCDCFA9552E0DF6037F48B55BDBB30B2FC776ED9

##加密输出 2
c2= 0x6A3D5E0B56CAC5719C4D7ED0C1FBE0C2683B8CED7BB996EE9844DFA096C05B66BF18F136C45540EE263F8431F7D258A4B9EE3D419429845083673E363D343CFD9E329B226C787388B20D2037AB8F2D2D29EA5A76EA650C687385F844DE43E68EF733F07A8431C74BB48036CA7B1197E04FC5EF161CAAB891804A8EBCB0D2CE53

n2= 0x939C324269BDF0A0A8EB294EB0808BBFD2151913FDD1C100A5AA33D442EC1FB487B37CF87CF1B9FBB538EB51223DC193FF074F825B018EE548496CCE7762849408AD300582D8B9F7BF684377766AF7884C04BA23F217624D979AA84155661BCE0CB3383DCD2F1EB3D8324195B45F8837CF29A7E61FBA9AA52B369CB74C0D9639

##加密输出 3
c3 = 0x385D2213C7D7314F333727937FCB692B13AF214D88E0F6C473977810A99744CE34A5FA0FEEEA367572B4F23CC40481AF535D2537B2E28894F39CB1AF8D617152782EE3268B469E3F92E7666F17FABF5DCC275589AE0C08FF2A081442AF1AFE4A094C8B60748B6B91DF1C947BF53AB87806A33D8AE7CDE0BECBC250808DEFCBD

n3 = 0x9638FC9CA2DB7835EFE47F2C93EB261A7A028909BA866DA8C449DE4191FCAF3EAB68E879882B31817F289C8EA22135B32650812C24959A603288992C37F52C8D02C721DB7559D839B48118AA385304A616A29CEB48E02E968CC49719C3549CA72296605CD329E67270430025D65C5B854B8ECF48BFBCFA12904D63B7883BD84B

##使用中国余数定理计算m的e次方
x = crt([n1, n2, n3], [c1, c2, c3], check=True)
print("x=", x)

##开e次方求解m
m = integer_nthroot(x[0], 5)
print("m=", m)

##输出明文
flag = long_to_bytes(m[0])
print("flag=", flag)