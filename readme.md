# Genetic Algorithms

## Missions & Activities:

<img src="img\Mastermind.jpg" alt="Mastermind" width="300"/>

*Source: [Wikipedia](https://en.wikipedia.org/wiki/Mastermind_(board_game))*

### Activity
Choose between the following two problems:
- **Problem 1**: Use a Genetic Algorithm (GA) to find a quasi-optimal solution for a simple problem (i.e., solve a mastermind game).
- **Problem 2**: Use a Genetic Algorithm (GA) to fine tune any classifier in scikit-learn.
  - Basically, our function will replace the grid search in the scikit-learn library.
  - The goal is to find the best hyperparameters for a classifier using GA.
  - You can use any classifier you want (e.g., SVM, Random Forest, etc.). We provide an example with Neural Networks.
- **Tools**: [DEAP](https://deap.readthedocs.io/en/stable/index.html) library *or* other libraries (e.g., [PyGAD](https://pygad.readthedocs.io/en/latest/))
- **Consolidation of ML Glossary**:
  - **Steps**: Initialization, selection, crossover, mutation, evaluation.
  - **Terminology**: Gene, individual (or chromosome), population, parents, children, elite, fitness scores.

- **Implementation of GA - Problem 1**:
  - Solve a mastermind game using GA:
    - Check the files: 
      - `sentence_mastermind.py` (a simple class providing the game logic: selecting hidden sentence, checking the guess, etc.)
      - `example_mastermind.py` (an example that shows how to call the methods in sentence_mastermind.py)
- **Implementation of GA - Problem 2**:
  - Use a GA to fine-tune a classifier in scikit-learn:
    - Check the file: `GA_search.py` (we only provide the part that implements the NN classifier, you need to implement the GA part)
  - NOTE: you can use a GA library or implement GA yourself from scratch. The first is faster, the second will require some extra work, but it will provide a better understanding of the implementation details of selection, crossover, mutation, etc. In any case, you can start from online examples.
    - If you use the Deap library, check this [example](https://deap.readthedocs.io/en/stable/examples/ga_onemax.html). Be sure of reading the "stable" version of the doc.
    - If you want to code all by yourself, check this [example](https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/).

 ### Implementing GA (provide these answers in the jupyter notebook)
- Explain the main GA steps also in your code: Initialization, selection, crossover, mutation, evaluation. (Sanity check) Is there any difference compared to what you saw in the slides?
- Discuss which hyperparameters you tested (e.g., varying number of generations, mutation rate, etc.) and their impact on the results.
- Discuss which other hyperparameters you did not test (if any), but would you test if you had more time. 
- What if you used Brute Force to solve the problem? How would you do it? What would be the complexity of the Brute Force approach? How does it scale compared to the GA?
  - Optional: compare the results of the GA with the Brute Force approach while increasing the size of the hidden sentence.

## Expected Outcomes:
  - A Jupyter notebook for the optimization of a simple problem.
  - In your notebook, systematically use markdown cells to:
    - Explain the goal of your code.
    - Comment on the results.
    - Provide **direct** answer to the questions in the [Implementing GA](#implementing-ga-provide-these-answers-in-the-jupyter-notebook) section.

## Installation
If you have [Poetry](https://github.com/hei-synd-aml/lab-0-TutoPoetry) on your machine, you can install the dependencies by running the following command in the root directory of the project (where the `pyproject.toml` file is located):
```bash
poetry install
```

If you don't have Poetry installed, you can install the dependencies using pip (as usual, we strongly suggest to create a virtual environment).

