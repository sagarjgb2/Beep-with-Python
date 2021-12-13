import winsound
frequency=int(input('Enter frequency in Hz..'))
duration=int(input('Enter the time in milliseconds'))
number_of_times=int(input('Enter the number of times the sound to be played'))
for i in range(0, number_of_times):
    winsound.Beep(frequency, duration)
print('! DONE !')
