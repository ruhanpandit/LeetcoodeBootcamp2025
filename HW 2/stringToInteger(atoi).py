class Solution:
    def myAtoi(self, s: str) -> int:

        final = ""
        cleaned = s.lstrip()

        if(len(cleaned) == 0):
            return 0

        if(cleaned[0] == "-"):
            final += "-"
            cleaned = cleaned[1:]
        elif(cleaned[0] == "+"):
            cleaned = cleaned[1:]
        
        if(len(cleaned) == 0):
            return 0
        
        firstNum = False
        end = False
        curr = 0
        while (end == False):
            if(cleaned[curr] == "0" and firstNum == True):
                final += cleaned[curr]
            elif (curr != "0"):
                if (cleaned[curr].isdigit() == True):
                    firstNum = True
                    final += cleaned[curr]
                else:
                    end = True
            
            if(curr == len(cleaned)-1):
                end = True
            curr += 1

        if (len(final) == 0):
            return 0
        
        try:
            if (int(final) < -2**31):
                return -2**31
            elif (int(final) > (2**31)-1):
                return (2**31)-1
            else:
                return int(final)
        except Exception as e:
            return 0