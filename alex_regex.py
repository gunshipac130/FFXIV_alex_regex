import re

# {
# 	"C2S_ActionRequest": "0x0283",
# 	"C2S_ActionRequestGroundTargeted": "0x01ef",
# 	"Common_UseOodleTcp": true,
# 	"PatchCode": [],
# 	"S2C_ActionEffect01": "0x01bf",
# 	"S2C_ActionEffect08": "0x0104",
# 	"S2C_ActionEffect16": "0x02b8",
# 	"S2C_ActionEffect24": "0x016c",
# 	"S2C_ActionEffect32": "0x0217",
# 	"S2C_ActorCast": "0x007b",
# 	"S2C_ActorControl": "0x026f",
# 	"S2C_ActorControlSelf": "0x00b2",
# 	"Server_IpRange": "0.0.0.0/0",
# 	"Server_PortRange": "1-65535"
# }

# Name string holder
C2S_ActionRequest = ""  #0
C2S_ActionRequestGroundTargeted = ""    #1
S2C_ActionEffect01 = "" #2
S2C_ActionEffect08 = "" #3
S2C_ActionEffect16 = "" #4
S2C_ActionEffect24 = "" #5
S2C_ActionEffect32 = "" #6
S2C_ActorCast = ""  #7
S2C_ActorControl = ""   #8
S2C_ActorControlSelf = ""   #9
HolderArray = [False, False, False, False, False, False, False, False, False, False]

textfile = open('string.txt', 'r', encoding='utf8')
print(textfile)

def addExtracted(stringExtract) :
    if len(stringExtract) > 0 :
        return stringExtract[0]

TitleFoundState = 0
for line in textfile:
    line = line.rstrip()
    tempstring = ""

    tempstring = re.findall('\d{4}.*IpcTypeFinder.*C2S_ActionRequest\/GroundTargeted\((.{6})\).*actionId=08ce', line)
    if addExtracted(tempstring) != None :
        HolderArray[0] = addExtracted(tempstring)

    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActorControlSelf\((.{6})\).*actionId=08ce', line)
    if addExtracted(tempstring) != None :
        HolderArray[9] = addExtracted(tempstring)

    tempstring = re.findall('\d{4}.*IpcTypeFinder.*C2S_ActionRequest\/GroundTargeted\((.{6})\).*actionId=0df1', line)
    if addExtracted(tempstring) != None :
        HolderArray[1] = addExtracted(tempstring)

    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActorCast\((.{6})\).*actionId=0078', line)
    if addExtracted(tempstring) != None :
        HolderArray[7] = addExtracted(tempstring)

    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActorControl\((.{6})\).*actionId=0078', line)
    if addExtracted(tempstring) != None :
        HolderArray[8] = addExtracted(tempstring)


    
    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActionEffect01\((.{6})\)\slength=9c', line)
    if addExtracted(tempstring) != None :
        HolderArray[2] = addExtracted(tempstring)
    
    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActionEffect08\((.{6})\)\slength=29c', line)
    if addExtracted(tempstring) != None :
        HolderArray[3] = addExtracted(tempstring)

    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActionEffect16\((.{6})\)\slength=4dc', line)
    if addExtracted(tempstring) != None :
        HolderArray[4] = addExtracted(tempstring)
    
    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActionEffect24\((.{6})\)\slength=71c', line)
    if addExtracted(tempstring) != None :
        HolderArray[5] = addExtracted(tempstring)
    
    tempstring = re.findall('\d{4}.*IpcTypeFinder.*S2C_ActionEffect32\((.{6})\)\slength=95c', line)
    if addExtracted(tempstring) != None :
        HolderArray[6] = addExtracted(tempstring)

print(HolderArray, "\n")
print("{")
print("	\"C2S_ActionRequest\": \"" + HolderArray[0]+ "\",")
print("	\"C2S_ActionRequestGroundTargeted\": \"" + HolderArray[1]+ "\",")
print("	\"Common_UseOodleTcp\": true,")
print("	\"PatchCode\": [],")
print("	\"S2C_ActionEffect01\": \"" + HolderArray[2]+ "\",")
print("	\"S2C_ActionEffect08\": \"" + HolderArray[3]+ "\",")
print("	\"S2C_ActionEffect16\": \"" + HolderArray[4]+ "\",")
print("	\"S2C_ActionEffect24\": \"" + HolderArray[5]+ "\",")
print("	\"S2C_ActionEffect32\": \"" + HolderArray[6]+ "\",")
print("	\"S2C_ActorCast\": \"" + HolderArray[7]+ "\",")
print("	\"S2C_ActorControl\": \"" + HolderArray[8]+ "\",")
print("	\"S2C_ActorControlSelf\": \"" + HolderArray[9]+ "\",")
print("	\"Server_IpRange\": \"0.0.0.0/0\",")
print("	\"Server_PortRange\": \"1-65535\"")
print("}\n")

input("Press Enter to continue...")