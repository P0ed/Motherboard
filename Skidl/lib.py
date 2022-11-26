from skidl import *

# Metric constants
K = 1000
M = K * K
m = 1 / K
u = m / K
n = u / K
p = n / K

# Base nets
gnd = Net('GND')
vps =  Net('V+ supply')
vns = Net('V- supply')
vp = Net('V+')
vn =  Net('V-')

# Parts library
# set_default_tool(SKIDL)
lib = SchLib(name='Serge')

_ad823 = Part(lib, 'AD823', footprint='DIP8', dest=TEMPLATE, tool=SKIDL)
_ad823.ref_prefix = 'IC'
_ad823.description = 'OpAmp'
_ad823.pins += Pin(num=1, name='A.OUT', func=Pin.types.OUTPUT)
_ad823.pins += Pin(num=2, name='A.NEG', func=Pin.types.INPUT)
_ad823.pins += Pin(num=3, name='A.POS', func=Pin.types.INPUT)
_ad823.pins += Pin(num=4, name='V-', func=Pin.types.PWRIN)
_ad823.pins += Pin(num=5, name='B.POS', func=Pin.types.INPUT)
_ad823.pins += Pin(num=6, name='B.NEG', func=Pin.types.INPUT)
_ad823.pins += Pin(num=7, name='B.OUT', func=Pin.types.OUTPUT)
_ad823.pins += Pin(num=8, name='V+', func=Pin.types.PWRIN)
lib += _ad823

@subcircuit
def ad823(ap, an, ao, bp, bn, bo, vp=vp, vn=vn):
    device = _ad823()
    device[1] & ao
    device[2] & an
    device[3] & ap
    device[4] & vn
    device[5] & bp
    device[6] & bn
    device[7] & bo
    device[8] & vp

lib.export('Serge')
