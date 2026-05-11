class Solution:
    def compress(self, chars: List[str]) -> int:
        n =len (chars)
        write = 0
        read = 0
        while read<n:
            count = 0
            currentChar = chars[read]
            while read<n and chars[read]==currentChar:
                count+=1
                read+=1
            if count ==1:
                chars[write]=currentChar
                write+=1
            else:
                chars[write]=currentChar
                write+=1
                strs = str(count)
                for digit in strs:
                    chars[write]=digit
                    write +=1
        return write