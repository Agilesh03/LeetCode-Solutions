                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result