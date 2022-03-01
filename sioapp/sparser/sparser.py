# from ast import literal_eval\
import json
import math
# import pprint
from datetime import datetime
import time
from sioapp.mongodb import collection
from sioapp.sparser.deviceRouting import routingInfoFordevice
from sioapp.iot.IOT_MQTT.certificate import pubsub


#If in development environment set flag to True to see 
SHOW = False

#If Customer needs iot based data then set flag to True
data_pub = False

class SerialData():
    
    def __init__(self, raw_str):
        self.initial = 0
        self.raw_str = raw_str["pan"]
        self.dev_mac = ""
        self.arr = ""
        self.depth = ""
        self.child = 256
        self.dt = True
        self.afi_data = self.end_afi_data = {}
        self.sync_time = ""
        self.rssi = ""
        self.r = ""
        self.n = ""
    
    def parse(self):
        conti = True
        if "!" == self.raw_str[0]:
            IField = self.initial
            REPEATER = "0200"
            REPEATERMODE = "06"
            
            b_data = {
                "DATEANDTIME": datetime.utcnow().strftime('%Y:%m:%d:%H:%M:%S.%f')[:-3],
                "RAW": self.raw_str,
                "SOL(A)": 1,
                "MSGID(D)": 4,
                "SYSTEMID(H)": 8,
                "UARTPKLGTH(D)": 4,
                "UARTPKTYPE(H)": 2,
                "UARTPKFRAMEID(H)": 2,
                "GWHUBMAC(D)": 6,
                "PANMAC(D)": 6,
            }

            basic_data = b_data.copy()
            i = 0
            for item, l in basic_data.items():
                i+=1
                if i > 2:
                    basic_data_val = self.raw_str[IField:IField+l]
                    if '(D)' not in item:
                        basic_data[item] = basic_data_val
                    elif '(D)' in item:
                        basic_data[item] = int(basic_data_val, 16)
                    IField = IField + l
            
            Lfield = 6
            DMAC = int(self.raw_str[IField:IField+Lfield], 16)

            IField = IField + Lfield
            Lfield = 4
            RPTT = self.device_type = self.raw_str[IField:IField+Lfield]

            IField = IField + Lfield
            Lfield = 2
            RPTM = self.device_mode = self.raw_str[IField:IField+Lfield]

            IField = IField + Lfield
            Lfield = 2
            AFI = self.app_frame_id = self.raw_str[IField:IField+Lfield]

            if "6C" not in basic_data["UARTPKTYPE(H)"]:
                IField = IField + Lfield
                Lfield = 2
                self.repeater_dl_info = self.raw_str[IField:IField+Lfield]

                if REPEATER == RPTT and REPEATERMODE == RPTM :
                    IField = IField + Lfield
                    Lfield = int(self.repeater_dl_info) * 2
                    REPEATERADD = self.raw_str[IField:IField+Lfield]
                elif RPTT in routingInfoFordevice.keys():
                    a_d = routingInfoFordevice.get(RPTT)[RPTT][1].get(AFI)
                    self.afi_data = a_d.copy()
                    
                    self.afi_meta_data(IField, self.afi_data)
                    conti = False
            else:
                self.sixC(IField, Lfield)
                conti = False

            if conti:
                IField = IField + Lfield
                Lfield = 6
                self.dev_mac = int(self.raw_str[IField:IField+Lfield], 16)

                IField = IField + Lfield
                Lfield = 4
                EDT = self.end_device_type = self.raw_str[IField:IField+Lfield]

                IField = IField + Lfield
                Lfield = 2
                EDM = self.end_device_mode = self.raw_str[IField:IField+Lfield]

                IField = IField + Lfield
                Lfield = 2
                EAFI = self.end_app_frame_id = self.raw_str[IField:IField+Lfield]

                if EDT in routingInfoFordevice.keys():
                    IField = IField + Lfield
                    e_a_d = routingInfoFordevice.get(EDT)[EDT][1].get(EAFI)
                    self.end_afi_data = e_a_d.copy()
                    self.afi_meta_data(IField, self.end_afi_data)

            rpt_data = {
                "RPTMAC(D)": DMAC,
                "RPTDEVICETYPE(H)": self.deviceType(routingInfoFordevice),
                "RPTDEVICEMODE(H)": self.deviceMode(routingInfoFordevice),
                "RPTAPPFRAMEID(H)": self.appFrameId(routingInfoFordevice),
                "C(D)": self.n_children(routingInfoFordevice),
                "DL(D)": int(self.depth, 16) if self.depth else "No Depth Level",
                "RA(H)": self.arr if self.depth else "No Repeater Address",
                "DEVICEMAC(D)": self.dev_mac,
                "DEVICETYPE(H)": self.endDeviceType(routingInfoFordevice),
                "DEVICEMODE(H)": self.endDeviceMode(routingInfoFordevice),
                "APPFRAMEID(H)": self.endAppFrameId(routingInfoFordevice),
            }

            end_data = {
                "DEVICEMAC(D)": DMAC,
                "DEVICETYPE(H)": self.deviceType(routingInfoFordevice),
                "DEVICEMODE(H)": self.deviceMode(routingInfoFordevice),
                "APPFRAMEID(H)": self.appFrameId(routingInfoFordevice),
            }

            sync_data = {
                "DEVICEMAC(D)": DMAC,
                "DEVICETYPE(H)": self.deviceType(routingInfoFordevice),
                "DEVICEMODE(H)": self.deviceMode(routingInfoFordevice),
                "APPFRAMEID(H)": self.appFrameId(routingInfoFordevice),
                "GMTTIMELIVE(T)": self.sync_time,
                "RSSI(D)(dBm)": self.rssi, 
                "CR(A)": self.r,
                "LF(A)": self.n

            }

            if "6C" in basic_data["UARTPKTYPE(H)"]:
                data = basic_data | sync_data

                # if data_pub:
                #     pubsub.myMQTTClient.publish("info", json.dumps(data), 1)
                #     pubsub.myMQTTClient.publish("info", json.dumps(self.sixD()), 1)
                
                collection.insert_many([data,self.sixD()])
                return True
                # return data, self.sixD()
                # return pprint.pp(data), self.sixD()
            elif RPTT == REPEATER and RPTM == REPEATERMODE:
                data = basic_data | rpt_data | self.end_afi_data
            else:
                data = basic_data | end_data | self.afi_data

            if data_pub:
                try:
                    pubsub.myMQTTClient.publish("info", json.dumps(data), 1)
                except:
                    print("raise: publishTimeoutException() AWSIoTPythonSDK.exception.AWSIoTExceptions.publishTimeoutException")
            collection.insert_one(data)
            return data
            # return pprint.pp(data)

    def n_children(self, routing_device):
        app_frame_id_repeater = "07"
        try:
            if app_frame_id_repeater in routing_device.get(self.device_type)["deviceMode"][self.device_mode]["applicationFrameType"].keys() and not SHOW:
                ASIZE, BSIZE = 45, 47
                for i, x in enumerate(range(int(self.repeater_dl_info)+1)):
                    ASIZE = ASIZE + 2
                    BSIZE = BSIZE + 2
                    if i == 0:
                        self.depth = self.depth + str(self.raw_str[ASIZE:BSIZE])
                        # self.depth = int(self.depth)

                    if i != 0:
                        self.arr = self.arr + str(self.raw_str[ASIZE:BSIZE])

                return self.child
            # if SHOW:
            #     return f'{routing_device.get(self.device_type)["deviceMode"][self.device_mode]["applicationFrameType"][self.app_frame_id]}, {self.app_frame_id}'
        except:
            return 'Invalid Information For Repeater' 
        # val = 512
        # bits = []
        # for x in range(8):
        #     val = val/2
        #     bits.append(int(val))

        # if C in range(256):
        #     pass

    # DEVICE TYPE FUNCTIONALITY
    def deviceType(self, routing_device):
        try:
            if self.device_type in routing_device.keys() and not SHOW:
                return self.device_type

            # Teseting flag
            if SHOW:
                return f'{routing_device.get(self.device_type)[self.device_type][0]}, {self.device_type}'
        except:
            return 'Invalid RPT Device Type'
    
    # END DEVICE TYPE FUNCTIONALITY
    def endDeviceType(self, routing_device):
        try:
            if self.end_device_type in routing_device.keys() and not SHOW:
                return self.end_device_type

            # Teseting flag
            if SHOW:
                return f'{routing_device.get(self.end_device_type)[self.end_device_type][0]}, {self.end_device_type}'
        except:
            return 'Invalid End Device Type'

    # DEVICE MODE FUNCTIONALITY
    def deviceMode(self, routing_device):
        try:
            if self.device_mode in routing_device.get(self.device_type)["deviceMode"].keys() and not SHOW:
                return self.device_mode
            if SHOW:
                return f'{routing_device.get(self.device_type)["deviceMode"][self.device_mode][self.device_mode][0]}, {self.device_mode}'
        except:
            return 'Invalid Device Mode'

    # END DEVICE MODE FUNCTIONALITY
    def endDeviceMode(self, routing_device):
        try:
            if self.end_device_mode in routing_device.get(self.end_device_type)["deviceMode"].keys() and not SHOW:
                return self.end_device_mode
            if SHOW:
                return f'{routing_device.get(self.end_device_type)["deviceMode"][self.end_device_mode][self.end_device_mode][0]}, {self.end_device_mode}'
        except:
            return 'Invalid End Device Mode'

    # APP FRAME ID FUNCTIONALITY
    def appFrameId(self, routing_device):
        try:
            if self.app_frame_id in routing_device.get(self.device_type)["deviceMode"][self.device_mode]["applicationFrameType"].keys() and not SHOW:
                return self.app_frame_id
            if SHOW:
                return f'{routing_device.get(self.device_type)["deviceMode"][self.device_mode]["applicationFrameType"][self.app_frame_id][0]}, {self.app_frame_id}'
        except:
            return 'Invalid Device Application Frame ID'

    # END APP FRAME ID FUNCTIONALITY
    def endAppFrameId(self, routing_device):
        try:
            if self.end_app_frame_id in routing_device.get(self.end_device_type)["deviceMode"][self.end_device_mode]["applicationFrameType"].keys() and not SHOW:
                return self.end_app_frame_id
            if SHOW:
                return f'{routing_device.get(self.end_device_type)["deviceMode"][self.end_device_mode]["applicationFrameType"][self.end_app_frame_id][0]}, {self.end_app_frame_id}'
        except:
            return 'Invalid Device Application Frame ID'

    # Test
    def afi_meta_data(self, IField, afi_data):
        if IField in ("83","84"):
            print("Before  Forloop:", IField, self.raw_str)
        for item, l in afi_data.items():
            afi_data_val = self.raw_str[IField:IField+l]
            if '(D)(V)' in item:
                afi_data[item] = (int(afi_data_val, 16) + 100) / 100
            elif '(D)(dBm)' in item:
                b = bytes.fromhex(afi_data_val)
                afi_data[item] = int.from_bytes(b, byteorder= "big" ,signed=True)
            elif '(D)(℃)' in item:
                b = bytes.fromhex(afi_data_val)
                afi_data[item] = int.from_bytes(b, byteorder= "big" ,signed=True) / 10
                # elif '(D)(µA)' in item:
                #    afi_data[item] = afi_data_val
                # elif '(D)(min)' in item:
                #     afi_data[item] = afi_data_val
                # elif '(D)(MHz)' in item:
                #     afi_data[item] = afi_data_val
                # elif '(D)(sps)' in item:
                #     afi_data[item] = afi_data_val
                # elif '(D)(bps)' in item:
                #     afi_data[item] = afi_data_val
                # elif '(D)(sec)' in item:
                #     afi_data[item] = afi_data_val
                # elif '(D)(min)' in item:
                #     afi_data[item] = afi_data_val
            elif 'TSLICEVAL(D)(ms)' == item:
                afi_data[item] = afi_data[item] * 100
            elif '(T)' in item:
                raw_time = int(afi_data_val, 16)
                afi_data[item] = self.gmtTime(raw_time)
            elif '(D)' not in item:
                afi_data[item] = afi_data_val
            elif '(D)' in item:
                afi_data[item] = int(afi_data_val, 16)

            # try:
            if 'TSLICE(D)(ms)' == item:
                afi_data[item] = afi_data[item] * 100
                afi_data['TSLICEDATA(H)'] = math.ceil(afi_data['MSGINT(D)(sec)'] / ((afi_data[item])/ 1000)/8) * 2
            # except:
            #     print("NOTSLICE(D)(ms)", )

            IField = IField + l

    # Time FUNCTIONALITY
    def gmtTime(self, rawTime):
        ymd = time.strftime("%Y:%m:%d", time.gmtime())
        raw_time = ((rawTime * 10) / 1000) / 3600
        hr = int(raw_time)
        minu = int((raw_time - int(raw_time)) * 60)
        sec= round(((raw_time - int(raw_time)) * 60 - int(minu)) * 60, 3)

        return f"{ymd}:{hr:02d}:{minu:02d}:{sec:06.3f}"

    # sixC
    def sixC(self, IField, Lfield):
        
        IField = IField + Lfield
        Lfield = 6
        self.sync_time = self.gmtTime(int(self.raw_str[IField:IField+Lfield], 16))

        IField = IField + Lfield
        Lfield = 2
        b = bytes.fromhex(self.raw_str[IField:IField+Lfield]) 
        self.rssi = int.from_bytes(b, byteorder= "big" ,signed=True)

        IField = IField + Lfield
        Lfield = 1
        self.r = self.raw_str[IField:IField+Lfield]

        IField = IField + Lfield
        Lfield = 1
        self.n = self.raw_str[IField:IField+Lfield]

    # sixD
    def sixD(self):
        extra_d = {
            "DATEANDTIME": datetime.utcnow().strftime('%Y:%m:%d:%H:%M:%S.%f')[:-3],
            "RAW": "",
        }
        data = {
            "SOL(A)": 1,
            "MSGID(D)": 4,
            "SYSTEMID(H)": 8,
            "UARTPKLGTH(D)": 4,
            "UARTPKTYPE(H)": 2,
            "UARTPKFRAMEID(H)": 2,
            "GWHUBMAC(D)": 6,
            "PANMAC(D)": 6,
            "DEVICEMAC(D)": 6,
            "DEVICETYPE(H)": 4,
            "DEVICEMODE(H)": 2,
            "APPFRAMEID(H)": 2,
            "GMTTIMELIVE(T)": 6,
            "RSSI(D)(dBm)": 2, 
            "CR(A)": 1,
            "LF(A)": 1
        }
        sixd = data.copy()
        sixdd = data.copy()
        ifield = 0 
        for item, l in sixd.items():
            asci = self.raw_str[ifield:ifield+l]
            if "UARTPKTYPE(H)" in item:
                sixd[item] = "6D"
                sixdd[item] = "6D"
            elif "GMTTIMELIVE(T)" in item:
                # sixd[item] = datetime.utcnow().strftime('%Y:%m:%d:%H:%M:%S.%f')[:-3]

                time_str  = str(datetime.utcnow().strftime('%H:%M:%S.%f')[:-3])
                h, m, s = time_str.split(':')
                d_x = int((int(h) * 3600 + int(m) * 60 + float(s))*100)
                sixdd[item] = f"{d_x:06X}"

                sixd[item] = self.gmtTime(int(sixdd[item], 16))
            elif "(D)(dBm)" in item:
                sixdd[item] = asci

                b = bytes.fromhex(asci) 
                sixd[item] = int.from_bytes(b, byteorder= "big" ,signed=True)
            elif "(D)" in item:
                sixd[item] = int(asci, 16)
                sixdd[item] = asci
            elif "(D)" not in item:
                sixd[item] = asci
                sixdd[item] = asci

            ifield = ifield + l
        sixd_string = "".join(sixdd.values())
        extra_d["RAW"] = sixd_string

        sync_d = extra_d | sixd
        # pprint.pp(sync_d)
        return sync_d
