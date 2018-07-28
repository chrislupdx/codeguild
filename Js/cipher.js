let english = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
let rot = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r','f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}
let querent = prompt("Input?").toLowerCase();

let reversed = {}
for (key in rot) {
    let value = rot[key]
    // console.log(reversed)
  }

// measure/translate/pull by indexical length?

let encoded = []
for (let i = 0; i < querent.length; i++) {
  // char = querent[i]
  // rotd = rot[char]
  // encoded.push(rotd)
  encoded.push(rot[querent[i]])
  // lines 15-17=18
}
  let joined = encoded.join('')
console.log(joined)


let decoded = {}
for (let i = 0; i< querent.length; i++) {
  console.log(querent[i]);
}
