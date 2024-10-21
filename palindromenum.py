class Solution:
    def check_palindromnumber(self, x: int) -> bool:
        # Step 1: Check if the number is negative
        if x < 0:
            return False  # Return False for negative numbers since they can't be palindromes

        reserved_num = 0  # Initialize a variable to hold the reversed number
        temp = x  # Store the original number in a temporary variable for manipulation

        # Step 2: Reverse the number
        while temp != 0:  # Continue until all digits have been processed
            digit = temp % 10  # Get the last digit of temp
            reserved_num = reserved_num * 10 + digit  # Build the reversed number
            temp //= 10  # Remove the last digit from temp

        # Step 3: Compare the original number with the reversed number
        return x == reserved_num  # Return True if they are the same, False otherwise


# Create an instance of the Solution class
palindrom = Solution()

# Call the method and print the result for a test input
result = palindrom.check_palindromnumber(123)  # Example input
print(result)  # Print the result
