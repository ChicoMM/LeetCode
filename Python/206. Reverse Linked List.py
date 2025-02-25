class Solution:
    def reverseList(self, head):
        new = None
        while head:
            nextnode = head.next
            head.next = new
            new = head
            head = nextnode 
        return new