# import time
# import datetime
# # timestamp = time.strftime('%H:%M:S')
# start_time = datetime.datetime.now().replace(hour=6)
# end_time = datetime.datetime.now().replace(hour=11)
# times = []


import time
import datetime

present_time = datetime.datetime.now()

hour = present_time.hour

def generate_greetings(hour):
    if 6 <=hour<=12:
        return "Good Morning!"
    elif 12<hour<=15:
        return "Good Noon"
    elif 15<hour<=18:
        return "Good Afternoon"
    elif 18<hour<=24:
        return "Good Night"
    

name = input("What's your name ? ")

greeting = generate_greetings(hour)   

print( f"{greeting} {name}")


        
         