# Network Simulations

Using Python, I followed instructions to simulate a social network and simulate some covariates for each individual in the network. Lastly I was tasked with taking a sample and computing its confidence interval to ultimately check if the values of beta1 and beta2 matched those that I had provided earlier. The steps are shown below:

My first task was to simulate the social nework. Setting an x and a y using two values taken from a normal distribution with an arbitrary mean and standard deviation, I plotted various points in a two dimensional graph to represent individuals in a network. 

I then proceeded to create a list of lists to represent a matrix which consisted of euclidean distances between any two points contained in the graph. When printed to console, looks like this:
```sh
[['0.0', '0.465990674635', '0.357202949064', '0.0133321569109', '0.388099356896'], ['0.465990674635', '0.0', '0.660109732204', '0.478682555747', '0.839541846968'], ['0.357202949064', '0.660109732204', '0.0', '0.357965940372', '0.332919926034'], ['0.0133321569109', '0.478682555747', '0.357965940372', '0.0', '0.377884098192'], ['0.388099356896', '0.839541846968', '0.332919926034', '0.377884098192', '0.0']]
```
Visually, it is not appealing but this matrix allows for fast access when requesting a euclidean distance between any two points. 

Next, I simulated edges by taking draws from a bernoulli distribution with probability: e^(euc_dist * a)/[1 + e^(euc_dist * a)]. The constant a is an arbitrary constant which controlls the overall expected tie frequency. Values of 1 contributed an edge between two given points and values of 0 signified no edge.

Plotting the edges in the graph resulted in a graph like the one below:

![Alternate text](http://4.bp.blogspot.com/-jv6D24r02HA/UYMMSIVbbGI/AAAAAAAABC8/51z5axqtJT8/s1600/Interactions_2011.jpg)

My next task was to simulate covariates like age and gender for each individual in the graph. Using a module in Python called Numpy, I took a draw from a random uniform distribution which varied anywhere from age 1 to age 90. For the gender of the individual, I again took a draw from a binomial distribution with probability p = 0.5.

```sh
age = int(np.random.uniform(1, 91))
gender = np.random.binomial(1, 0.5, 1)
```
With the age and gender, I generated an outcome by taking a draw from a standard normal with a mean equal to beta0 * beta1 * gender + beta2 * age. Combining all the information, I represented each individual with the tuple data struture in Python. An example is shown below in the form: (x cordinate, y cordinate, age, gender(0 or 1), outcome)

```sh
(0.04060265052702533, -0.3298469515571403, 12, 0, 11.29663869720959)
```





 



