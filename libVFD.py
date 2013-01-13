import time #time module imported for animation functions
try:
    import serial #pySerial-2.5 library
except importError:
    print "libVFD module needs pyserial library to be installed."

class VFD:
    def __init__(self, portName = '/dev/ttyAMA0', baudRate = 115200):
        self.port = serial.Serial(portName, baudRate)
        
    def clearAll(self):
        """This clears VFD memory and display"""
	    if self.port.isOpen():
	        self.port.write('\x0C')
	    else:
	        print "No initialized VFD found"
    
    def setBrtness(self, percentage):
        """Setting VFD brightness, in percents"""
        if self.port.isOpen():
            self.port.write('\x1F\x58\x04')
        else:
            print "No initialized VFD found"

    def writeStr(self, Str):
        """Write string"""
	    if self.port.isOpen():
	        self.port.write(Str)
	    else:
	        print "No initialized VFD found"
    
    def blink(blinkCount):
        """Blinking VFD, blinkCount times"""
        pass
            
    def vScroll():
        """Scrolling display vertically"""
        pass
        
    def hScroll():
        """Scrolling display horizontally"""
        pass
        
    def bitmapImage():
        """Display a bitmap image from file"""
        if self.port.isOpen():
            self.port.write('\x1F\x28\x66\x11\x08\x00\x01\x00\x01\xFD\xFF\xCD\xFA\xFA\xCD\xFF\xFD')
            time.sleep(1)
            self.port.write('\n Privet German!')
        else:
            print "No initialized VFD found"

if __name__ == '__main__':
    #Demonstation of libVFD functions
    sampleVFD = VFD() #Create an object of VFD class. You can do this other way - sampleVFD = VFD('/dev/ttyAMA0', 115200)
    sampleVFD.clearAll() #Clear display and its memory
    sampleVFD.setBrtness(25) #Set brightness to 25%
    sampleVFD.writeStr("Hello World!") #Write string on current cursor position
