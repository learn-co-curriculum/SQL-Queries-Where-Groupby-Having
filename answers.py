Questions
Which student was born closest to the cohort's graduation date?
Which student has the most siblings?
How many students are only children?
Which 3 students have lived in NYC the shortest amount of time?
How many students are native New Yorkers?
Do any two students have the same favorite food?

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


7. 
c.execute('''
SELECT name,
abs(julianday('2018-' || substr(birthdate,1,2) || '-' || substr(birthdate,4,2)) - julianday('2018-06-19'))
FROM students
ORDER BY 2
LIMIT 1
''').fetchall() 
