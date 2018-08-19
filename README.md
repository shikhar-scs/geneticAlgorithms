# geneticAlgorithms

## Problem Statement 
 
There are 20 classes in a semester. Being a college student, I want to maximise my learning index but also not comprise much with my health. Moreover, the no. of classes I attend should be manageable enough to cross the cutoff bar. Above that it doesnt matter. Implement this as a GA problem.

## Running the file

```
python randomGuy.py
```

## Sample/Demo
 
Visit [analysis.md](https://github.com/shikhar-scs/geneticAlgorithms/blob/master/analysis.md) to see an analysis of the data.

## Note 

Below are several factors on which the number of classes I attend depends. The data present in [ActualData.csv](https://github.com/shikhar-scs/geneticAlgorithms/blob/master/ActualData.csv) is not random, rather, is based upon several factors I've listed underneath. The calculations have been made accordingly.

### Supposing I have 4 classes in a week & 5 weeks in a semester & time table is week-based.

- Attendance > 50% 																				
- Midterms : class no. 8 & 9
- Personal Projects : I make one project when the session begins & end it before midsems. I make two more between midsems & endsems.																			
- Weather Conditions : extreme summers, monsoons & humidity, 1 mark for each factor. 						
- Work of higher priority : Includes society work (preferably at the start of the semester), study leave for mid terms, Fest related work, Project Completions and study leaves for end sems.
- Class Assignments : 3 in the semester, evenly distributed.	
- No. of consecutive classes :	Class on the first day is the 4th consecutive class on that day & class on the third day is the 3rd consecutive class on that day.
- Class Timings (Too early/late) : Class on the second day is held at 8am , Class on the third day is held at 5pm.															
- Important Topic In Class : According to the syllabus, the important topics would be covered in the 3rd, 7th, 8th, 13th, 15th, 19th & 20th class.
- Classrooms Allocated, AC etc : Classes on the second & third day take place in air conditioned classrooms.
- Gaps in Classes :	5 hr gap on the second day and 3 hr gap on the 4th day.																			


## Fitness Function :

Initially, several factors which could affect me when attending a class were listed down. Then, based, on the above listed factors, a score out between 0 & 1 was given to each `classNo-factor` cell. Now, each of these factors could affect the notions `Depth & Breadth Of Learning` & `Cost To Health` differently & they also have a certain `weight` or `contibution factor` when taken into final consideration. 

Thus, a `weighted mean` is calculated for each day. Next, for a given day, I could be willing to learn more OR could rather ensure a lesser cost to my health, depending on the number of the particular class or rather any other event taking place at that time. Thus, a weight factor for each day is included too. 

So the final contribution of each day is calculated as `(the weighted mean of each of the factors) * (weight factor of the specific day)`. A sum of all the **included** days finally gives the respective `learning_index` & `cost_to_health`. 

The motive now is to maximise the learning index & minimise the cost to health.

Thus, the final fitness is calculated as `learning_index - cost_to_health`. 
A general formula for a given chromosome has been given below.

![untitled diagram](https://user-images.githubusercontent.com/25258877/44309932-d02c3400-a3eb-11e8-9a2a-8033859bed49.png)
<br>
<br>
<br>
f   : fitness calculated. <br>
cr  : chromosome array, cr[i] defines the i'th allelle of the chromosome <br>
Other terms are self explanatory.<br>
Please refer [ActualData.csv](https://github.com/shikhar-scs/geneticAlgorithms/blob/master/ActualData.csv) for the actual data. 
