// ex 1 "if and printing"
// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + fourSpades

// Congratulate the player if they have reached 21
if (hand == 21) {
    println("Twenty-One!")
}


// ex 2 "if expressions result in a value"
// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Inform a player where their current hand stands
val informPlayer: String = {
  if (hand > 21)
    "Bust! :("
  else if (hand == 21)
    "Twenty-One! :)"
  else 
    "Hit or stay?"
}

// Print the message
print(informPlayer)


// ex 3 "if and else inside of a function"
// Find the number of points that will cause a bust
def pointsToBust(hand: Int): Int = {
  // If the hand is a bust, 0 points remain
  if (bust(hand))
    return 0
  // Otherwise, calculate the difference between 21 and the current hand
  else
    return 21 - hand
}

// Test pointsToBust with 10♠ and 5♣
val myHandPointsToBust = pointsToBust(tenSpades + fiveClubs)
println(myHandPointsToBust)




// ex 4 "A simple while loop"
// Define counter variable
var i = 0

// Define the number of loop iterations
val numRepetitions = 3

// Loop to print a message for winner of the round
while (i < numRepetitions) {
  if (i < 2)
    println("winner")
  else
    println("chicken dinner")
  // Increment the counter variable
  i = i + 1

}


// ex 5 "Loop over a collection with while"
// Define counter variable
var i = 0

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands
while (i < hands.length)  {
  // Find and print number of points to bust
  println(pointsToBust(hands(i)))
  // Increment the counter variable
  i = i + 1
}



// ex 6 "Converting while to foreach"
// Find the number of points that will cause a bust
def pointsToBust(hand: Int) = {
  // If the hand is a bust, 0 points remain
  if (bust(hand))
    println(0)
  // Otherwise, calculate the difference between 21 and the current hand
  else
    println(21 - hand)
}

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands, finding each hand's number of points to bust
hands.foreach(pointsToBust)
