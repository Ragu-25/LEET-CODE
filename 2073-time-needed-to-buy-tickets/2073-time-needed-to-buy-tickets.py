class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        q=list(range(len(tickets)))
        while q:
            person=q.pop(0)
            tickets[person]-=1
            time+=1
            if tickets[person]==0 and k==person:
               return time
            if tickets[person]>0:
               q.append(person) 
        return time       
