package main

import "fmt"

// consumer
type Warehouse struct {
}

type Shipper interface {
	Ship(items []string)
}

func (w Warehouse) processOrder(s Shipper, items []string) {
	fmt.Printf("processing order of items %s..\n", items)
	s.Ship(items)
}

// producer 1
type Fedex struct {
}

func (f Fedex) Ship(items []string) {
	fmt.Printf("shipping items %s via Fedex\n", items)
}

// producer 2
type UPS struct {
}

func (f UPS) Ship(items []string) {
	fmt.Printf("shipping items %s via UPS\n", items)
}

func main() {
	// following https://bryanftan.medium.com/accept-interfaces-return-structs-in-go-d4cab29a301b

	// consumer defines interface it wants, and accepts it
	// producers implement (but do not define) interface

	// benefit: allows consumer to program to interface
	// benefit: similar to hexagonal architecture
	warehouse := Warehouse{}

	warehouse.processOrder(Fedex{}, []string{"item 1", "item 2"})
	warehouse.processOrder(UPS{}, []string{"item 1", "item 2"})

	// note: "return structs" is not represented in the example above
}
