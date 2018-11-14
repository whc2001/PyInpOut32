import ctypes, sys

inpout = ctypes.WinDLL("64" in sys.version and "inpoutx64.dll" or "inpout32.dll")

def __DllFunc(name, ret, args):
    func = inpout[name]
    func.restype = ret
    func.argtype = args
    return func

IsInpOutDriverOpen = __DllFunc("IsInpOutDriverOpen", ctypes.c_bool, (ctypes.c_void_p))
IsXP64Bit = __DllFunc("IsXP64Bit", ctypes.c_bool, (ctypes.c_void_p))

Out32 = __DllFunc("Out32", ctypes.c_void_p, (ctypes.c_short, ctypes.c_short))
Inp32 = __DllFunc("Inp32", ctypes.c_short, (ctypes.c_short))

DlPortReadPortUchar = __DllFunc("DlPortReadPortUchar", ctypes.c_ubyte, (ctypes.c_ushort))
DlPortWritePortUchar = __DllFunc("DlPortWritePortUchar", ctypes.c_void_p, (ctypes.c_ushort, ctypes.c_ubyte))

DlPortReadPortUshort = __DllFunc("DlPortReadPortUshort", ctypes.c_ushort, (ctypes.c_ushort))
DlPortWritePortUshort = __DllFunc("DlPortWritePortUshort", ctypes.c_void_p, (ctypes.c_ushort, ctypes.c_ushort))

DlPortReadPortUlong = __DllFunc("DlPortReadPortUlong", ctypes.c_ulong, (ctypes.c_ulong))
DlPortWritePortUlong = __DllFunc("DlPortWritePortUlong", ctypes.c_void_p, (ctypes.c_ulong, ctypes.c_ulong))
