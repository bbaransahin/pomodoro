import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

print("Welcome to pomodoro")
print("ctrl+s will be pause the timer")
print("ctrl+q will be continue the timer")
print("ctrl+c will terminate the timer")
pom_time = int(input('Enter the time of pomodoro in minutes:'))
countdown(pom_time*60)
