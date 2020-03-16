# Inaugural project

The purpose of this project is to construct a function in Python that can solve problems of utility maximization using numerical optimization. We use the optimizer method from the scipy package called 'bounded', which is a an optimizer that allowes constraints.
Afterwards we use the matplotlib package to plot the optimized values of labor and consumption, as functions of the wage in the given interval. 
We now evaluate the tax-revenue from the given expression in the Inagural project description, under the assumption that the wage is represented by a uniform stocastic variable - we do this by setting a seed (we used '2020') and then looping through the 10.000 observations while using the optimizer from the previous problem. Subsequently we repeat the process with an alternative value of epsilon. 
At last we perform an optimization of the tax-revenue with respect to the three parameters tau0 and tau1 (the two tax-rates), and kappa (the cut-off for the top labor income bracket). 
