class Solution:
    def getHint(self, secret: str, guess: str) -> str:
            bulls , cows = 0 , 0
            possible_cow,possible_guessed_cow = "",""
            for i in range(len(secret)):
                if secret[i] == guess[i]:
                    bulls += 1
                else:
                    possible_cow += secret[i]
                    possible_guessed_cow += guess[i]
            possible_guessed_cow = Counter(possible_guessed_cow)
            for x in possible_cow:
                if possible_guessed_cow[x] > 0:    
                    cows += 1
                    possible_guessed_cow[x] -= 1

            s = [str(bulls) , "A" , str(cows) , "B"]
            return "".join(s)
                
                    