package ch01

func Factorial(inputValue int) int {
	if inputValue <= 1 {
		return 1
	}
	return inputValue * Factorial(inputValue-1)
}
