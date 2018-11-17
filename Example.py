import InpOut32
from time import sleep

freqs = [262, 196, 196, 220, 196, 0, 247, 262]
duras = [4, 8, 8, 4, 4, 4, 4, 4]

def Beep(freq, dura):
    # For further info please see https://wiki.osdev.org/PC_Speaker
    if freq > 0:
        cycle = int(1193180 / freq)
        InpOut32.DlPortWritePortUchar(67, 182)
        InpOut32.DlPortWritePortUchar(66, (cycle & 255))
        InpOut32.DlPortWritePortUchar(66, ((cycle >> 8) & 255))
        tmp = InpOut32.DlPortReadPortUchar(97)
        InpOut32.DlPortWritePortUchar(97, (tmp | 3))
    sleep(dura / 1000)
    tmp = InpOut32.DlPortReadPortUchar(97)
    InpOut32.DlPortWritePortUchar(97, (tmp & 252))
    
def Setup():
    if not InpOut32.IsInpOutDriverOpen():
        raise("Driver open error, please run with admin privilege or run 'InstallDriver.exe' first!")

def Loop():
    for i in range(len(freqs)):
        Beep(freqs[i], 1000 / duras[i])
    sleep(1)

if __name__ == "__main__":
    Setup()
    while True:
        Loop()
