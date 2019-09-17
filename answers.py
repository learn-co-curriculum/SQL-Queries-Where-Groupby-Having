Questions
1. Which student was born closest to the cohort's graduation date?
2. Which student(s) has the most siblings?
3. How many students are only children?
4. Which 3 students have lived in NYC the shortest amount of time?
5. How many students are native New Yorkers?
6. Do any two students have the same favorite food?

1. 
c.execute('''select name from students''').fetchall()

2. 
c.execute("""SELECT name, siblings
FROM students
WHERE siblings = (SELECT MAX(siblings) FROM students);""").fetchall()
[('Florencia Leoni', 4),
 ('Mohamad Eldebek', 4),
 ('Menachi Korn', 4),
 ('Miguel Peña', 4)]

3. 
c.execute("""SELECT COUNT(name)
FROM students
WHERE siblings = 0;""").fetchone()
(3,)

4. 
c.execute('''
SELECT name, years_in_nyc from students order by 2 limit 3
''').fetchall()

5. 
c.execute('''select  name, birth_place from Students where birth_place like '%NY' ''').fetchall()
[('David Miller', 'New York, NY'),
 ('Amy Li', 'New York, NY'),
 ('Akshay Sharma', 'New York, NY'),
 ('Adam Dick', 'New York, NY'),
 ('Alex Mitrani', 'New York, NY'),
 ('Nicole Roach', 'Brooklyn, NY')]

6. 
c.execute("""SELECT favorite_food, count(favorite_food)
FROM students
GROUP BY favorite_food
HAVING count(favorite_food) > 1
""").fetchall()
[('pizza', 2), ('steak', 2)]

