# Analysis

## The very first randomized search space

Initially, 20 different chromosome sets are randomly generated, which also serve as the primary population. 

<img width="980" alt="basic" src="https://user-images.githubusercontent.com/25258877/44310720-8433bc00-a3f8-11e8-9f4b-8728f895ae1d.png">

## The first eligible chromosome set

Chromosomes with no. of set bits > 10 (attendance should be atleast 50%) are chosen and this forms the first fit population set.

<img width="981" alt="first" src="https://user-images.githubusercontent.com/25258877/44310721-885fd980-a3f8-11e8-85c4-92fddfa32769.png">

Now, 2 chromosome sets are randomly picked up from the eligible set. **Crossover** is performed & a new child chromosome is generated.

Next, to facilitate **mutation** , a random bit is flipped. Our child chromosome is now ready & thus, its fitness is calculated. 

In every generation, the best 50%, along with their parents are chosen (on the basis of the fitness function) & the processes of crossover & mutation are performed again.

The best chromosome of every generation is tracked

## Best chromosome in i'th population 

As we can observe, the value `li-hc`, which is also the `fitness` of a chromosome, improves over time. Multiple instances of the program can be run to verify the same.

Starting from 1.51 -> 2.66 , a significant improvement. 

<img width="980" alt="best" src="https://user-images.githubusercontent.com/25258877/44310722-8e55ba80-a3f8-11e8-927b-ec4c4f5ccde4.png">


## Complete history of each participating chromosome

The complete population set can be found [here](https://gist.github.com/shikhar-scs/c82a9ece2475241410af28357310095d) 

## Inference

Running the algo for a higher no of generations will give a better result, unless we hit a bottle-neck. The process can be stopped now.

## Graph of Complete Population

To get a graph of the complete population, run

```coffeescript

python randomGuy.py # generate a new population set

python plottingAGraph.py # run Graph Plotter

```
![graphplot](https://user-images.githubusercontent.com/25258877/44615597-82845100-a85b-11e8-9268-6fa60de3204a.png)
