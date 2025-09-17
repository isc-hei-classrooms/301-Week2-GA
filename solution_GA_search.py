# Genetic Algorithm - Hyperparameter Tuning using DEAP
# The idea is to replace GridSearchCV with a Genetic Algorithm (GA) to find the best hyperparameters for a given
# classifier. The DEAP library is used to implement the GA.

from deap import base, creator, tools
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
import numpy as np

# -----------------------------
# Evaluation Function
# -----------------------------
def evalModel(individual, clf, X, y, scoring='f1', cv=5):
    # Individual is a list of (param_name, value)
    hyperparams = {name: value for name, value in individual}

    # Set hyperparameters into the classifier
    for param_name, value in hyperparams.items():
        setattr(clf, param_name, value)

    # Perform cross-validation
    scores = cross_val_score(clf, X, y, scoring=scoring, cv=cv)

    # Return mean score as a tuple (DEAP requires tuples for fitness)
    return (scores.mean(),)


# -----------------------------
# Individual Generator
# -----------------------------
def create_individual(param_grid):
    """Randomly sample one value per hyperparameter from the grid."""
    individual = [
        (param_name, random.choice(param_values))
        for param_name, param_values in param_grid.items()
    ]
    return individual


# -----------------------------
# Main GA Function
# -----------------------------
def GA_search(clf, param_grid, X_train, y_train, scoring='f1', ngen=10, pop_size=50):
    print("🔍 Starting Genetic Algorithm hyperparameter search...\n")

    # -----------------------------
    # DEAP Setup
    # -----------------------------

    # Fitness function (we want to maximize score)
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    # Individuals are lists of (param_name, value)
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_hyper_param", create_individual, param_grid)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr_hyper_param)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Register DEAP operators
    toolbox.register("evaluate", evalModel, clf=clf, X=X_train, y=y_train, scoring=scoring)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # -----------------------------
    # Run Evolution
    # -----------------------------
    run_evolution(toolbox, ngen=ngen, pop_size=pop_size)


# -----------------------------
# GA Execution Loop
# -----------------------------
def run_evolution(toolbox, ngen=10, pop_size=50):
    random.seed(42)
    pop = toolbox.population(n=pop_size)

    print(f"Initial population of {pop_size} individuals")

    # Evaluate initial population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    CXPB, MUTPB = 0.5, 0.2
    avg_fitness_per_gen = []

    for g in range(1, ngen + 1):
        print(f"\n Generation {g}/{ngen}")

        # Select, clone, crossover, and mutate
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values # del instruction invalidate the fitness of the modified offspring
                del child2.fitness.values 

        # Apply mutation
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Re-evaluate only invalid individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Replace population
        pop[:] = offspring

        # Gather and report stats
        fits = [ind.fitness.values[0] for ind in pop]
        mean = np.mean(fits)
        std = np.std(fits)

        print(f"  Min:  {min(fits):.4f}")
        print(f"  Max:  {max(fits):.4f}")
        print(f"  Avg:  {mean:.4f}")
        print(f"  Std:  {std:.4f}")
        avg_fitness_per_gen.append(mean)

    # -----------------------------
    # Final Results
    # -----------------------------
    print("\n Evolution complete.")
    best_ind = tools.selBest(pop, 1)[0]
    best_hyperparams = {name: value for name, value in best_ind}

    print("\n Best Hyperparameters Found:")
    for k, v in best_hyperparams.items():
        print(f"   - {k}: {v}")
    print(f"\n Best Fitness Score: {best_ind.fitness.values[0]:.4f} after {ngen} generations")

    # Plot fitness curve
    plt.plot(avg_fitness_per_gen, marker='o')
    plt.xlabel("Generation")
    plt.ylabel("Average Fitness")
    plt.title("Genetic Algorithm Fitness Progress")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -----------------------------
# Usage Example
# -----------------------------
if __name__ == "__main__":
    # Here, we show an example of how to use the GA_search function with a neural network classifier in scikit-learn.
    # You can use any classifier from scikit-learn.
    # As dataset, we will use the Iris dataset.

    # Import necessary libraries
    from sklearn.neural_network import MLPClassifier

    # Load example dataset
    X, y = load_iris(return_X_y=True)

    # Define a NN classifier
    clf_nn = MLPClassifier(random_state=42, max_iter=1000)
    # Define parameter search space for NN
    param_grid_nn = {
        "hidden_layer_sizes": [(50,), (100,), (50, 50)],
        "activation": ["relu", "tanh", "logistic"],
        "solver": ["adam", "sgd"],
        "alpha": [0.0001, 0.001, 0.01],
        "learning_rate": ["constant", "adaptive"]
    }
    # Run GA search for NN
    GA_search(
        clf_nn,
        param_grid_nn,
        X_train=X,
        y_train=y,
        scoring="f1_macro", # Scoring metric: _macro is used for multi-class classification
        ngen=10,  # Number of generations
        pop_size=30  # Population size
    )

