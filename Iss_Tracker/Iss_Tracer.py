import requests 
import datetime as dt
import smtplib
import time
MY_LATITUDE=16.25217846507038
MY_LONGITUDE=80.32580758895553
MY_EMAIL="your email id"
MY_PASSOWRD="your password"

def iss_position():
    iss_response=requests.get(url="http://api.open-notify.org/iss-now.json")
    #raises an exception when it does not get a successful response.
    iss_response.raise_for_status()
    #to get that data
    data=iss_response.json()
    iss_latitude=int(float(data['iss_position']['latitude']))
    iss_longitude=int(float(data['iss_position']['longitude']))
     #to check weather our position is within +5 or -5 of iss position.
    if 10<iss_latitude<22 and 74<iss_longitude<86:
        return True
        



def is_night_time():
    current_time=dt.datetime.now()
    current_hour=int(current_time.hour)
    parameters={
        "lat":MY_LATITUDE,
        "lng":MY_LONGITUDE,
        "formatted":0,
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    details=response.json()
    sunrise=int(details["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset=int(details["results"]["sunset"].split('T')[1].split(':')[0])
    
    if sunset<=current_hour and current_hour<=sunrise:
        return True
print("Code is currently running and will notify you via gmail when Iss is above you!!")
while True:  
    time.sleep(20)
    if iss_position() and is_night_time():
        send_mail=smtplib.SMTP("smtp.gmail.com")
        send_mail.starttls()
        send_mail.login(user=MY_EMAIL, password=MY_PASSOWRD)
        send_mail.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="khyathivardhan17@gmail.com",
            msg="Subject:IssAlert\n\nIss is abouve your head watch towards the sky to see it"
            )
        break
        
   