1. NIN use Death Blossom(AoE)
	- C2S_ActionRequest
	- S2C_ActorControlSelf
2. WHM Use Asylem(Dome)
	- C2S_ActionRequestGroundTargeted
3. WHM Use Cure1 then cancel by move
	- S2C_ActorCast
	- S2C_ActorControl
4. go to Satasha, AoE adds -> 1, 2-8, 9-12, 17-24, 32+
	- S2C_ActionEffect01
	- S2C_ActionEffect08
	- S2C_ActionEffect16
	- S2C_ActionEffect24
	- S2C_ActionEffect32
5. clear text in '__string.txt__' -> paste log from alex -> save
6. run '__alex_regex.py__'
---
```
NIN use Death Blossom(AoE) actionId=08ce : C2S_ActionRequest + S2C_ActorControlSelf
2025-03-31 17:19:28.971	IpcTypeFinder	15f4: C2S_ActionRequest/GroundTargeted(0x0283): actionId=08ce sequence=0022
2025-03-31 17:19:29.187	IpcTypeFinder	15f4: S2C_ActorControlSelf(0x00b2): Cooldown: actionId=08ce duration=2.12s


WHM Use Asylem(Dome) actionId=0df1 : C2S_ActionRequestGroundTargeted
2025-03-31 17:22:04.738	IpcTypeFinder	15f4: C2S_ActionRequest/GroundTargeted(0x01ef): actionId=0df1 sequence=0023
2025-03-31 17:23:43.719	IpcTypeFinder	15f4: C2S_ActionRequest/GroundTargeted(0x01ef): actionId=0df1 sequence=0024

W

WHM Use Cure1 then cancle by move actionId=0078 : S2C_ActorControl
2025-03-31 17:28:06.949	IpcTypeFinder	15f4: S2C_ActorControl(0x026f): CancelCast: actionId=0078

AoE : S2C_ActionEffectxx

       1 tagets length: 9c	S2C_ActionEffect01


	9-16 tagets length:4dc	S2C_ActionEffect16
2025-03-31 17:38:02.595	IpcTypeFinder	15f4: S2C_ActionEffect16(0x02b8) length=4dc actionId=08dd sequence=002c wait=0.600
	
   17-24 tagets length:71c	S2C_ActionEffect24
2025-03-31 17:39:04.044	IpcTypeFinder	15f4: S2C_ActionEffect24(0x016c) length=71c actionId=0911 sequence=002d wait=0.600

   32+	 tagets length:95c	S2C_ActionEffect32
2025-03-31 17:40:11.794	IpcTypeFinder	15f4: S2C_ActionEffect32(0x0217) length=95c actionId=0911 sequence=002e wait=0.600



{
	"C2S_ActionRequest": "0x0283",
	"C2S_ActionRequestGroundTargeted": "0x01ef",
	"Common_UseOodleTcp": true,
	"PatchCode": [],
	"S2C_ActionEffect01": "0x01bf",
	"S2C_ActionEffect08": "0x0104",
	"S2C_ActionEffect16": "0x02b8",
	"S2C_ActionEffect24": "0x016c",
	"S2C_ActionEffect32": "0x0217",
	"S2C_ActorCast": "0x007b",
	"S2C_ActorControl": "0x026f",
	"S2C_ActorControlSelf": "0x00b2",
	"Server_IpRange": "0.0.0.0/0",
	"Server_PortRange": "1-65535"
}
```

---