class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = {
            'a': ".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."
        }
        
        sets = set()
        for word in words:
            temp = []
            for letter in word:
                temp.append(codes[letter])
            sets.add("".join(temp))
            
        return len(sets)