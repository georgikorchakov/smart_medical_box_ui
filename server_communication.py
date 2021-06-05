import zmq


class ServerCommunication():
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5555")

    def setValue(self, command, parameter):
        self.socket.send(command.encode('ascii'))
        message = self.socket.recv() # Handle "OK"
        self.socket.send(str(parameter).encode('ascii'))
        message = self.socket.recv() # Handle "OK"
    
    def getValue(self, command):
        self.socket.send(command.encode('ascii'))
        return self.socket.recv()
    
    def setClockSeconds(self, seconds):
        self.setValue("SET_CLOCK_SECONDS", seconds)

    def setClockMinutes(self, minutes):
        self.setValue("SET_CLOCK_MINUTES", minutes)

    def setClockHour(self, hour):
        self.setValue("SET_CLOCK_HOUR", hour)

    def setClockDayOfWeek(self, day_of_week):
        self.setValue("SET_CLOCK_DAY_OF_WEEK", day_of_week)

    def setClockDayOfMonth(self, day_of_month):
        self.setValue("SET_CLOCK_DAY_OF_MONTH", day_of_month)

    def setClockMonth(self, month):
        self.setValue("SET_CLOCK_MONTH", month)

    def setClockYear(self, year):
        self.setValue("SET_CLOCK_YEAR", year)

    def getClockSeconds(self):
        return int(self.getValue("GET_CLOCK_SECONDS"))

    def getClockMinutes(self):
        return int(self.getValue("GET_CLOCK_MINUTES"))

    def getClockHour(self):
        return int(self.getValue("GET_CLOCK_HOUR"))

    def getClockDayOfWeek(self):
        return int(self.getValue("GET_CLOCK_DAY_OF_WEEK"))

    def getClockDayOfMonth(self):
        return int(self.getValue("GET_CLOCK_DAY_OF_MONTH"))

    def getClockMonth(self):
        return int(self.getValue("GET_CLOCK_MONTH"))

    def getClockYear(self):
        return int(self.getValue("GET_CLOCK_YEAR"))

    def disableAutomaticBox(self):
        self.getValue("DISABLE_AUTOMATIC_BOX")

    def enableAutomaticBox(self):
        self.getValue("ENABLE_AUTOMATIC_BOX")

    def openBox(self, power_segment, servo_control_line):
        self.socket.send(b"OPEN_BOX")
        message = self.socket.recv() # Handle "OK"
        self.socket.send(str(power_segment).encode('ascii'))
        message = self.socket.recv() # Handle "OK"
        self.socket.send(str(servo_control_line).encode('ascii'))
        message = self.socket.recv() # Handle "OK"

    def closeBox(self, power_segment, servo_control_line):
        self.socket.send(b"CLOSE_BOX")
        message = self.socket.recv() # Handle "OK"
        self.socket.send(str(power_segment).encode('ascii'))
        message = self.socket.recv() # Handle "OK"
        self.socket.send(str(servo_control_line).encode('ascii'))
        message = self.socket.recv() # Handle "OK"

    def closeBoxAll(self):
        self.getValue("CLOSE_BOX_ALL")

    def openInsulinDay(self):
        self.getValue("OPEN_INSULIN_DAY")

    def closeInsulinDay(self):
        self.getValue("CLOSE_INSULIN_DAY")

    def openInsulinNight(self):
        self.getValue("OPEN_INSULIN_NIGHT")

    def closeInsulinNight(self):
        self.getValue("CLOSE_INSULIN_NIGHT")

    def getNormalIntervalByName(self, interval_name):
        interval = {
            "interval_name": interval_name, 
            "is_empty": 1, 
            "active": 0, 
            "time_start_h": 0, 
            "time_start_m": 0, 
            "time_end_h": 0, 
            "time_end_m": 0
        }

        self.getValue("GET_NORMAL_INTERVAL_BY_NAME")
        interval["is_empty"] = int(self.getValue(interval_name))

        print(interval)

        if interval["is_empty"] == 1:
            return interval
        
        interval["active"] = int(self.getValue("ACTIVE"))
        interval["time_start_h"] = int(self.getValue("TIME_START_H"))
        interval["time_start_m"] = int(self.getValue("TIME_START_M"))
        interval["time_end_h"] = int(self.getValue("TIME_END_H"))
        interval["time_end_m"] = int(self.getValue("TIME_END_M"))

        print(interval)

        return interval

    def setOrUpdateNormalInterval(self, interval_name, time_start_h, time_start_m, time_end_h, time_end_m, active):
        self.getValue("SET_OR_UPDATE_NORMAL_INTERVAL")
        self.getValue(interval_name)
        self.getValue(str(time_start_h))
        self.getValue(str(time_start_m))
        self.getValue(str(time_end_h))
        self.getValue(str(time_end_m))
        self.getValue(str(active))

    def getInsulinIntervalByNumberAndType(self, interval_number, insulin_type):
        insulin_interval = {
            "interval_number": interval_number, 
            "insulin_type": insulin_type, 
            "is_empty": 1, 
            "time_start_h": 0, 
            "time_start_m": 0, 
            "time_end_h": 0, 
            "time_end_m": 0
        }

        self.getValue("GET_INSULIN_INTERVAL_BY_NUMBER_AND_TYPE")
        self.getValue(str(interval_number))
        insulin_interval["is_empty"] = int(self.getValue(str(insulin_type)))

        if insulin_interval["is_empty"] == 1:
            return insulin_interval
        
        insulin_interval["time_start_h"] = int(self.getValue("TIME_START_H"))
        insulin_interval["time_start_m"] = int(self.getValue("TIME_START_M"))
        insulin_interval["time_end_h"] = int(self.getValue("TIME_END_H"))
        insulin_interval["time_end_m"] = int(self.getValue("TIME_END_M"))


        return insulin_interval

    def setOrUpdateInsulinInterval(self, interval_number, insulin_type, time_start_h, time_start_m, time_end_h, time_end_m):
        self.getValue("SET_OR_UPDATE_INSULIN_INTERVAL")
        self.getValue(str(interval_number))
        self.getValue(str(insulin_type))
        self.getValue(str(time_start_h))
        self.getValue(str(time_start_m))
        self.getValue(str(time_end_h))
        self.getValue(str(time_end_m))

    def deleteInsulinIntervalByNumberAndType(self, interval_number, insulin_type):
        self.getValue("DELETE_INSULIN_INTERVAL_BY_NUMBER_AND_TYPE")
        self.getValue(str(interval_number))
        self.getValue(str(insulin_type))