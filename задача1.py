class Stroca(BaseException):
    pass
try:
    v1 = int(input())
    v2 = int(input())
    t = int(input())
    if t == 0:
        raise Stroca

    def decorator(uscorenie):
        def obertc(v1,v2,t):
            uscorenie()
            print(((v2*v2)-(v1*v1))/ (2*((v2-v1)/t)))
        return obertc

    @decorator
    def uscorenie():
        print((v2-v1)/t)

    uscorenie(v1,v2,t)
except Stroca:
    print('время не может равняться нулю')
except ValueError:
    print('Недьзя вводить строки')