class Solution:
    def bitCounter(self, number):
        count = 0
        while number:
            count += (number & 1)
            number = number >> 1
            
        return count
            
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        valids = set()
        for hr in range(12):
            for minute in range(60):
                
                if self.bitCounter(hr) + self.bitCounter(minute) == turnedOn:
                    generated_minute = str(minute)
                    if minute < 10:
                        generated_minute = "0" + generated_minute

                    valids.add(str(hr) + ":" + generated_minute)
        
        return valids