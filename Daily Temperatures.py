# TC: O(n)
# SC: O(n) size of the stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        mstack = []
        result = [0] * len(temperatures)

        mstack.append(0)

        i= 1
        i += 1

        for i in range(1, len(temperatures)):
            if temperatures[i-1] < temperatures[i]:
                while len(mstack) != 0  and temperatures[mstack[-1]] < temperatures[i]:
                    result[mstack[-1]] = (i - mstack[-1])
                    mstack.pop()

            mstack.append(i)
            
        return result
                    
                    
        
        
        