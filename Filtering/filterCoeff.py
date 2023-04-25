import numpy as np
import matplotlib.pyplot as plt
import scipy
import math

'''SCRIPT FOR GENERATING FILTER COEFFICIENTS FOR A GIVEN FILTER TYPE AND ORDER'''

#constants
freq = 60
dt = freq**-1

filterTypes = ["lowpass", "highpass", "bandpass", "bandstop"]

print("choose a filter type: ")
for k,v in enumerate(filterTypes):
    print(k, v)
    
bandtype = filterTypes[int(input("Enter the number of the filter type: "))]

order = int(input("Enter the order of the filter: "))
freqs = []

while True:
	l=input("Enter frequencies of importance: ")
	if l=='exit':
		break
	freqs.append(float(l))
 
typeSel = input("IIR or FIR? enter 'i' or 'f': ").lower()
if typeSel == 'i':
	b , a = scipy.signal.iirfilter(order, freqs, btype=bandtype, analog=False, ftype='butter', output='ba', fs=freq)
elif typeSel == 'f':
	b , a = scipy.signal.firwin(order, freqs, btype=bandtype, analog=False, ftype='butter', output='ba', fs=freq)
else:
	print("invalid input")
	exit()


print('b table:')
print(b)

print('a table:')
print(a)


w, h = scipy.signal.freqz(b, a)

plt.figure() #phase plot

plt.semilogx(w, 20 * np.log10(abs(h)))

plt.title('Butterworth filter frequency response')

plt.xlabel('Frequency [radians / second]')

plt.ylabel('Amplitude [dB]')

plt.margins(0, 0.1)

plt.grid(which='both', axis='both')

plt.axvline(freqs[0], color='green') # cutoff frequency

plt.tight_layout()



plt.style.use('dark_background')

plt.show()