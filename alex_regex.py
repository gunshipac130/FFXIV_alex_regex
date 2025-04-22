import re

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

    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*C2S_ActionRequest\/GroundTargeted\((.{6})\).*actionId=08ce', line)
    if addExtracted(tempstring) != None :
        HolderArray[0] = addExtracted(tempstring)

    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActorControlSelf\((.{6})\).*actionId=08ce', line)
    if addExtracted(tempstring) != None :
        HolderArray[9] = addExtracted(tempstring)

    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*C2S_ActionRequest\/GroundTargeted\((.{6})\).*actionId=0df1', line)
    if addExtracted(tempstring) != None :
        HolderArray[1] = addExtracted(tempstring)

    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActorCast\((.{6})\).*actionId=0078', line)
    if addExtracted(tempstring) != None :
        HolderArray[7] = addExtracted(tempstring)

    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActorControl\((.{6})\).*actionId=0078', line)
    if addExtracted(tempstring) != None :
        HolderArray[8] = addExtracted(tempstring)

    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActionEffect01\((.{6})\)\slength=9c', line)
    if addExtracted(tempstring) != None :
        HolderArray[2] = addExtracted(tempstring)
    
    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActionEffect08\((.{6})\)\slength=29c', line)
    if addExtracted(tempstring) != None :
        HolderArray[3] = addExtracted(tempstring)

    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActionEffect16\((.{6})\)\slength=4dc', line)
    if addExtracted(tempstring) != None :
        HolderArray[4] = addExtracted(tempstring)
    
    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActionEffect24\((.{6})\)\slength=71c', line)
    if addExtracted(tempstring) != None :
        HolderArray[5] = addExtracted(tempstring)
    
    tempstring = re.findall(r'\d{4}.*IpcTypeFinder.*S2C_ActionEffect32\((.{6})\)\slength=95c', line)
    if addExtracted(tempstring) != None :
        HolderArray[6] = addExtracted(tempstring)

C2S_ActionRequest = str(HolderArray[0])  #0
C2S_ActionRequestGroundTargeted = str(HolderArray[1])    #1
S2C_ActionEffect01 = str(HolderArray[2]) #2
S2C_ActionEffect08 = str(HolderArray[3]) #3
S2C_ActionEffect16 = str(HolderArray[4]) #4
S2C_ActionEffect24 = str(HolderArray[5]) #5
S2C_ActionEffect32 = str(HolderArray[6]) #6
S2C_ActorCast = str(HolderArray[7])  #7
S2C_ActorControl = str(HolderArray[8])   #8
S2C_ActorControlSelf = str(HolderArray[9])   #9

print(HolderArray, "\n")
print("{")
print("	\"C2S_ActionRequest\": \"" + C2S_ActionRequest + "\",")
print("	\"C2S_ActionRequestGroundTargeted\": \"" + C2S_ActionRequestGroundTargeted + "\",")
print("	\"Common_UseOodleTcp\": true,")
print("	\"PatchCode\": [],")
print("	\"S2C_ActionEffect01\": \"" + S2C_ActionEffect01 + "\",")
print("	\"S2C_ActionEffect08\": \"" + S2C_ActionEffect08 + "\",")
print("	\"S2C_ActionEffect16\": \"" + S2C_ActionEffect16 + "\",")
print("	\"S2C_ActionEffect24\": \"" + S2C_ActionEffect24 + "\",")
print("	\"S2C_ActionEffect32\": \"" + S2C_ActionEffect32 + "\",")
print("	\"S2C_ActorCast\": \"" + S2C_ActorCast + "\",")
print("	\"S2C_ActorControl\": \"" + S2C_ActorControl + "\",")
print("	\"S2C_ActorControlSelf\": \"" + S2C_ActorControlSelf + "\",")
print("	\"Server_IpRange\": \"0.0.0.0/0\",")
print("	\"Server_PortRange\": \"1-65535\"")
print("}\n")

input("Press Enter to continue...")