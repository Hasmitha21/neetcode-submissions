# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # BRUTE FORCE

        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next
        
        # removeIndex = len(nodes) - n
        # if removeIndex == 0:
        #     return head.next
        
        # nodes[removeIndex -1].next = nodes[removeIndex].next

        # return head


        # TWO POINTERS
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next