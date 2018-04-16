// Core hello package

package main // required for standalone executable
import "fmt" // Impliments formatted I/O

// Global Constant Variable (string)
const m string = "wElL hElLo mY CrAzEe wErLd!"

func wait() {
	w := "...waiting"
	fmt.Println(w)
}

func greet() {
	// Non-Global Variable
	var g string = "  Hello! My name is: "
	// Map Player & Names
	myPlayers := make(map[string]string)

	// Add Key/Value Pairs to map "myPlayers"
	myPlayers["MainHost"] = "Kat"
	myPlayers["AltHost"] = "Erin"
	myPlayers["MainGuest"] = "Claire"
	myPlayers["AltGuest"] = "Stephanie"

	// Introduce MainHost
	fmt.Println(g, myPlayers["MainHost"])
}

// Greet World
func meet() {
	i := 1
	for i <= 3 {
		fmt.Println(i, m)
		if i == 3 {
			greet()
		} else if i < 3 {
			wait()
		}
		i++
	}
}

// Core Logic
func main() {
	meet()
}
