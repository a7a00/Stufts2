# Introduction

All right, fun time! Missed the part where Sheldon talked about how this is basically Silicon Valley the class.

Anyhow, schedule!
* First month, Python, basic threading
* Second month, Erlang, a functional language based around concurrency

So, what does concurrency mean? Basically, multiple programs running at once, or, in older systems, give the appearance of running at once.

So, while most programs run like this:

```
A -> B -> C
```

A concurrent program may look like this:

```
   -> B -> D 
 /           \
A             -> F -> G
 \           /
   -> C -> E
```

Note, parallelism and concurrency are not the same thing, though they're often conflated. Concurrency is a logical paradigm by which event ordering is not fully determined. Parallelism is a way of implementing concurrency by having shit run on different hardware. Even single-core machines used to use parallelism, letting the CPU do non-disk activities while things were written to disk.

The world as we know it is concurrent, and modern computing depends on it.

## Why is concurrency hard?

Mostly due to roommates. I'll explain.

When you and your roommate both go to the fridge and see there's no milk and both get milk, you now have too much milk. How do we solve this?

* We can have a unique thing in the world. (You see the refillable carton is missing)
* You can leave a note, but good luck doing it fast enough. What if the OS puts you to sleep and you wake up with 4 gallons of milk dumped there by a COMP11 student's shit code?

The answer is that there's no software solution. You need a hardware guarantee.

Sheldon just told a very long story about the necessity of these. Say we have some code for bank withdrawl:

```python
if (check.amount < account.balance)
	pay(check.payee, check.amount)
	account.balance -= check.amount
else
	send_hatemail(account.owner)
```

Now, imagine 2 people withdraw from the same account at once! They could both pay and the account could go into the negatives without the hatemail aver being sent!

## Atomic actions

Atomic actions execute in one chunk, indivisible by any other processes. It either happens completley or not at all. You need to have these in order for any concurrent program to work properly. Very few things in C are atomic; even the increment operator is made of easily interruptible assembly instructions

## Race Conditions

These happen when two routines share a resource, and the result of the program depends entirely on which code gets to a resource first. This is what makes your Node programs fall into callback hell.

***YOU'RE PRESENTING PUZZLE 3.3 IN CLASS MONDAY, DON'T FUCK THIS UP.***
