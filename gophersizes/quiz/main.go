package main

import (
	"bufio"
	"encoding/csv"
	"flag"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strings"
	"time"
)

type problem struct {
	Question string
	Answer   string
}

func main() {
	var filename string
	flag.StringVar(&filename, "filename", "problems.csv", "filename of the CSV source of problems (question,answer)")
	flag.StringVar(&filename, "f", "problems.csv", "Short form of filename flag.")

	timeLimit := flag.Int("limit", 30, "time limit in seconds")

	shuffleFlag := flag.Bool("shuffle", false, "shuffle the problems")

	flag.Parse()

	lines := readCsv(filename)
	problems := parseProblems(lines)
	if *shuffleFlag {
		shuffle(problems)
	}

	timer := time.NewTimer(time.Duration(*timeLimit) * time.Second)

	quiz(problems, timer)
}

func shuffle(ps []problem) {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))

	// Fisher-Yates shuffle algorithm
	for i := len(ps) - 1; i > 0; i-- {
		j := r.Intn(i + 1)
		ps[i], ps[j] = ps[j], ps[i]
	}
}

func quiz(problems []problem, t *time.Timer) {
	score := 0

problemLoop:
	for i, p := range problems {
		fmt.Printf("Problem #%d: %s = ", i+1, p.Question)

		answerCh := make(chan string)

		go func() {
			reader := bufio.NewReader(os.Stdin)
			input, err := reader.ReadString('\n')
			if err != nil {
				log.Fatal("An error occurred while reading input: ", err)
			}

			answerCh <- strings.TrimSuffix(input, "\n")
		}()

		select {
		case <-t.C:
			fmt.Println()
			break problemLoop
		case answer := <-answerCh:
			if answer == p.Answer {
				score += 1
			}
		}
	}

	fmt.Printf("You scored %d out of %d.", score, len(problems))
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
