**Course**: Data Science   <br/>
**Mod**:    2                 <br/>
**Topic**:   SQL Queries - Where, Groupby, Having <br/>
**Amount of time**: 45 minutes <br/>
**Author**: Vishal Patel vishal.patel@flatironschool.com

## Teacher Notes

## Summary

This is a set of useful practice exercises for students to test their SQL knowledge of filtering datasets. Problems also require students to use group by statements and having clauses. The second problem requires a subquery. This could be a good preview activity even if students have yet to be formally introduced to subqueries, the concept is fairly natural. The final exercise is a real stretch, involving datetime functions which students are apt to have no previous exposure to. Encourage students to actively problem solve as they would on the job by using search engines and other online resources.

## Learning Goals
* Perform simple select statements with SQL
* Use where clauses appropriately with SQL
* Understand the difference between where and having clauses
* Perform group by aggregations with sql

## Prerequisite Knowledge

Students should already have a done a fair amount of practice with SQL before trying these exercises, some of which are moderately complex.

## Agenda

* Student Work Time on Problems
* Class Discussion of Exercises


1. What are the names of all of the students.

> This is a straightforward review question meant to build some repetition and easy practice.

2. Which student has the most siblings?

> This is great place to use a subquery. Encourage students who are initially struggling with a question along the lines of "How could you select the largest number of siblings that anyone has in the group?" From there, you can further push students with a hint if needed: "How can you now make a selection using the result of this, [embedded as a subquery]?"

3. How many students are only children?

> This is considerably easier then question 2. Students can simply place a selection filtered by a where clause. A simple aggregate is also required.

4. Which 3 students have lived in NYC the shortest amount of time? [How long has each lived in NYC?]
    
    > Also considerably easier then the previous two questions. This problem requires a simple order by and limit clauses.

5. How many students are native New Yorkers?

> This place can be tricky depending on how the problem is formulated. For one, are we talking New York City or New York State? If we mean the former, NYC, then the answer below actually would include other non-relevant results. 

It can also be worth noting the difference between like and ilike in this context; ilike being case sensitive while like will ignore all caps. If you wish to further progress this conversation, you can also ask students how they might compare the functionality of like and ilike using python string methods.

6. Do any two students have the same favorite food?

This problem employs the `Having` clause.  Be sure to review the difference between the where and having clause here. (Where filters apply before the group by clause and conditions following the having clause are filters applied after the group by on the resulting aggregate [statistics].) A useful example in doing so, could be to modify the question to something with an additional filtering criterion such as 'do any native new yorkers have the same favorite food?' This would force students to use a where clause prior to the group by to filter the results. Alternatively, see the question below for an alternative but related problem on favorite foods.

> Extension:

Have students write their own problems (up to 3), and share them with a partner. These can also then be shared out with the larger class. Please add any exemplars to this document and push those additions to github. 