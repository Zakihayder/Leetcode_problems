class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = []
        ten = []

        for i in range(len(bills)):
            if five or ten or bills[i] == 5:
                if bills[i] == 5:
                    five.append(5)
                elif bills[i] == 10:
                    ten.append(10)
                    if len(five) > 0:
                        five.pop()
                else:
                    if len(ten) > 0 and len(five) > 0:
                        ten.pop()
                        five.pop()
                    elif len(five) > 2:
                        five.pop()
                        five.pop()
                        five.pop()
                    else:
                        return False
            else:
                return False
            
        return True