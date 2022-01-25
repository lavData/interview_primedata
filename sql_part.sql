-- I use SQL Lite to solve questions. 

-- Q.1 
-- I create a set value of Score without duplicate and get the number at offset 1 
-- -> Second highest Score of athletes 
SELECT DISTINCT Score FROM Performance 
ORDER BY Score LIMIT 1 OFFSET 1;


-- Q.2
SELECT id FROM Customers 
WHERE id NOT IN (SELECT customerid FROM Orders)


-- Q.3
-- First, I will join two tables with CONDITION is DepartmentId =  Id (Department)
-- Second, the salary must be in high earns.
-- Third, I will group by table with order is department name, employee
SELECT D.name, E.name, E.salary
FROM Employee AS E JOIN Department AS D ON E.departmentId = D.id
WHERE E.salary IN (SELECT DISTINCT salary 
                   FROM Employee
                   WHERE departmentId = E.departmentId
                   ORDER BY salary DESC LIMIT 3)
GROUP BY D.name, E.name, E.salary