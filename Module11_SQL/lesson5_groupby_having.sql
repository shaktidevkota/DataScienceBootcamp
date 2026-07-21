USE StudentDB;

SELECT Course, COUNT(*)
FROM Students
GROUP BY Course;

SELECT Course, AVG(Age)
FROM Students
GROUP BY Course;

SELECT Course, MAX(Age)
FROM Students
GROUP BY Course;

SELECT Course, MIN(Age)
FROM Students
GROUP BY Course;

SELECT Course, SUM(Age)
FROM Students
GROUP BY Course;

SELECT Course, COUNT(*)
FROM Students
GROUP BY Course
HAVING COUNT(*) > 1;

SELECT Course, AVG(Age)
FROM Students
GROUP BY Course
HAVING AVG(Age) > 20;