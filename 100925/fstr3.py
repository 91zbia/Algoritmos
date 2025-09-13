def inverter(s):
    if s == "":
        return s
    else:
        return s[-1] + inverter(s[:-1])
    
print(inverter("hello"))
print(inverter("bia"))
print(inverter(""))  # Test with an empty string