class Solution:
    def middleNode(self, head):
        ahead = head
        count=0
        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next
        return head