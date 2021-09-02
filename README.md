# AdaGrams

## Skills Assessed

- Following directions and reading comprehension
- Reading tests
- Using git to maintain code
- Manipulating and processing data in lists and strings
- Practicing pair-programming techniques

## Goal

An [anagram](https://en.wikipedia.org/wiki/Anagram) is a word or phrase formed by rearranging the letters of a different word or phrase. In this project you and your partner will be creating _Adagrams_, a game in which a player is given a random set of letters and must make an anagram using those letters.  Each submitted word will score points.

While working on _Adagrams_, it may help to think of a physical metaphor for this game, such as other common word games like _Scrabble_ or _Bananagrams_. These games all feature a _pool_ of letter _tiles_ that the player _draws_ from.

In this version of _Adagrams_, we will only be working with the English alphabet.

![an image of a pile of letter tiles](assets/letter-tiles.jpeg)


## Project Development

### Pair Programming

Utilize good pair programming practices. Refer to articles from the [Agile Alliance](http://guide.agilealliance.org/guide/pairing.html), the [Agile Institute](http://powersoftwo.agileinstitute.com/2015/02/benefits-of-pair-programming-revisited.html), and the lesson in Learn titled Intro to Pair Programming from Approaching a Problem if you need a refresher for some best practices. Switch _driver_ and _navigator_ roles often. When there is uncertainty or confusion, step away from the keyboard and discuss, plan, and document on paper or whiteboard before continuing.

### Workflow

1. When you want to begin work on this project, ensure that your virtual environment is activated:

```bash
$ source venv/bin/activate
```

2. Run the game and play test your current wave.  Replace the word `wave` below with the wave number (ie, 1, 2, 3 or 4):

```bash
# Must be in activated virtual environment
$ python main.py wave
```

3. Find the test file that contains the test you want to run.

   - Check the `tests` folder, and find the test file you want to run
   - In that test file, read through each test case

4. Run the tests for your specific wave

```bash
# Must be in activated virtual environment
$ pytest tests/test_wave_01.py
```

4. Use play-testing wth your partner to guide your development.

5. Use tests to verify your functions after thoroughly play-testing.

6. Use git to commit your work regularly!  Commit between each wave.

```bash
# Add your current work
$ git add .
$ git commit -m "meaningful message explaining your commit"
```

6. Move on to the next wave!

7. When you are finished working for the day, deactivate your environment with deactivate or closing the Terminal tab/window

```bash
$ deactivate
```

## Project Write-Up: How to Complete and Submit

Go through the waves one-by-one and build the features of this game.

At submission time, no matter where you are, submit the project via Learn.

Both teammates must submit in Learn.  In addition to submitting the repo and the pull request, fill out the section 'Reflect on Pair Programming'.

## Project Directions

1. [Setup](project-docs/setup.md)
1. [Test Info](project-docs/tests.md)
1. [Hints](project-docs/hints.md)
1. [Wave 1: draw_letters](project-docs/wave_01.md)
1. [Wave 2: uses_available_letters](project-docs/wave_02.md)
1. [Wave 3: score_word](project-docs/wave_03.md)
1. [Wave 4: get_highest_score](project-docs/wave_04.md)

