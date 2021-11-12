# Optimization of multi-vehicle Transportaion

## Screenshots
**Input data file**  
![mkpInput](https://user-images.githubusercontent.com/58071878/141596470-f3d5ef1b-dc2b-48ed-b341-089dc26899ad.png)

**Output list**  
![mkpOutput](https://user-images.githubusercontent.com/58071878/141596524-dfaacea1-a6d6-4f1b-b508-7e2cdccb2be1.png)

**Visualization of the solution**  
![outputVisualization](https://user-images.githubusercontent.com/58071878/141596539-2e67c453-6706-4eed-a4cb-bbc0c1f6d306.png)


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
