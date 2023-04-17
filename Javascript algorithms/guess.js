let date = 16

let guess = prompt("Enter a date")

let counter = 0;

while (counter != -1){
    guess = prompt("Enter a date")

    if(guess == date){
        console.log("Correct guess")
    }
    console.log("Incorrect guess")

   counter++;
}