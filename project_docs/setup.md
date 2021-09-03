# Setup

## Setup For Collaboration

1. You'll be working with an assigned pair. [Virtual] high-five your pair.
1. Choose **one person** to fork the project repo.
1. Add the other person in the pair (who didn't fork) to the forked repo as a _collaborator_. Instructions [here](https://help.github.com/articles/inviting-collaborators-to-a-personal-repository/).
1. **Both teammates** clone the forked repo: `$ git clone [YOUR FORKED REPO URL]`

Both members of the team will be working from the same forked repository.  Be sure to follow proper git protocol from the Intro to Git topic in Learn.

### Setup a Pair Plan

First, come up with a "plan of action" for how you want to work as a pair. Discuss your learning style, how you prefer to receive feedback, and one team communication skill you want to improve with this experience.

We recommend spending at least a portion of the time pair programming and working collaboratively from the same machine.  Zoom and screen sharing or [VSCode Live Share](https://code.visualstudio.com/learn/collaboration/live-share) are good tools to consider.  Some teams will choose to pair program and work collaboratively from the same machine for the entire project.  Some teams will choose to divide a portion of the work and combine their code using git.  

### Get Familiar

Take time to read through the Wave 1 implementation requirements and the tests for wave 1. Write down your questions, and spend some time going through your understanding of the requirements and tests with your pair. Make sure you both can run `$ rake` and see the tests fail.

Come up with a "plan of action" for your implementation with your pair.

If, after you and your pair have taken some time to think through the problem and would like direction for how to dissect the problem, or if you need clarity on the terms/vocabulary we used in this project, you can check out [a small hint we've provided](../projecty_docs/hints.md).

## One-Time Project Setup

Follow these directions once, at the beginning of your project:   

1. Navigate to your projects folder named `projects`

```bash
$ cd ~/Developer/projects
```

2. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `swap-meet`, and then puts the project into this new folder.

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

3. Move your location into this project folder

```bash
$ cd swap-meet
```

4. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

5. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

6. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

Summary of one-time project setup:

- [ ] `cd` into your `projects` folder
- [ ] Clone the project onto your machine
- [ ] `cd` into the `swap-meet` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`
