from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

Serge = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'AD823', 'dest':TEMPLATE, 'tool':SKIDL, 'description':'OpAmp', '_match_pin_regex':False, 'ref_prefix':'IC', 'num_units':None, 'fplist':None, 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'DIP8', 'pins':[
            Pin(num=1,name='A.OUT',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num=2,name='A.NEG',func=Pin.types.INPUT,do_erc=True),
            Pin(num=3,name='A.POS',func=Pin.types.INPUT,do_erc=True),
            Pin(num=4,name='V-',func=Pin.types.PWRIN,do_erc=True),
            Pin(num=5,name='B.POS',func=Pin.types.INPUT,do_erc=True),
            Pin(num=6,name='B.NEG',func=Pin.types.INPUT,do_erc=True),
            Pin(num=7,name='B.OUT',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num=8,name='V+',func=Pin.types.PWRIN,do_erc=True)] })])