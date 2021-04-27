package testAlgo_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestTestCoWa(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "TestAlgo Suite")
}
