import Monsoon.reflash as reflash
Mon=reflash.bootloaderMonsoon()
Mon.setup_usb()
fwm_name=b"LVPM_RevE_Prot_1_Ver32.fwm"
Header, Hex = Mon.getHeaderFromFWM(fwm_name.decode('latin-1'))

if Mon.verifyHeader(Header):
    Mon.writeFlash(Hex)
