
                if kth is None:
                    return dummy.next

            group_next = kth.next

            # Reverse the group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous group to reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp