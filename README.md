# monsoon_power_measurement

### Equipment and Cable Connections
Monsoon Power Monitor
![back view](Pasted_image_20230609122725.png)

### Software Pre-request
https://github.com/msoon/PyMonsoon/tree/master
```bash
# create Python2.7 env
conda create -n monsoon python=2
conda activate monsoon

# install the specific version of libusb1
pip install libusb1==1.9.3

# install monsoon
pip install monsoon
```

### Firmware
[LVPM_RevE_Prot_1_Ver32.fwm](https://github.com/msoon/PyMonsoon/blob/master/Firmware/LVPM/LVPM_RevE_Prot_1_Ver32.fwm)

#### install firmware
Hold the "output enabled" button on the front panel and push the power button.
Run with `sudo`.
```python
import Monsoon.reflash as reflash  
Mon=reflash.bootloaderMonsoon()  
Mon.setup_usb()  
fwm_name=b"LVPM_RevE_Prot_1_Ver32.fwm"  
Header, Hex = Mon.getHeaderFromFWM(fwm_name.decode('latin-1'))  
  
if Mon.verifyHeader(Header):  
Mon.writeFlash(Hex)
```

### Measure Experiments
Since the max voltage of `Mon.setVout()` is `4.55V`, we power the embedded board by laptop. One cable between power monitor and embedded board, another cable between power monitor and laptop.
![front view](Pasted_image_20230609122718.png)

#### Run the experiments
Run with `sudo`.
```bash
which python
sudo ...
```

```python
import Monsoon.LVPM as LVPM  
import Monsoon.sampleEngine as sampleEngine  
import Monsoon.Operations as op  
  
Mon = LVPM.Monsoon()  
Mon.setup_usb()  
  
# Mon.setVout(4.0)  
engine = sampleEngine.SampleEngine(Mon)  
# engine.enableCSVOutput("Main Example.csv")  
engine.ConsoleOutput(True)  
numSamples=50000 #sample for ten second  
# engine.startSampling(numSamples)  
  
#Disable Main channels  
engine.disableChannel(sampleEngine.channels.MainCurrent)  
engine.disableChannel(sampleEngine.channels.MainVoltage)  
#Enable USB channels  
engine.enableChannel(sampleEngine.channels.USBCurrent)  
engine.enableChannel(sampleEngine.channels.USBVoltage)  
#Enable Aux channel  
# engine.enableChannel(sampleEngine.channels.AuxCurrent)  
#Set USB Passthrough mode to 'on,' since it defaults to 'auto' and will turn off when sampling mode begins.  
Mon.setUSBPassthroughMode(op.USB_Passthrough.On)  
  
engine.enableCSVOutput("USB Example.csv")  
engine.startSampling(numSamples)
```

