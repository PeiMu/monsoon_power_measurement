import Monsoon.LVPM as LVPM
import Monsoon.sampleEngine as sampleEngine
import Monsoon.Operations as op

Mon = LVPM.Monsoon()
Mon.setup_usb()

# Mon.setVout(4.0)
engine = sampleEngine.SampleEngine(Mon)
# engine.enableCSVOutput("Main Example.csv")
engine.ConsoleOutput(True)

# sample for ten seconds
numSamples = 50000
# engine.startSampling(numSamples)

# Disable Main channels
engine.disableChannel(sampleEngine.channels.MainCurrent)
engine.disableChannel(sampleEngine.channels.MainVoltage)
# Enable USB channels
engine.enableChannel(sampleEngine.channels.USBCurrent)
engine.enableChannel(sampleEngine.channels.USBVoltage)
# Enable Aux channel
# engine.enableChannel(sampleEngine.channels.AuxCurrent)
# Set USB Passthrough mode to 'on,' since it defaults to 'auto' and will turn off when sampling mode begins.
Mon.setUSBPassthroughMode(op.USB_Passthrough.On)

engine.enableCSVOutput("USB Example.csv")
engine.startSampling(numSamples)
