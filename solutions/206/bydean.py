class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prevNode = None

        while curr:
            
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode

        return prevNode