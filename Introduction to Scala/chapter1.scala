// ex 1 "Scala is object-oriented"

// Calculate the difference between 8 and 5
val difference = 8 - 5

// Print the difference
println(difference)



// ex 2 "Define immutable variables (val)"
// Define immutable variables for clubs 2♣ through 4♣
val twoClubs: Int = 2
val threeClubs: Int = 3
val fourClubs: Int = 4



// ex 3 ""
// Define immutable variables for player names
val playerA: String = "Alex"
val playerB: String = "Chen"
val playerC: String = "Umberto"


// ex 4 "Define mutable variables (var)"
// Define mutable variables for all aces
var aceClubs = 1
var aceDiamonds = 1
var aceHearts = 1
var aceSpades = 1


// ex 5 ""
// Create a mutable variable for Alex as player A
var playerA = "Alex"

// Change the point value of A♦ from 1 to 11
aceDiamonds = 11

// Calculate hand value for J♣ and A♦
println(jackClubs + aceDiamonds)