package main

import (
	"bufio"
	"encoding/csv"
	"flag"
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
	var filename string
	flag.StringVar(&filename, "filename", "problems.csv", "Specify the filename of the CSV source of problems.")
	flag.StringVar(&filename, "f", "problems.csv", "Short form of filename flag.")
	flag.Parse()

	lines := readCsv(filename)
	problems := parseProblems(lines)

	quiz(problems)
}

func quiz(problems []problem) {
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

func readCsv(filename string) [][]string {
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal("Cannot open file:", err)
	}

	defer file.Close()

	reader := csv.NewReader(file)

	lines, err := reader.ReadAll()

	if err != nil {
		log.Fatal("Cannot read rows in ", filename, ": ", err)
	}

	return lines
}

func parseProblems(lines [][]string) []problem {
	problems := make([]problem, len(lines))

	for i, r := range lines {
		problems[i] = problem{
			Question: r[0],
			Answer:   r[1],
		}
	}

	return problems
}
