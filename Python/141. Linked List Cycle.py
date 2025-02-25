class Solution:
    def hasCycle(self, head):
        ahead = head
        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next
            if head == ahead:
                return True
        return False