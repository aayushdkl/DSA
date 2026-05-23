if num1 == "0" or num2 == "0":
            return "0"
        
        L1, L2 = len(num1), len(num2)
        
        # Step B: Initialize the Result Array
        result = [0] * (L1 + L2)
        
        # Step C: The Nested Iteration (Right to Left)
        for i in range(L1 - 1, -1, -1):
            for j in range(L2 - 1, -1, -1):
                
                # Multiply the current single digits
                product = int(num1[i]) * int(num2[j])
                
                # Add to the existing value at the units position
                # (i + j + 1 is the units place for this specific multiplication)
                current_sum = product + result[i + j + 1]
                
                # Step D: Update Units and Carry
                result[i + j + 1] = current_sum % 10       # Update the units
                result[i + j] += current_sum // 10         # Add carry to the left
                
        # Step E: Formatting the Output
        # Find the first non-zero index to skip any leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
            
        # Convert the remaining elements to strings and join them
        return "".join(map(str, result[start:]))