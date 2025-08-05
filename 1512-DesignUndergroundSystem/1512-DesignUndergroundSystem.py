# Last updated: 8/5/2025, 2:54:07 PM
class UndergroundSystem:

    def __init__(self):
        self.checkin = dict()
        self.avgTime = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkin:
            self.checkin[id] = (stationName, t)
        return None

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin:
            station, time = self.checkin.get(id)
            if station + '-' + stationName not in self.avgTime:
                self.avgTime[station + '-' + stationName] = (abs(t - time), 1)
            else:
                oldtime, itr = str(self.avgTime[station + '-' + stationName]).split(',')
                oldtime = float(oldtime.strip('('))
                itr = int(itr.strip(')'))
                self.avgTime[station + '-' + stationName] = (abs(oldtime + (t - time)), itr + 1)
            self.checkin.pop(id)
        return None

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation + '-' + endStation in self.avgTime:
            time, num = str(self.avgTime[startStation + '-' + endStation]).split(',')
            time = float(time.strip('('))
            num = int(num.strip(')'))
            return time / num


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)