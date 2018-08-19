# Analysis

Initially, a random function generator generates 20 diff chromosomes. The ones with no. of set bits>10 are chosen and thus the first fit population is formed. 


## The very first randomized search space
<img width="980" alt="basic" src="https://user-images.githubusercontent.com/25258877/44310720-8433bc00-a3f8-11e8-9f4b-8728f895ae1d.png">

## The first eligible chromosome set
Eligibility is defined as no of set bits > 10 (attendance atleast 50%)

<img width="981" alt="first" src="https://user-images.githubusercontent.com/25258877/44310721-885fd980-a3f8-11e8-85c4-92fddfa32769.png">

Now these, are mixed & matched on a random basis & a track of their parents is kept. In every generation, the best 50% are chosen (on the basis of the fitness function). There parents are also chosen & now, a new generation set is generated.
A track of the best chromosome in every generation is kept, & also all participating chromosomes are stored in the population. 


## Best chromosome in i'th population 

As we can observe, the value `li-hc`, which is also the fitness of a chromosome, improves over time. Multiple instances of the program can be run to verify the same.
Starting from 1.51 -> 2.66 , a significant improvement. 

<img width="980" alt="best" src="https://user-images.githubusercontent.com/25258877/44310722-8e55ba80-a3f8-11e8-927b-ec4c4f5ccde4.png">


## Complete history of each participating chromosome

The complete population set can be found here https://gist.github.com/shikhar-scs/c82a9ece2475241410af28357310095d 

## Inference

Running the algo for a higher no of generations will give a better result, unless we hit a bottle-neck. The process can be stopped now.
