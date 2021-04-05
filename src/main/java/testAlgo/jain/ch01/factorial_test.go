package ch01

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	"testing"
)

func TestFactorialSuite(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Algorithms Suite")
}

var _ = Describe("Factorial", func() {
	Context("initially", func() {
		It("of 4", func() {})
		Specify("result is equal to 24", func() {})
	})
	/*Context("initially", func() {
		It("has 00 items", func() {})
		If("has 0 units", func() {})
		Specify("the total amount is 0.00", func() {})
	})*/
})

func TestFactorial(t *testing.T) {
	testCases := []struct {
		input          int
		expectedResult int
	}{
		{-1, 1},
		{0, 1},
		{1, 1},
		{2, 2},
		{4, 24},
		{6, 720},
	}
	for _, tc := range testCases {
		got := Factorial(tc.input)
		if got != tc.expectedResult {
			t.Errorf("Factorial(%d) = %d; want", tc.input, got)
		}
	}
}
