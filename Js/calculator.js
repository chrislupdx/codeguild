
let operation = {}
  let one, two, op, answer

while (operation != "done")
{
  one = prompt("first number")
  two = prompt("second number")
  operation = prompt("add/sub/mult/div?")

  if (operation == "add"){
    answer = one + two
  }

  if (operation == "sub"){
    answer = one - two
  }

  if (operation == "mult"){
    answer = one * two
  }

  if (operation == "div"){
    answer = one / two
  }

  if (answer != undefined){
    operation = "done"
  }
}
console.log(answer)
