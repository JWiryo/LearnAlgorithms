class removeNthFromLinkedList:

    # 1 Pointer two-pass Solution
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head, n):
      
      # Edge Case
      if not head:
        return None
      
      # Setup Variables
      root = head
      pointer = head
      length = 0
      
      # Calculate length of linkedlist
      while pointer:
        
        # Increase length
        length += 1
        # Move pointer
        pointer = pointer.next
      
      # Edge Case again
      if length == n:
        return head.next
      
      # Calculate which node to delete
      nodeToDel = length - n
      
      # Reset Pointer
      pointer = root
      
      # Setup Count
      count = 0
      
      while count != nodeToDel-1:
        
        # Move pointer forward
        count += 1
        pointer = pointer.next
      
      # Remove next node
      nextNode = pointer.next.next
      pointer.next = nextNode
      
      return head