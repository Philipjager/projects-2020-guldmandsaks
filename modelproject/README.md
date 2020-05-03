# Model analysis project - Constrained Stock Allocation Optimization

Our project is titled "Constrained Stock Allocation Optimization". It revolves around exactly the means of the title implying that we are implementing a model using an initially concave utility function applied in two different stages, a budget constraint, initially two different stocks that yields different negatively correlated and predetermined returns in the two comparable stages for which a predetermined probability and a complementary probability is fixed. The optimizer iterates through possible allocations expressed as shares of each stock in relation to the complete budget, and at the end returns the allocation that provides the highest utility. 
After the initial optimization we create a loop through the different values of the probability of the first stage inferring that we run the optimization of values from the first stage being 100% likely to happen, until the second stage being 100% likely to happen - We then create and display different graphs of the investment shares in each of the stocks as functions of the stage likelihood. Afterwards we repeat this process but now looping through the yield of the first stock in the first stage (the high yield stage for the first stock), and display the optimizing allocations as function of the yield.
In the third main part of the project we ammend the utility functions to evaluate scenarios where the investor is either riskneutral or risk loving, that is if his/her utility function is linear or convex respectively. We then deduct on the results, and the correlation between our optimization and general theory of risk adversion and expected returns. 
In the final part of the project we add extensions to the Constraint Stock Allocation Optimization model. Our extensions to the model are two different approaches. In the first part we extend the model with a third stock that is characterized with having no risk, in the  general financial theory the CAPM (Capital Asset Pricing Model) this corresponds to the risk-free asset. We perform the optimization with the original utility function representing a risk-adverse investor. The second extension to the main model consists of introducing a third potential stage, so the spectre and probability of each stage is increased and decreased respectively.


The results and full script of our project can be viewed by running "Model Project.ipynb"

Apart from a standard Anaconda Python 3 installation, the project requires the following packages installed:
- Numpy
- Scipy (optimize)
- Matplotlib
