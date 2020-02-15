package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	numStr, _ := reader.ReadString('\n')
	numStr = strings.TrimRight(string(numStr), "\r\n")
	numStrInt, _ := strconv.ParseInt(numStr, 10, 64)

	inpStrings := make([]string, numStrInt)
	var i int64
	for i = 0; i < numStrInt; i++ {
		tmp, _ := reader.ReadString('\n')
		tmp = strings.TrimRight(string(tmp), "\r\n")
		inpStrings[i] = tmp
	}

	numStr, _ = reader.ReadString('\n')
	numStr = strings.TrimRight(string(numStr), "\r\n")
	numStrInt, _ = strconv.ParseInt(numStr, 10, 64)

	inpQueries := make([]string, numStrInt)
	freqDict := make(map[string]int)
	for i = 0; i < numStrInt; i++ {
		tmp, _ := reader.ReadString('\n')
		tmp = strings.TrimRight(string(tmp), "\r\n")
		freqDict[tmp] = 0
		inpQueries[i] = tmp
	}
	lenStrings := len(inpStrings)
	var j int
	for j = 0; j < lenStrings; j++ {
		freqDict[inpStrings[j]] = freqDict[inpStrings[j]] + 1
	}

	for _, query := range inpQueries {
		fmt.Println(freqDict[query])
	}

}
