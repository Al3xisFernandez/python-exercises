function puzzle(N) {
  let A = 1;
  let B = 1;
  let C = 1;
  let D = 1;
  
  for (let i = 0; i < N; i++) {
    let X = D + 2 * C + 3 * B + 4 * A;
    A = B;
    B = C;
    C = D;
    D = X;
  }

  return D % 10000000000;
}

console.log(puzzle(10));
console.log(puzzle(100));
console.log(Math.pow(2022, 100));
