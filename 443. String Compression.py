class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            # Count how many times current_char repeats
            while read < n and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character itself
            chars[write] = current_char
            write += 1

            # If it repeats more than once, write the digits of count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # 'write' is now the length of the compressed array
        return write