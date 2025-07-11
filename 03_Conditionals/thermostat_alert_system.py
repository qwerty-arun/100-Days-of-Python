# thermostat alert system
device_status = "active"
temperature = 38

if(device_status == "active"):
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temp normal")
else:
    print("Device is offline")