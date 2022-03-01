

# Device Mode Variables 
IAS, O, S, A, D, DEVICE = "Inactive State", "Occupancy", "Security", "Activity", "Door", "RPT100 Device"
L_R, S_R, A_O_NA = "Location Response", "Sensor Response", "Activated or Not Activated"
S_D, TWO_W_V, L_P = "Social Distancing", "2 Way Voice", "Location Ping"
ELS100, ELS101, ELS201, ELS300 = "ELS100", "ELS101", "ELS201", "ELS300" 
ECS100, EMS100, RPT100 = "(Contact Sensor) ECS100", "EMS100", "RPT100 Reapeater"
NA, T, TRH, XYZ  = "N/A", "T", "T & RH", "T, P, RH, eCO2, TeVOC"

# Application Frame Type Variables 
BEACON, DATA, HB, DIAGNOSTIC, S_S = "Beacon", "Data", "HeartBeat", "Diagnostic", "Status / Settings"
PARAM0, PARAM1, CMD_T_MSG = "PARAM0", "PARAM1", "CMD Type msg"

# Application Frame Type
applicationFrameType_NA = {"00": NA, "01": NA, "81": NA, "82": NA, "83": NA, "84": NA, "85": NA, "A0": NA}
applicationFrameType = {
    "00": BEACON, 
    "01": DATA, 
    "02": DATA, 
    "03": DATA, 
    "04": DATA, 
    "05": DATA,
    "06": DATA, 
    "81": HB, 
    "82": DIAGNOSTIC, 
    "83": S_S, 
    "84": PARAM0, 
    "85": PARAM1, 
    "A0": CMD_T_MSG}
applicationFrameType_Repeater = {"00": BEACON, "07": "Application Frame Type RPT100 Reapeater DATA"}
applicationFrameType_sync = {"00": "reg", "01": DATA, "81": HB, "82": DIAGNOSTIC, "83": S_S, "84": PARAM0, "85": PARAM1}

# Device Mode
deviceMode={
        "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
        "01": {"01":O,"applicationFrameType": applicationFrameType},
        "02": {"02":S,"applicationFrameType": applicationFrameType},
        "03": {"03":A,"applicationFrameType": applicationFrameType},
        "04": {"04":D,"applicationFrameType": applicationFrameType},
        "05": {"05":L_R,"applicationFrameType": applicationFrameType},
        "06": {"06":S_R,"applicationFrameType": applicationFrameType},
    }


# Application Frame Type Device Data
BatteryActivitySensor={
        "00": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1}, 
        "01": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "02": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "03": {"DATASEQ(D)":2,"DEVICEBAT(D)(V)":2,"RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4,
            "NODESL(D)":2,"MSGINT(D)(sec)":4, "BKTLEN(D)(sec)":2, "BUCKETDATA[0](D)(Counts)":2,"BUCKETDATA[1](D)(Counts)":2,
            "TSLICE(D)(ms)": 2, "TSLICEDATA(H)":4,"GMTTIMEDATA(T)":6, "GMTTIMELIVE(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "04": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "05": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "06": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "81": {"HBSEQ(D)":2,"DEVICEBAT(D)(V)":2,"RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4,
            "HBINT(D)(sec)":4,"FWMAJOR(D)":2,"FWMINOR(D)":2,"GMTTIMELIVE(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "82": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "83": {"DEVINFOSEQ(D)":2, "DEVICEBAT(D)(V)":2, "RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4, "DEVINFOINT(D)(min)":4,"DEVPID(H)":2,
            "DEVVID(H)":2,"DEVHID(H)":20,"DEVSN(D)":6,"DEVPD(D)":6,"DEVMID(H)":8,"DEVHW(H)":2,"EVTMEMOFFSET(H)":6,"EVTIDXCNT(D)":4,"EVTIDXOVFCNT(D)":4,"EVTTCNT(D)":6,
            "INITBAT(D)(mV)":4,"NWDTR(D)":4,"PREVGWSN(D)":6,"REMODULEHID(D)":10,"RFRADIOPN(H)":4,"GMTTIMELIVE(T)":6, "RSSI(D)(dBm)":2,"CR(A)":1,"LF(A)":1,},
        "84": {"PARAMSEQ(D)":2,"DEVICEBAT(D)(V)":2,"RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4,"PARAMINT(D)(min)": 4,
            "DEVHW(H)": 2,"FWMAJOR(D)":2,"FWMINOR(D)":2,"FWBUILDMAJOR(D)":2,"FWBUILDMINOR(D)":2,"BLMAJOR(D)":2,"BLMINOR(D)":2,"BLBUILDMAJOR(D)":2,
            "BLBUILDMINOR(D)":2,"PVERMAJOR(D)":2,"PVERMINOR(D)":2,"HOMEFRB(D)":2,"HOMEFRC(D)(MHz)":4,"HOMEPRFTX(D)(dBm)":2,"HOMERFDR(D)(sps)":6,"BLFRB(D)":2,
            "BLFRC(D)(MHz)":4,"BLPRFTX(D)(dBm)":2,"BLRFDR(D)(sps)":6,"DEVUARTBAUD(D)(bps)":6,"BLUARTBAUD(D)(bps)":6,"MSGINT(D)(sec)":4,"BCNINT(D)(sec)":4,
            "HBINT(D)(sec)":4,"DEVINFOINT(D)(min)":4,"DIAGINT(D)(min)":4,"DCONTIME(T)":6,"DCOFFTIME(T)":6,"BKTLEN(D)(sec)":2,"TSLICEVAL(D)(ms)":2,"DIAGENFLG(D)":2,
            "GMTSYNCENFLG(D)":2,"LEDFLASHENFLG(D)":2,"EVTENFLG(D)":2,"BATMEASUREINT(D)(min)":4,"BATMEASUREHYST(D)(mV)":2,"IONMAX(D)(µA)":4,"IONMIN(D)(µA)":4,
            "IONOFFSET(D)(µA)":4,"BLVALIDSTATFLG(D)":2,"DEEPSLEEPSTATFLG(D)":2,"RDL(D)":2,"RRA(H)":2,"GMTTIMELIVE(T)":6,"RSSI(D)(dBm)":2,"CR(A)":1,"LF(A)":1,},
        "85": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
        "A0": {"HBSEQ":2,"DEVICEBAT(D)(V)":2,"RSSIACK":2,"AMBTTMP":4,"IRTMP":4,"ION":4,"HBINT":4,"FWMAJOR":2,"FWMINOR":2, 
            "GMTTIMEDATA(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},}


SimpleRepeater = {
    "07": {"HBSEQ(D)":2,"DEVICEBAT(D)(V)":2,"RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4,
        "HBINT(D)(sec)":4,"FWMAJOR(D)":2,"FWMINOR(D)":2,"RDL(D)":2, "RRA(H)":2,"GMTTIMELIVE(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
    "81": {"HBSEQ(D)":2,"DEVICEBAT(D)(V)":2,"RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4,
        "HBINT(D)(sec)":4,"FWMAJOR(D)":2,"FWMINOR(D)":2,"RDL(D)":2, "RRA(H)":2,"GMTTIMELIVE(T)":6,"RSSI(D)(dBm)":2, "CR(A)":1,"LF(A)":1},
    "83": {"DEVINFOSEQ(D)":2, "DEVICEBAT(D)(V)":2, "RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4, "DEVINFOINT(D)(min)":4,"DEVPID(H)":2,
            "DEVVID(H)":2,"DEVHID(H)":20,"DEVSN(D)":6,"DEVPD(D)":6,"DEVMID(H)":8,"DEVHW(H)":2,"EVTMEMOFFSET(H)":6,"EVTIDXCNT(D)":4,"EVTIDXOVFCNT(D)":4,"EVTTCNT(D)":6,
            "INITBAT(D)(mV)":4,"NWDTR(D)":4,"PREVGWSN(D)":6,"REMODULEHID(D)":10,"RFRADIOPN(H)":4, "RDL(D)":2, "RRA(H)":2, "GMTTIMELIVE(T)":6, "RSSI(D)(dBm)":2,"CR(A)":1,"LF(A)":1,},
    "84": {"PARAMSEQ(D)":2,"DEVICEBAT(D)(V)":2,"RSSIACK(D)(dBm)":2,"AMBTTMP(D)(℃)":4,"IRTMP(D)(℃)":4,"ION(D)(µA)":4,"PARAMINT(D)(min)": 4,
            "DEVHW(H)": 2,"FWMAJOR(D)":2,"FWMINOR(D)":2,"FWBUILDMAJOR(D)":2,"FWBUILDMINOR(D)":2,"BLMAJOR(D)":2,"BLMINOR(D)":2,"BLBUILDMAJOR(D)":2,
            "BLBUILDMINOR(D)":2,"PVERMAJOR(D)":2,"PVERMINOR(D)":2,"HOMEFRB(D)":2,"HOMEFRC(D)(MHz)":4,"HOMEPRFTX(D)(dBm)":2,"HOMERFDR(D)(sps)":6,"BLFRB(D)":2,
            "BLFRC(D)(MHz)":4,"BLPRFTX(D)(dBm)":2,"BLRFDR(D)(sps)":6,"DEVUARTBAUD(D)(bps)":6,"BLUARTBAUD(D)(bps)":6,"MSGINT(D)(sec)":4,"BCNINT(D)(sec)":4,
            "HBINT(D)(sec)":4,"DEVINFOINT(D)(min)":4,"DIAGINT(D)(min)":4,"DCONTIME(T)":6,"DCOFFTIME(T)":6,"BKTLEN(D)(sec)":2,"TSLICEVAL(D)(ms)":2,"DIAGENFLG(D)":2,
            "GMTSYNCENFLG(D)":2,"LEDFLASHENFLG(D)":2,"EVTENFLG(D)":2,"BATMEASUREINT(D)(min)":4,"BATMEASUREHYST(D)(mV)":2,"IONMAX(D)(µA)":4,"IONMIN(D)(µA)":4,
            "IONOFFSET(D)(µA)":4,"BLVALIDSTATFLG(D)":2,"DEEPSLEEPSTATFLG(D)":2,"RDL(D)":2,"RRA(H)":2,"GMTTIMELIVE(T)":6,"RSSI(D)(dBm)":2,"CR(A)":1,"LF(A)":1,},
}

LegacyRpiGW = {
    "00": {"GMTTIMELIVE(T)": 6,"RSSI(D)(dBm)": 2, "CR(A)": 1,"LF(A)": 1}, 
    "01": {"GMTTIMELIVE(T)": 6,"RSSI(D)(dBm)": 2, "CR(A)": 1,"LF(A)": 1}, 
}

#Routing Information
routingInfoFordevice={
    "1000": {"1000":["Legacy RPi GW", LegacyRpiGW], 
        "deviceMode":{
            "01": {"01":"Legacy RPi GW", "applicationFrameType":applicationFrameType_sync},}
        },
    "0001": {"0001":["Battery Activity Sensor", BatteryActivitySensor], "deviceMode":deviceMode,},
    "0002": {"0002":["Powered Activity Sensor", BatteryActivitySensor], "deviceMode": deviceMode,},
    "0003": {"0003":["Standard Rip Cord", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":A_O_NA,"applicationFrameType": applicationFrameType},
            "02": {"02":S_D,"applicationFrameType": applicationFrameType},
            "03": {"03":TWO_W_V,"applicationFrameType": applicationFrameType},
            "04": {"04":L_P,"applicationFrameType": applicationFrameType},}
            },
    "0004": {"0004":["Advanced Rip Cord", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":A_O_NA,"applicationFrameType": applicationFrameType},
            "02": {"02":S_D,"applicationFrameType": applicationFrameType},
            "03": {"03":TWO_W_V,"applicationFrameType": applicationFrameType},
            "04": {"04":L_P,"applicationFrameType": applicationFrameType},}
            },
    "0005": {"0005":["Water Leak Sensors", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":ELS100,"applicationFrameType": applicationFrameType},}
            },
    "0006": {"0006":["Water Leak Sensors", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":ELS101,"applicationFrameType": applicationFrameType},}
            },
    "0007": {"0007":["Water Leak Sensors", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":ELS201,"applicationFrameType": applicationFrameType},}
            },
    "0008": {"0008":["Rope Water Leak Sensor", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":ELS300,"applicationFrameType": applicationFrameType},}
            },
    "0009": {"0009":["Wireless Contact Sensor", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":ECS100,"applicationFrameType": applicationFrameType},}
            },
    "0010": {"0010":["Powered Air Quality Sensor", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":XYZ,"applicationFrameType": applicationFrameType},
            "02": {"02":T,"applicationFrameType": applicationFrameType},
            "03": {"03":TRH,"applicationFrameType": applicationFrameType},}
            },
    "0011": {"0011":["Battery Air Quality Sensor", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":NA,"applicationFrameType": applicationFrameType},
            "02": {"02":T,"applicationFrameType": applicationFrameType},
            "03": {"03":TRH,"applicationFrameType": applicationFrameType},}
            },
    "0200": {"0200":["Simple Repeater", SimpleRepeater],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":DEVICE,"applicationFrameType": applicationFrameType},
            "06": {"06":RPT100,"applicationFrameType": applicationFrameType_Repeater},}
            },
    "000A": {"000A":["Inertial Motion Sensor", BatteryActivitySensor],
        "deviceMode":{
            "00": {"00":IAS, "applicationFrameType":applicationFrameType_NA},
            "01": {"01":EMS100,"applicationFrameType": applicationFrameType},}
            },
    "000B": {"000B":["Battery Activity Sensor With T & RH", BatteryActivitySensor], "deviceMode":deviceMode,},
    "000C": {"000C":["Battery Legacy Sensor With ToF Person Counter", BatteryActivitySensor], "deviceMode":deviceMode,},
    "000D": {"000D":["Powered Legacy Sensor With ToF Person Counter", BatteryActivitySensor], "deviceMode":deviceMode,},
    "000E": {"000E":["Powered Activity Sensor With ToF Person Counter", BatteryActivitySensor], "deviceMode":deviceMode,},
    "000F": {"000F":["Powered Activity Sensor With ToF Person Counter & T&RH", BatteryActivitySensor], "deviceMode":deviceMode,},
}
