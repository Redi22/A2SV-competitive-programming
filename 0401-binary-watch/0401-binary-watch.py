class Solution:
    def bk(self, i, valids, turned_on, hr, minute):
        if turned_on == 0 and hr < 12 and minute < 60:
            generated_minute = str(minute)
            if minute < 10:
                generated_minute = "0" + generated_minute
                
            valids.add(str(hr) + ":" + generated_minute)
            return
        
        if turned_on < 0 or i > 9 or hr >= 12 or minute >= 60:
            return 
        
        if i < 4:
            new_hr = hr | (1 << (3 - i))
            self.bk(i + 1, valids, turned_on - 1, new_hr, minute)
            self.bk(i + 1, valids, turned_on, hr, minute)
        else:
            new_minute = minute | (1 << (5 - (i - 4)))
            self.bk(i + 1, valids, turned_on - 1, hr, new_minute)
            self.bk(i + 1, valids, turned_on, hr, minute)
            
            
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        valids = set()
        self.bk(0, valids, turnedOn, 0, 0)
        
        return sorted(valids)