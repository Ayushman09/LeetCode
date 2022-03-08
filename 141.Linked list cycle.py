def hasCycle(head) -> bool:
        # Using two-pointer method
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while fast.next and fast.next.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    return slow == fast


        #using Hashing (Dictionary)
def hasCycle(head):
     d={}
     temp=head
     while temp:
        if temp in d.keys():
            return True
        else:
            d[temp]=1
        temp=temp.next
     return False   