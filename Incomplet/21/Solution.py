from ListNode import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None :
            return list2
        if list2 == None :
            return list1
        
        nodes = ListNode()
        len1 = 0
        len2 = 0
        pList1 = list1
        pList2 = list2

        while pList1.next != None :
            len += 1
            assert 0 <= pList1.val <= 50
            assert pList1.val <= pList1.next.val
            pList1 = list1.next
        while pList2.next != None :
            len += 1
            assert 0 <= pList2.val <= 50
            assert pList2.val <= pList2.next.val
            pList2 = list2.next
        assert len <= 50
        
        return nodes