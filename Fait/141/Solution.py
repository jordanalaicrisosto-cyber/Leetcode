from typing import Optional
from ListNode import ListNode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None :
            return False
        len = 0

        tail = head
        memorize = []
        while tail.next != None :
            for node in memorize :
                if node is tail :
                    return True
            assert -10**5 <= tail.val <= 10**5
            len += 1
            memorize.append(tail)
            tail = tail.next

        assert 0 <= len <= 10**4

        return False
