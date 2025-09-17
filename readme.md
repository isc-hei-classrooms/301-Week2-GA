# Genetic Algorithms

## Missions & Activities:

<img src="img\Mastermind.jpg" alt="Mastermind" width="300"/>

*Source: [Wikipedia](https://en.wikipedia.org/wiki/Mastermind_(board_game))*

### Activity
- **Problem**: Use a Genetic Algorithm (GA) to find a quasi-optimal solution for a simple problem (i.e., solve a mastermind game).
- **Tools**: [DEAP](https://deap.readthedocs.io/en/stable/index.html) library *or* other libraries (e.g., [PyGAD](https://pygad.readthedocs.io/en/latest/))
- **New glossary**:
  - **Steps**: Initialization, selection, crossover, mutation, evaluation.
  - **Terminology**: Gene, individual (or chromosome), population, parents, children, elite, fitness scores.

- **Implementation of GA - Problem 1**:
  - Solve a mastermind game using GA:
    - Check the files: 
      - `sentence_mastermind.py` (a simple class providing the game logic: selecting hidden sentence, checking the guess, etc.)
      - `example_mastermind.py` (an example that shows how to call the methods in sentence_mastermind.py)
  - NOTE: you can use one of the GA libraries mentioned above or implement GA yourself from scratch. The first is faster, the second will require some extra work, but it will provide a better understanding of the implementation details of selection, crossover, mutation, etc. In both cases, you can start from online examples.
    - If you use the Deap library, check this [example](https://deap.readthedocs.io/en/stable/examples/ga_onemax.html). Be sure of reading the "stable" version of the doc.
    - If you want to code all by yourself, check this [example](https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/).

 ### Implementing GA (provide these answers in the jupyter notebook)
- Explain the main GA steps also in your code: Initialization, selection, crossover, mutation, evaluation.
- Discuss which "hyperparameters" you tested (e.g., varying number of generations, mutation rate, etc.) and their impact on the results.
- Discuss which other hyperparameters you did not test (if any), but would you test if you had more time. 
- [Optional task] Solve the same problem using Brute Force: test all possible solutions! Consider this:
    - What is the complexity of the Brute Force approach?
    - How does it scale compared to the GA? (E.g., compare the results of the GA with the Brute Force approach while increasing the size of the hidden sentence.)

## Expected Outcomes:
  - A Jupyter notebook for the optimization of a simple problem.
  - In your notebook, systematically use markdown cells to:
    - Explain the goal of your code.
    - Comment on the results.
    - Provide **direct** answer to the questions in the [Implementing GA](#implementing-ga-provide-these-answers-in-the-jupyter-notebook) section.

## Installation
### uv
- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) on your machine. If you want to keep things simplem this is enough: 

```bash
pipx install uv
```

- Install the dependencies by running the following command in the root directory of the project (where the `pyproject.toml` file is located):
```bash
poetry install
```

If you don't have Poetry installed, you can install the dependencies using pip (as usual, we strongly suggest to create a virtual environment).

