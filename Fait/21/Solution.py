from ListNode import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None :
            return list2
        if list2 == None :
            return list1

        len1 = 1
        len2 = 1
        pList1 = list1
        pList2 = list2


        while pList1.next != None :
            len1 += 1
            assert -100 <= pList1.val <= 100
            assert pList1.val <= pList1.next.val
            pList1 = pList1.next
        while pList2.next != None :
            len2 += 1
            assert -100 <= pList2.val <= 100
            assert pList2.val <= pList2.next.val
            pList2 = pList2.next
        assert len1 <= 50 and len2 <= 50

        pList1 = list1
        pList2 = list2
        merge = ListNode(min(pList1.val, pList2.val))
        pMerge = merge
        if pMerge.val == pList1.val :
            pList1 = pList1.next
        else :
            pList2 = pList2.next

        while pList1 != None and pList2 != None :
            pMerge.next = ListNode(min(pList1.val, pList2.val))
            pMerge = pMerge.next
            if pMerge.val == pList1.val :
                pList1 = pList1.next
            else :
                pList2 = pList2.next

        if pList1 != None :
            while pList1 != None :
                pMerge.next = pList1
                pMerge = pMerge.next
                pList1 = pList1.next
        elif pList2 != None :
            while pList2 != None :
                pMerge.next = pList2
                pMerge = pMerge.next
                pList2 = pList2.next
        """
        pMerge = merge
        while pMerge != None :
            print(pMerge.val)
            pMerge = pMerge.next
        print("\n")
        """
        return merge
