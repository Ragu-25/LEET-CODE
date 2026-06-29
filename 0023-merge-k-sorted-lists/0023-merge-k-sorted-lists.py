# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1,list2):
          dummy=ListNode()
          temp=dummy
          while list1 and list2:
             if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
             else:
                temp.next=list2
                list2=list2.next
             temp=temp.next         
          temp.next=list1 if list1 else list2
          return dummy.next
        ans=None
        for l in lists:
            ans=merge(ans,l)  
        return ans    