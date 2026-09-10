
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum


                if current_sum == target:
                    return current_sum


                elif current_sum < target:
                    left += 1


                else:
                    right -= 1

        return closest