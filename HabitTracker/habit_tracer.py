import requests
from datetime import datetime
from tkinter import messagebox
from tkinter import simpledialog,Tk
USERNAME="your username"
TOKEN="your pixela generated token"
graph_id="your graph id"
user_endpoint="https://pixe.la/v1/users"

user_parameters={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# user_creation=requests.post(url=user_endpoint,json=user_parameters)
# print(user_creation.text)


graph_endpoint=f"{user_endpoint}/{USERNAME}/graphs"

graph_parameters={
    "id":graph_id,
    
    "name":"CodingTime",
    "unit":"Hours",
    "type":"float",
    "color":"momiji",
}

header={
    "X-USER-TOKEN":TOKEN,
}
# graph_creation=requests.post(url=graph_endpoint,json=graph_parameters,headers=header)
# print(graph_creation.text)


window=Tk()
window.withdraw()
user_input=simpledialog.askstring(title="CodingTime",prompt="Enter today's coding time(In Hours): ")
current_date=datetime.now()

pixel_endpoint=f"{graph_endpoint}/{graph_id}"

pixel_parameters={
    "date":current_date.strftime("%Y%m%d"),
    "quantity":user_input,
}
pixel_creation=requests.post(url=pixel_endpoint,json=pixel_parameters,headers=header)
print(pixel_creation.text)
window.destroy()
