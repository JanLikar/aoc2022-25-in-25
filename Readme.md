# 2022 Advent of Code - 25 days in 25 languages

- [01 - Python](#1-python)
- [02 - Clojure](#2-clojure)
- [03 - Elixir](#3-elixir)
- [04 - C](#4-c)
- [05 - PHP](#5-php)
- [06 - Kotlin](#6-kotlin)
- [07 - Javascript](#7-javascript)
- [08 - Scala](#8-scala)
- [09 - Java](#9-java)
- [10 - Bash](#10-bash)
- [11 - Raku](#11-raku)
- [12 - C++](#12-c)
- [13 - Python](#13-python)
- [14 - D](#14-d)
- [15 - Perl](#15-perl)

In each of the languages I tried to follow the best practices to
the best of my knowledge and to succinctly solve the problem at
hand.

I am, however, familiar with only a handful of these languages, so
don't hold it against me if I butcher them colossally.

[AoC 2022](https://adventofcode.com/2022)

## 25 Days
### 1. Python
Python is an excellent fit for solving tasks like these and
I figured I should start with a language I'm actually familiar
with.

I used a generator to aggregate the lines and a couple of maps
and reducers to calculate the results. In most cases I would
prefer list comprehensions to using `map`, but in this case
it fits perfectly.

What can I say... Python is my primary language and I love it dearly,
so this was not a challenge at all.

[Day 1: Calorie Counting](https://adventofcode.com/2022/day/1)

[Solution](01/)

### 2. Clojure
As I don't have any real-world experience with lisps, I expected a decent Clojure solution would be harder for me to implement.

I was pleasantly surprised - Clojure proved extremely expressive and nice to work with.

Converting my first PoC, which looked fairly similar to
what an imperative solution would look like,
to a more idiomatic, functional solution was thoroughly rewarding.

[Day 2: Rock Paper Scissors](https://adventofcode.com/2022/day/2)

[Solution](02/)

### 3. Elixir
In a way this felt like Clojure with a different syntax.

String handling was slightly awkward, but I am sure that's because I didn't take enough time
to learn about Elixir's string types.

This task does not really allow Elixir's killer features to shine, but it was still a decent fit.

[Day 3: Rucksack Reorganization](https://adventofcode.com/2022/day/3)

[Solution](03/)

### 4. C
I haven't had the pleasure of using C in a long time. It felt a bit like cheating to use
it for such a simple task that would have been easy in any of the languages on my list (short of assembly).

Having said that, I would rather save the languages I am less familiar with for more interesting tasks.

[Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4)

[Solution](04/)

### 5. PHP
PHP was my first programming language and I used to adore it. 
Its low barrier to entry showed me what programming is and opened me doors into the wonderful world of computer engineering.

Solving this task, however, was no fun at all.

Array and string handling is awkward, syntax sugar you would
expect in a high-level programming language is simply missing,
semantics of some basic language constructs are unclear...

Unless I was trying to cobble together a quick-and-dirty web app
I would actually prefer to use C over PHP.


[Day 5: Supply Stacks](https://adventofcode.com/2022/day/5)

[Solution](05/)

### 6. Kotlin
Like with Elixir, this task does not fully demonstrate
Kotlin's killer features, but it was nonetheless a fun exercise.

Kotlin seems like a great language for someone who likes to
intertwine imperative, functional and object-oriented programming
styles.

It allowed me to implement the solution very concisely,
especially after replacing the function to check for unique
substrings with a very clever oneliner I borrowed from the
internet.

[Day 6: Tuning Trouble](https://adventofcode.com/2022/day/6)

[Solution](06/)

### 7. Javascript
This one was a wild one.

At first glance it seemed I could implement this in functional style,
using immutable values, but that proved rather complex so I opted for
a more imperative approach.

In my first attempt I used a hiearchy of JS objects with recursive
functions to calculate the required sums. That worked, but the
solution proved to be rather messy, so I rewrote it.

Final (and best) approach uses an object to store directory sizes with
paths being used as keys. When iterating over files all parent directories
are updated based on the PWD that is stored in a stack-like list.

[Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7)

[Solution](07/)

### 8. Scala
Interesting problem today. At first I implemented it naively using 4 for loops
and a 2d matrix to mark visible elements & prevent duplicates
but when I started working on the second part it became clear I didn't use the
correct data structure for the task.

I quickly [jumped into Python](08/extras/solution.py) to prototype the algorithm,
because Scala was not really cooperating with my debugging atempts.
The error messages were not always clear and I think the docs are lacking.

Nonetheless, I soon found a good solution. I iterate over the trees and slice the grid
into 4 1D arrays - one for each of the directions. Each of the slices is then reduced
using an appropriate method for either part of the puzzle.

Scala was my least favorite funtional language so far, but still not too bad.

[Day 8: Treetop Tree House](https://adventofcode.com/2022/day/8)

[Solution](08/)

### 9. Java
I haven't used Java since university, but this was a lot of fun and fairly mentally
stimulating!

I had an issue with the custom implementation of `hashCode` (needed for a HashSet)
where I accidentally compared `Integers` with `==`, which cause the algorithm to
return the wrong result. I should have used `.equals`.

The code is relatively verbose, but I guess that's just how it is with Java.

[Day 9: Rope Bridge](https://adventofcode.com/2022/day/9)

[Solution](09/)

### 10. Bash
Bash can be a pain, but this wasn't too bad.

[Day 10: Cathode-Ray Tube](https://adventofcode.com/2022/day/10)

[Solution](10/)

### 11. Raku
I have no experience with Perl or Raku, so this took me a very long
time to implement.

Raku seems like a very powerful language with lots of obscure features
which can be misused in many creative ways.

Although I probably won't be using Raku for any serious purpose anytime soon,
I must say having a built in way of specyfing the grammar and using it to parse
the input was very cool.

[Day 11: Monkey in the Middle](https://adventofcode.com/2022/day/11)

[Solution](11/)


### 12. C++
Graph search problem forced me to try some built-in data structures from
STL, which was interesting. They're powerful, but perhaps have slightly
dated APIs.

The language itself is verbose and confusing at times, but it made me
appreciate the improvement C++ brought over rudimentary features of C.

I had a major problem, which was a huge pain to debug, because I forgot
how C/C++ handle unsigned ints in expressions with (-)
(hint: no automatic casting, underflows are possible).

[Day 12:  Hill Climbing Algorithm](https://adventofcode.com/2022/day/12)

[Solution](12/)


### 13. Python
Yes, Python again, because I didn't have enough time for using
something else. I will fix this ASAP.

[Day 13: Distress Signal](https://adventofcode.com/2022/day/13)

[Solution](13/)


### 14. D
I was positively surprised by D's expressiveness and ease of use.
Certainly a very nice programming language.

It isn't entirely clear to me in what cases it would be preferred over Rust or Go, but it's certainly a strong contender.

[Day 14: Regolith Reservoir](https://adventofcode.com/2022/day/14)

[Solution](14/)


### 15. Perl
I don't want to bash a language I don't actually know, but I can
say that using Perl felt like a chore. Personally, I found Raku
to be nicer and more intuitive.

I fully understand that Perl used to be very important for various
scripting tasks, but today it just feels dated.

[Day 15: Beacon Exclusion Zone](https://adventofcode.com/2022/day/15)

[Solution](15/)


### 16.


[Day 16: ](https://adventofcode.com/2022/day/16)

[Solution](16/)


## Contributing
If you feel you can improve any of the posted solutions, feel free to open a PR.


## Future Ideas
OCaml
Haskell
Rust
Go
Julia
C#
Ruby
Lua
Scheme
Matlab
Swift
R
F#
Nim
