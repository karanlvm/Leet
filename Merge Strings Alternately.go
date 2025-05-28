package leet

import "strings"

func mergeAlternately(word1 string, word2 string) string {
	var b strings.Builder
	i, j := 0, 0
	n1, n2 := len(word1), len(word2)

	for i < n1 && j < n2 {
		b.WriteByte(word1[i])
		b.WriteByte(word2[j])
		i++
		j++
	}

	if i < n1 {
		b.WriteString(word1[i:])
	}

	if j < n2 {
		b.WriteString(word2[j:])
	}

	return b.String()
}
