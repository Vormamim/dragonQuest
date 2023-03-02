### this applies to the following file
## roomAndPlayerVersions.py
## game_date_v2.jpon

In this example, a new field "treasure" has been added to each location object. This field contains the name of a treasure that can be found in that location. This information can be used in the Python program to add a treasure-hunting aspect to the game.

Compare the two JSON files to see the difference.

### F Strings

The f in f"You have {gold_coins} gold coins." stands for "format", and it's a feature of Python's string formatting. An f-string is a string literal that's prefixed with the letter f. Within the string, you can include expressions inside curly braces {} that are replaced with the values of the expressions when the string is evaluated.

In this case, f"You have {gold_coins} gold coins." is a string that includes an expression {gold_coins} inside curly braces. When the string is evaluated, the value of the gold_coins variable is inserted into the string, resulting in the message "You have X gold coins.", where X is the value of the gold_coins variable.

F-strings provide a concise and readable way to include expressions inside string literals. They were introduced in Python 3.6 and are a more modern alternative to the older string formatting techniques like the % operator or the str.format() method.