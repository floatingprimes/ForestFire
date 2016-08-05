# ForestFire-Model

Primary Goal: Design a stochastic dynamic model describing a forest fire during a storm.

- Forest will be depicted via n x n grid of cells

- Time scope of the model will be determined by the user

- Each cell will have one of three states:
        - Tree on Fire: A flaming tree occupies the space in question
        - Tree: An unaffected tree occupies the space
        - Empty: The space is empty

- Model will implement elements of probability contingent on user set initial values.

- The stochastic aspect of the model will be achieved through a variety of factors to include:
        - Tree resistance to fire
        - Chance of fire spreading to neighboring trees

- The user will also predetermine the initial number of trees in the forest

- Rules the model will adhere to:
        - Fire can only spread from one enflamed tree to another, non-enflamed tree contingent on
        an RNG
        - Fire can only spread to its von Neumann neighbors (up, down, left, right)
        - After one step of discrete time (one full forest iteration), the enflamed tree will both try to spread  to its von Neumann neighbors and then be reduced to Empty space on the grid
        - Each tree, being of the same forest, will have the same resistance value between 0 and 1.
        - Empty space cannot become enflamed by nearby flaming trees.


Features to Implement:

- Add a stochastic element of lightning, which will randomly strike cells on the grid with low probability
  of the struck cells have a probability of catching fire if the cell contains an un-enflamed tree.
