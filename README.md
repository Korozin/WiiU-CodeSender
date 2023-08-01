# WiiU-CodeSender

This repo is for the purpose of attempting to create more stable and refined CAFE and RAM WRITE code sending processes. By breaking down the tasks into smaller segments (like code sending in this example) I can focus on making sure each individual feature works before implementing it into the whole.

### How RAM Writes have changed.
Instead of defining my own socket functions like in the past, I've instead decided to read each line of the RAM Write input, and split each line into two parts- The `Address` and the `Value`. I then convert these values into their Decimal counterparts by using the `int(<var>, 16)` function, and pass it to uGecko's `kernerlWrite()` function. As uGecko is a library _meant_ for this- it should be more stable as it includes memory range and address verification.

### How CAFE sending has changed.
The CAFE process now adopts the practice of restore points. When the `CodeSender_Main()` Class is initialized it sets the `restore` value to `0`. But when undergoing the process of sending a code it uses a `for x in range()` statement to log the number of iterations the code uses to pass bytes to the server. When sending again it uses a new `for x in range()` statement using the `restore` value as the main variable to retrace the memory blocks and restore memory. This should create a more stable code sending process.
