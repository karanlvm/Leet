package leet

func reverseVowels(s string) string {
	vowels := map[byte]bool{
		'a': true, 'e': true, 'i': true, 'o': true, 'u': true,
		'A': true, 'E': true, 'I': true, 'O': true, 'U': true,
	}

	str := []byte(s) // creating a slice

	i, j := 0, len(str)-1

	for i < j {
		for i < j && !vowels[str[i]] {
			i++
		}

		for i < j && !vowels[str[j]] {
			j--
		}

		str[i], str[j] = str[j], str[i]
		i++
		j--
	}
	return string(str)
}
