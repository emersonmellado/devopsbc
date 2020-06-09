# Propositional Logic

## Conjunction & Disjunction & Negation

Statement: "John goes to the mall and Maria goes to the movies"
Let p = "John goes to the mall"
Let q = "Maria goes to the movies"

Conjunction: p ^ q
Disjunction: p v q
Negation: ~p v ~q
---
Statement: "Today is raining and the grass is wet"

Let p = "The grass is wet"
Let q = "Today is raining"

Conjunction: q ^ p: "Today is raining and the grass is wet"
Disjunction: q v p: "Today is raininig or the grass is wet"
Negation: ~q v ~p: "Is not raining today or the gras is not wet"
---
Statement: "I won't buy toilet paper and carry it with me"

Let a = "I will buy toilet paper"
Let b = "Carry it with me"
C: ~a ^ b
D: ~a v b
N: a v ~b
---
Statement: "Neither Jane or I drink"
let x = "Jane drink"
let y = "I drink"
C: ~x v ~y: "Jane does not drink or I do not drink"
D: ~x ^ ~y: "Jane does not drink and I will not drink"
N: x ^ y:   "Jane will drink and I will drink"
---
"The Cannucks did not win or the game is going longer"
let x = "The Cannucks won"
let y = "the game is long"
C: ~x v y: "They did not win or the game is long"
D: ~x ^ y: "They did not win AND the game is long"
N: x ^ ~y: "They win AND the game was not long"
---
## Implies
If I don't get paid, I won't go to work.
    - p -> q
    - p = "I don't get paid"
    - q = "I won't go to work"
    - ~p = "I will get paid"
    - ~q = "I will go to work"

- ~p -> q: "If I get paid then I won't go to work"
- p -> ~q: "If I don't get paid then I will go to work"


## Truth tables

The only possible two states are true or false

|p          |
|----       |
| true (1)  |
| false (0) |

- "Today is raining"

|p  | ~p |
|---|----|
| 1 | 0  |
| 0 | 1  |

- "Today is raining"

|q  | ~q |
|---|----|
| 0 | 1  |
| 1 | 0  |

- "Today is raining and the grass is wet"

let p = "Today is raining"

let q = "the grass is wet"

Molecule: p ^ q

| p   | q   | p ^ q |
|-----|-----|-------|
| 0   | 0   | 0     |
| 0   | 1   | 0     |
| 1   | 0   | 0     |
| 1   | 1   | 1     |

- "Today is raining or the grass is wet"

Molecule: p v q

| p   | q   | p v q |
|-----|-----|-------|
| 0   | 0   | 0     |
| 0   | 1   | 1     |
| 1   | 0   | 1     |
| 1   | 1   | 1     |

- "Today is raining and the grass is not wet"

let p = "Today is raininig"
let q = "the grass is wet"

- p ^ ~q

| p   | q   | ~q  | p ^ ~q |
|-----|-----|-----|--------|
| 0   | 0   | 1   | 0      |
| 0   | 1   | 0   | 0      |
| 1   | 0   | 1   | 1      |
| 1   | 1   | 0   | 0      |

### With more variables

"Today is raining and the grass is wet and I went outside"

let r = "Today is raining"
let w = "the grass is wet"
let o = "Went outside"

- r ^ w ^ o

| r   | w    | o    | r ^ w ^ o |
| ----|------|------|-----------|
| 0   | 0    | 0    | 0         |
| 0   | 0    | 1    | 0         |
| 0   | 1    | 0    | 0         |
| 0   | 1    | 1    | 0         |
| 1   | 0    | 0    | 0         |
| 1   | 0    | 1    | 0         |
| 1   | 1    | 0    | 0         |
| 1   | 1    | 1    | 1         |

- r ^ w ^ ~o

| r   | w    | o    |  ~o  | r ^ w ^ ~o |
| ----|------|------|------|------------|
| 0   | 0    | 0    | 1    | 0          |
| 0   | 0    | 1    | 0    | 0          |
| 0   | 1    | 0    | 1    | 0          |
| 0   | 1    | 1    | 0    | 0          |
| 1   | 0    | 0    | 1    | 0          |
| 1   | 0    | 1    | 0    | 0          |
| 1   | 1    | 0    | 1    | 1          |
| 1   | 1    | 1    | 0    | 0          |

### Example from a computer perspective

```
if (a or b and x>y or x>a){
    //True
} else {
    //False
}

if (a or ~b and x>y or x>a){
    //True
} else {
    //False
}
```

### Practical (ish) example - Good for debugging

- v = Virtual Box or HyperV or Parallels (Any virtualization software)
- u = Ubuntu Linux
- p = Python 3
- d = Docker
- j = Jenkins
- a = Ansible
- g = Git VCS
- c = Setup our cloud console on AWS.

```
- SetupChecker
if (v and c) {
    if (u){
        if (d and p and j and a and g){
            //Scenario: Ready - True
        } else {
            //Scenario: 1 - False
        }
    } else {
        //Scenario: 2 - False
    }
} else {
    //Scenario: 3 - False
}
```

- Ready: v ^ c -> u -> d ^ p ^ j ^ a ^ g
- S1: v ^ c -> u -> ~d v ~p v ~j v ~a v ~g 
- S2: v ^ c -> ~u
- S3: ~v or ~c

---

"System error: Not enough memory"

Heuristhics