# Optimization of multi-vehicle Transportaion

This project purpose is to provide a fully detailed plan of delievring goods.
In the first step the program will solve the Multi Knapsack problem
  it will provide a list of packages to be loaded on each vehicle, that will maximize the company income.
After that, the program will solve the Traveling Sales Person problem-
  it will provide the shortest route available for every vehicle.

To solve the problems, the program will use IBM ILOG CPLEX Optimizer solver.
The problems have been translated into Integer Linear Programming models, written in OPL language.

All the data, input and output processing is done by Python scripts.
The packages are given in a Json file, and the input file for the solver are created automatically.

On top of that the final solution with the routes is visually presented to the user.


## Screenshots
**Input data file**  
<img width="563" alt="mkpInput" src="https://user-images.githubusercontent.com/58071878/141596648-f72a4b62-233c-4ae1-8679-827453e0b07b.png">

**Output list**  
<img width="365" alt="mkpOutput" src="https://user-images.githubusercontent.com/58071878/141596651-fdc63c96-71c6-49ae-b0ae-9f6cf6cad891.png">

**Visualization of the solution**  
<img width="400" alt="visualization" src="https://user-images.githubusercontent.com/58071878/141596665-e867dd2f-7bde-40f1-9af4-3c9d7c827891.png">
