from ListNode import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None :
            return list2
        if list2 == None :
            return list1

        len1 = 0
        len2 = 0
        pList1 = list1
        pList2 = list2


        while pList1.next != None :
            len1 += 1
            assert 0 <= pList1.val <= 50
            assert pList1.val <= pList1.next.val
            pList1 = pList1.next
        while pList2.next != None :
            len2 += 1
            assert 0 <= pList2.val <= 50
            assert pList2.val <= pList2.next.val
            pList2 = pList2.next
        assert len1 <= 50 and len2 <= 50

        pList1 = list1
        pList2 = list2
        merge = ListNode(min(pList1.val, pList2.val))
        if merge.val == pList1.val :
            pList1 = pList1.next
        else :
            pList2 = pList2.next

        while pList1.next != None and pList2.next != None :
            merge.next = ListNode(min(pList1.val, pList2.val))
            if merge.val == pList1.val :
                pList1 = pList1.next
            else :
                pList2 = pList2.next

        if pList1 != None :
            while pList1.next != None :
                merge.next = pList1
                pList1 = pList1.next
        else :
            while pList2 != None :
                merge.next = pList2
                pList2 = pList2.next

        pMerge = merge
        while pMerge.next != None :
            print(pMerge.val)
            pMerge = pMerge.next

        return merge
