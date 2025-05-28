package leet

func gcd(a int, b int) int {
	if b != 0 {
		a, b = b, a%b
	}
	return a
}

func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}

	g := gcd(len(str1), len(str2))

	return str1[:g]
}
