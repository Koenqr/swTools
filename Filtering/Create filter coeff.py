import numpy as np
import matplotlib.pyplot as plt
import scipy
import math

'''SCRIPT FOR GENERATING FILTER COEFFICIENTS FOR A GIVEN FILTER TYPE AND ORDER'''

#constants
freq = 60
dt = freq**-1

bandtype = "lowpass"

order = float(input("Enter the order of the filter: "))
cutOff = float(input("Enter the cut off frequency of the filter: "))

b , a = scipy.signal.iirfilter(order, cutOff, btype=bandtype, analog=False, ftype='butter', output='ba', fs=freq)

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

plt.axvline(cutOff, color='green') # cutoff frequency

plt.tight_layout()



plt.style.use('dark_background')

plt.show()