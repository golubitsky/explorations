package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strings"
)

type problem struct {
	Question string
	Answer   string
}

func main() {
	filename := "problems.csv"
	problems := readProblems(filename)

	score := 0
	for i, p := range problems {
		if waitForResponseAndScoreProblem(p, i+1) {
			score += 1
		}
	}

	fmt.Printf("You scored %d out of %d.", score, len(problems))
}

func waitForResponseAndScoreProblem(p problem, n int) bool {
	fmt.Print("Problem #", n, ": ", p.Question, " = ")
	reader := bufio.NewReader(os.Stdin)
	// ReadString will block until the delimiter is entered
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal("An error occurred while reading input: ", err)
	}

	input = strings.TrimSuffix(input, "\n")

	return input == p.Answer
}
func readProblems(filename string) []problem {
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal("Cannot open file:", err)
	}

	defer file.Close()

	reader := csv.NewReader(file)

	records, err := reader.ReadAll()

	if err != nil {
		log.Fatal("Cannot read rows in ", filename, ": ", err)
	}

	problems := []problem{}

	for _, r := range records {
		problem := problem{
			Question: r[0],
			Answer:   r[1],
		}
		problems = append(problems, problem)
	}

	return problems
}
