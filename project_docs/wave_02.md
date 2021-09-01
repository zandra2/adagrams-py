# Wave 2

Next, you need a way to check if an input word (a word a player submits) only uses characters that are contained within a collection (or hand) of drawn letters. Essentially, you need a way to check if the word is an anagram of some or all of the given letters in the hand.

To do so, implement the function called `uses_available_letters` in `game.py`. This function should have the following properties:

- Has two parameters:
   - `word`, the first parameter, describes some input word, and is a string
   - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter
- Returns either `true` or `false`
- Returns `true` if every letter in the `input` word is available (in the right quantities) in the `letters_in_hand`
- Returns `false` if not; if there is a letter in `input` that is not present in the `letters_in_hand` or has too much of compared to the `letters_in_hand`