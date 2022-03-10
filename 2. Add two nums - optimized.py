def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        ptr = result # the current node of the result list during loop
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            ptr.next = ListNode(carry%10)
            ptr = ptr.next
            carry //= 10
        return result.next
        