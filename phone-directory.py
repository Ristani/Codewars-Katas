from re import sub

def phone(dir, num):
    if dir.count("+" + num) == 0:
        return "Error => Not found: " + num
    
    if dir.count("+" + num) > 1:
        return "Error => Too many people: " + num
    
    for line in dir.splitlines():
        if "+" + num in line:
            name = sub(".*<(.*)>.*", "\g<1>", line)
            line = sub("<" + name + ">|\+" + num, "", line)
            address = " ".join(sub("[^a-zA-Z0-9\.-]", " ", line).split())
            return "Phone => %s, Name => %s, Address => %s" % (num, name, address)