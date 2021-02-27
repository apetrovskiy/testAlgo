package ch01

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	"testing"
)

func TestFactorial(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Algorithms Suite")
}

var _ = Describe("Factorial", func() {
	Context("initially", func() {
		It("of 4", func() {})
		Specify("result is equal to 24",func(){})
	})
	/*Context("initially", func() {
		It("has 00 items", func() {})
		If("has 0 units", func() {})
		Specify("the total amount is 0.00", func() {})
	})*/
})
