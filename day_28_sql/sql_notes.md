# SQL --- Interview Notes & Cheat Sheet

> **Goal:** Understand SQL well enough to solve interview problems,
> explain your reasoning, and avoid common mistakes.

------------------------------------------------------------------------

# 1. SQL Mental Model

Think of a query as a pipeline:

``` text
FROM / JOIN
      ↓
WHERE
      ↓
GROUP BY
      ↓
HAVING
      ↓
SELECT
      ↓
ORDER BY
      ↓
LIMIT
```

This is the **logical order** to remember when reasoning about queries.

### Key idea

-   `WHERE` → filters individual rows
-   `GROUP BY` → creates groups
-   `HAVING` → filters groups
-   `SELECT` → chooses/calculates output
-   `ORDER BY` → sorts the result
-   `LIMIT` → restricts the final number of rows

------------------------------------------------------------------------

# 2. SELECT

``` sql
SELECT customer_name, balance
FROM accounts;
```

Select everything:

``` sql
SELECT *
FROM accounts;
```

Use specific columns in interviews when possible because it makes the
query clearer.

------------------------------------------------------------------------

# 3. WHERE

Filters rows.

``` sql
SELECT *
FROM accounts
WHERE balance > 1000;
```

Operators:

``` text
=       equal
<>      not equal
>       greater than
<       less than
>=      greater than or equal
<=      less than or equal
```

Combine conditions:

``` sql
WHERE balance > 1000
  AND customer_id = 1;
```

``` sql
WHERE customer_id = 1
   OR customer_id = 2;
```

Use parentheses when mixing `AND` and `OR`.

------------------------------------------------------------------------

# 4. ORDER BY

``` sql
SELECT *
FROM accounts
ORDER BY balance DESC;
```

-   `ASC` → smallest → largest
-   `DESC` → largest → smallest

Multiple columns:

``` sql
ORDER BY customer_id ASC, balance DESC;
```

------------------------------------------------------------------------

# 5. LIMIT / OFFSET

``` sql
SELECT *
FROM customers
LIMIT 10;
```

Pagination-style example:

``` sql
SELECT *
FROM customers
LIMIT 10 OFFSET 20;
```

------------------------------------------------------------------------

# 6. DISTINCT

Removes duplicate result values.

``` sql
SELECT DISTINCT customer_id
FROM accounts;
```

Common interview use:

``` sql
COUNT(DISTINCT customer_id)
```

------------------------------------------------------------------------

# 7. INSERT / UPDATE / DELETE

## INSERT

``` sql
INSERT INTO customers (customer_id, customer_name)
VALUES (1, 'Amit');
```

## UPDATE

``` sql
UPDATE customers
SET customer_name = 'Amit Kumar'
WHERE customer_id = 1;
```

## DELETE

``` sql
DELETE FROM customers
WHERE customer_id = 1;
```

⚠️ Always think carefully before running `UPDATE` or `DELETE` without
`WHERE`.

------------------------------------------------------------------------

# 8. Aggregate Functions

Main aggregates:

``` text
COUNT()
SUM()
AVG()
MIN()
MAX()
```

Example:

``` sql
SELECT
    SUM(balance) AS total_balance,
    AVG(balance) AS average_balance,
    MAX(balance) AS highest_balance,
    MIN(balance) AS lowest_balance
FROM accounts;
```

## COUNT --- Important

``` sql
COUNT(*)
```

Counts rows.

``` sql
COUNT(balance)
```

Counts non-NULL `balance` values.

``` sql
COUNT(DISTINCT customer_id)
```

Counts unique non-NULL customer IDs.

### Interview trap

`COUNT(column)` ignores NULL.

------------------------------------------------------------------------

# 9. GROUP BY

Use `GROUP BY` when you want an aggregate **per category/entity**.

``` sql
SELECT
    customer_id,
    SUM(balance) AS total_balance
FROM accounts
GROUP BY customer_id;
```

Think:

``` text
GROUP BY → creates groups
SUM/COUNT/AVG/etc. → calculates inside each group
```

------------------------------------------------------------------------

# 10. WHERE vs HAVING

## WHERE

Filters rows **before** grouping.

``` sql
SELECT customer_id, SUM(balance)
FROM accounts
WHERE balance > 500
GROUP BY customer_id;
```

## HAVING

Filters groups **after** aggregation.

``` sql
SELECT
    customer_id,
    SUM(balance) AS total_balance
FROM accounts
GROUP BY customer_id
HAVING SUM(balance) > 2000;
```

### Memorize

> **WHERE = rows**\
> **HAVING = groups**

------------------------------------------------------------------------

# 11. NULL

Correct:

``` sql
WHERE amount IS NULL
```

``` sql
WHERE amount IS NOT NULL
```

Incorrect:

``` sql
WHERE amount = NULL
```

## COALESCE

Replace NULL with a fallback value:

``` sql
COALESCE(SUM(a.balance), 0)
```

Very useful with `LEFT JOIN`.

------------------------------------------------------------------------

# 12. CASE

SQL conditional logic.

``` sql
SELECT
    customer_name,
    CASE
        WHEN balance >= 2000 THEN 'High'
        WHEN balance >= 1000 THEN 'Medium'
        ELSE 'Low'
    END AS category
FROM accounts;
```

Think:

``` text
IF / ELSE IF / ELSE
```

------------------------------------------------------------------------

# 13. JOINS

## INNER JOIN

Only matching rows.

``` sql
SELECT *
FROM customers AS c
INNER JOIN accounts AS a
    ON c.customer_id = a.customer_id;
```

## LEFT JOIN

Keep **everything from the left table**.

``` sql
SELECT *
FROM customers AS c
LEFT JOIN accounts AS a
    ON c.customer_id = a.customer_id;
```

If no account exists, account columns become NULL.

### Find customers with no account

``` sql
SELECT c.customer_name
FROM customers AS c
LEFT JOIN accounts AS a
    ON c.customer_id = a.customer_id
WHERE a.account_id IS NULL;
```

This is an important interview pattern.

## RIGHT JOIN

Keeps everything from the right table.

## FULL OUTER JOIN

Keeps rows from both sides and matches where possible.

------------------------------------------------------------------------

# 14. Multi-Table JOINs

Our banking relationship:

``` text
customers
    ↓
accounts
    ↓
transactions
```

Example:

``` sql
SELECT
    c.customer_name,
    a.account_id,
    t.amount
FROM customers AS c
LEFT JOIN accounts AS a
    ON c.customer_id = a.customer_id
LEFT JOIN transactions AS t
    ON a.account_id = t.account_id;
```

Before writing a JOIN, ask:

> **What is the relationship between these two tables?**

------------------------------------------------------------------------

# 15. JOIN Multiplication --- Very Important

Suppose:

``` text
1 customer
   ↓
2 accounts
   ↓
3 transactions
```

After joining, an account can appear multiple times because of its
transactions.

Therefore:

``` sql
COUNT(a.account_id)
```

can overcount accounts.

Use:

``` sql
COUNT(DISTINCT a.account_id)
```

when you want the number of unique accounts.

Likewise:

``` sql
COUNT(DISTINCT t.transaction_id)
```

for unique transactions.

### Important lesson

> **Never treat an ID as a count.**

Wrong:

``` sql
a.account_id > 1
```

Correct:

``` sql
HAVING COUNT(DISTINCT a.account_id) > 1
```

------------------------------------------------------------------------

# 16. Subqueries

A query inside another query.

## Highest value

``` sql
SELECT *
FROM transactions
WHERE amount = (
    SELECT MAX(amount)
    FROM transactions
);
```

## Above average

``` sql
SELECT customer_id
FROM accounts
GROUP BY customer_id
HAVING SUM(balance) > (
    SELECT AVG(balance)
    FROM accounts
);
```

------------------------------------------------------------------------

# 17. IN / NOT IN

``` sql
SELECT *
FROM customers
WHERE customer_id IN (1, 2, 3);
```

With a subquery:

``` sql
SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM accounts
);
```

### Caution

`NOT IN` can behave unexpectedly when NULL values are present.

For many "doesn't exist" interview problems, `NOT EXISTS` is often
easier to reason about.

------------------------------------------------------------------------

# 18. EXISTS / NOT EXISTS

`EXISTS` asks:

> Does at least one matching row exist?

``` sql
SELECT c.customer_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM accounts AS a
    WHERE a.customer_id = c.customer_id
);
```

`NOT EXISTS` asks:

> Does no matching row exist?

``` sql
SELECT c.customer_name
FROM customers AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM accounts AS a
    WHERE a.customer_id = c.customer_id
);
```

------------------------------------------------------------------------

# 19. Correlated Subquery

The inner query refers to the current row of the outer query.

``` sql
SELECT c.customer_name
FROM customers AS c
WHERE EXISTS (
    SELECT 1
    FROM accounts AS a
    WHERE a.customer_id = c.customer_id
);
```

Here:

``` text
c.customer_id
```

comes from the outer query.

------------------------------------------------------------------------

# 20. CTE --- Common Table Expression

A CTE gives a temporary name to a query result.

``` sql
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(a.balance) AS total_balance
    FROM customers AS c
    LEFT JOIN accounts AS a
        ON c.customer_id = a.customer_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT *
FROM customer_totals;
```

### Why use CTEs?

They make complex queries easier to:

-   break into steps
-   read
-   debug
-   reason about

### Complex SQL method

``` text
1. What is the final output?
2. What is the main entity?
3. What tables are required?
4. What JOINs are required?
5. Do I need aggregation?
6. Do I need WHERE or HAVING?
7. Do I need a subquery / CTE / window function?
8. Write it.
9. Check for duplicate rows.
```

------------------------------------------------------------------------

# 21. Window Functions

A window function calculates across related rows **without collapsing
the original rows**.

This is the major difference:

``` text
GROUP BY
→ collapses rows

WINDOW FUNCTION
→ keeps rows
```

------------------------------------------------------------------------

## AVG OVER

``` sql
SELECT
    customer_id,
    balance,
    AVG(balance) OVER () AS overall_average
FROM accounts;
```

Every row can see the overall average.

------------------------------------------------------------------------

# 22. PARTITION BY

Creates separate windows.

``` sql
SELECT
    customer_id,
    balance,
    AVG(balance) OVER (
        PARTITION BY customer_id
    ) AS customer_average
FROM accounts;
```

Think:

> `PARTITION BY` = "calculate separately for each group, but keep every
> row."

------------------------------------------------------------------------

# 23. ROW_NUMBER

Assigns a unique number to every row.

``` sql
ROW_NUMBER() OVER (
    ORDER BY amount DESC
) AS row_num
```

Useful for:

-   Top 1
-   Top N
-   Latest record
-   First record
-   Nth record per group

------------------------------------------------------------------------

# 24. RANK vs DENSE_RANK

Suppose:

``` text
1000
1000
500
```

### RANK

``` text
1000 → 1
1000 → 1
500  → 3
```

### DENSE_RANK

``` text
1000 → 1
1000 → 1
500  → 2
```

### Interview rule

Use:

``` sql
DENSE_RANK()
```

when you want **distinct ranking levels** and ties should not create
gaps.

------------------------------------------------------------------------

# 25. LAG / LEAD

## LAG

Previous row:

``` sql
LAG(amount) OVER (
    ORDER BY transaction_id
)
```

## LEAD

Next row:

``` sql
LEAD(amount) OVER (
    ORDER BY transaction_id
)
```

Useful for:

-   previous transaction
-   next transaction
-   month-over-month comparisons
-   change from previous value

------------------------------------------------------------------------

# DATABASE FUNDAMENTALS

# 26. Primary Key

A primary key:

-   uniquely identifies a row
-   cannot be NULL

``` sql
customer_id INT PRIMARY KEY
```

------------------------------------------------------------------------

# 27. Foreign Key

A foreign key references a key in another table.

``` sql
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id)
```

A foreign key **does not have to be unique**.

------------------------------------------------------------------------

# 28. Relationships

## One-to-Many

``` text
Customer
   ↓
Accounts
```

One customer can have many accounts.

## Many-to-Many

``` text
Students ↔ Courses
```

Use a junction table:

``` text
student_courses
----------------
student_id
course_id
```

Example:

``` text
student_id | course_id
1          | 101
1          | 102
2          | 102
```

------------------------------------------------------------------------

# 29. Normalization

Main purpose:

> Reduce unnecessary duplication and maintain consistency.

Instead of:

``` text
student_id | student_name | course_id | course_name
```

repeating data, separate:

``` text
students
courses
student_courses
```

### Benefits

-   less duplication
-   easier updates
-   better consistency
-   cleaner relationships

### Update anomaly

If Amit's name appears in 10 rows, changing his name requires updating
many rows.

Normalized design:

``` text
students
1 | Amit
```

The name is stored once.

------------------------------------------------------------------------

# 30. Constraints

## PRIMARY KEY

Unique identity + NOT NULL.

## FOREIGN KEY

Maintains relationships.

## NOT NULL

Value is required.

``` sql
student_name VARCHAR(100) NOT NULL
```

## UNIQUE

No duplicate values.

``` sql
email VARCHAR(255) UNIQUE
```

## CHECK

Value must satisfy a condition.

``` sql
age INT CHECK (age >= 18)
```

## DEFAULT

Used when a value is not supplied.

``` sql
status VARCHAR(20) DEFAULT 'active'
```

------------------------------------------------------------------------

# 31. Transactions

A transaction groups multiple operations into one logical unit.

Bank transfer:

``` text
Amit - £200
Priya + £200
```

Both operations should succeed together.

### COMMIT

``` sql
COMMIT;
```

Makes the transaction permanent.

### ROLLBACK

``` sql
ROLLBACK;
```

Undoes uncommitted changes.

------------------------------------------------------------------------

# 32. ACID

## A --- Atomicity

**All or nothing.**

If one part fails, don't leave a partial transaction.

## C --- Consistency

The transaction must preserve database rules and constraints.

## I --- Isolation

Concurrent transactions should not interfere incorrectly.

## D --- Durability

Committed changes survive crashes.

### Memory

``` text
A → All or nothing
C → Consistent state
I → Isolated concurrent work
D → Data survives commit
```

------------------------------------------------------------------------

# 33. Indexes

An index is a data structure that can speed up lookups.

``` sql
CREATE INDEX idx_account_id
ON transactions(account_id);
```

Useful when a column is frequently used for:

-   filtering
-   joining
-   certain lookup/sort operations

### Trade-offs

``` text
Faster reads
     +
Extra storage
     +
More maintenance during INSERT/UPDATE/DELETE
```

Do not blindly index every column.

Primary keys commonly already have indexes created by the database.

------------------------------------------------------------------------

# 34. Views

A view is a saved query that behaves like a virtual table.

``` sql
CREATE VIEW customer_balances AS
SELECT
    c.customer_name,
    a.balance
FROM customers AS c
JOIN accounts AS a
    ON c.customer_id = a.customer_id;
```

Then:

``` sql
SELECT *
FROM customer_balances;
```

### Why use views?

-   simplify repeated queries
-   provide controlled access
-   expose only required information

A normal view does not usually store a separate copy of the underlying
data.

------------------------------------------------------------------------

# PYTHON + SQLITE

# 35. Connection

``` python
import sqlite3

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()
```

Think:

``` text
connection → connection to database
cursor     → execute SQL
```

------------------------------------------------------------------------

# 36. Execute

``` python
cursor.execute("SELECT * FROM customers")
```

`execute()` sends the SQL statement to the database.

------------------------------------------------------------------------

# 37. Fetch

### One row

``` python
row = cursor.fetchone()
```

Example:

``` python
(1, 'Amit')
```

### Several rows

``` python
rows = cursor.fetchmany(3)
```

### All remaining rows

``` python
rows = cursor.fetchall()
```

Example:

``` python
[(1, 'Amit'), (2, 'Priya')]
```

------------------------------------------------------------------------

# 38. INSERT + COMMIT

``` python
cursor.execute("""
    INSERT INTO customers (customer_id, customer_name)
    VALUES (3, 'Rahul');
""")

connection.commit()
```

Remember:

``` text
cursor.execute()    → execute SQL
fetchone()          → one row
fetchmany(n)        → up to n rows
fetchall()          → all remaining rows
connection.commit() → save changes
```

------------------------------------------------------------------------

# INTERVIEW PATTERNS

# 39. Find Highest Value

``` sql
SELECT MAX(amount)
FROM transactions;
```

Or retrieve the row:

``` sql
SELECT *
FROM transactions
WHERE amount = (
    SELECT MAX(amount)
    FROM transactions
);
```

------------------------------------------------------------------------

# 40. Second-Highest Distinct Value

Window approach:

``` sql
WITH ranked AS (
    SELECT
        amount,
        DENSE_RANK() OVER (
            ORDER BY amount DESC
        ) AS rnk
    FROM transactions
)
SELECT amount
FROM ranked
WHERE rnk = 2;
```

------------------------------------------------------------------------

# 41. Above Average

``` sql
SELECT *
FROM accounts
WHERE balance > (
    SELECT AVG(balance)
    FROM accounts
);
```

For grouped totals, calculate the totals first and compare those totals
with their average.

------------------------------------------------------------------------

# 42. Find Missing Records

Classic pattern:

``` sql
SELECT c.customer_name
FROM customers AS c
LEFT JOIN accounts AS a
    ON c.customer_id = a.customer_id
WHERE a.account_id IS NULL;
```

Think:

``` text
LEFT JOIN
+
IS NULL
=
"find records with no match"
```

------------------------------------------------------------------------

# 43. Top N per Group

Typical approach:

``` sql
ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY amount DESC
)
```

Then filter the generated row number in an outer query/CTE.

------------------------------------------------------------------------

# 44. Previous / Next Record

Previous:

``` sql
LAG(amount) OVER (
    ORDER BY transaction_id
)
```

Next:

``` sql
LEAD(amount) OVER (
    ORDER BY transaction_id
)
```

------------------------------------------------------------------------

# 45. Common Interview Mistakes

## Mistake 1 --- ID is not a count

Wrong:

``` sql
account_id > 1
```

Correct:

``` sql
COUNT(account_id) > 1
```

After a one-to-many join:

``` sql
COUNT(DISTINCT account_id) > 1
```

------------------------------------------------------------------------

## Mistake 2 --- `= NULL`

Wrong:

``` sql
WHERE amount = NULL
```

Correct:

``` sql
WHERE amount IS NULL
```

------------------------------------------------------------------------

## Mistake 3 --- Aggregate in WHERE

Wrong:

``` sql
WHERE SUM(balance) > 2000
```

Correct:

``` sql
HAVING SUM(balance) > 2000
```

------------------------------------------------------------------------

## Mistake 4 --- Forgetting JOIN multiplication

Always ask:

> "Can this JOIN create multiple rows for one entity?"

If yes, reconsider `COUNT()`.

------------------------------------------------------------------------

## Mistake 5 --- Ungrouped selected columns

If you use:

``` sql
GROUP BY customer_id
```

don't casually select another non-aggregated column unless it is also
grouped or your database/query design explicitly supports it.

------------------------------------------------------------------------

# 46. SQL Interview Checklist

Before submitting a query, ask:

``` text
□ Did I identify the correct main table?
□ Are my JOIN conditions correct?
□ Could the JOIN duplicate rows?
□ Do I need COUNT(DISTINCT)?
□ Is this a row filter or group filter?
□ WHERE or HAVING?
□ Do I need GROUP BY?
□ Do I need a subquery?
□ Would a CTE make this clearer?
□ Do I need a window function?
□ What happens with NULL?
□ Are ties possible?
□ Do I need RANK, DENSE_RANK, or ROW_NUMBER?
□ Can I explain every line?
```

------------------------------------------------------------------------

# 47. Practice Dataset

## customers

``` text
customer_id | customer_name
1           | Amit
2           | Priya
3           | Rahul
4           | Neha
```

## accounts

``` text
account_id | customer_id | balance
101        | 1           | 1500
102        | 2           | 2300
103        | 3           | 800
104        | 1           | 1200
```

## transactions

``` text
transaction_id | account_id | amount
1              | 101        | 500
2              | 101        | 200
3              | 102        | 1000
```

Useful facts:

``` text
Amit   → 2 accounts → 2700 balance → 700 transactions
Priya  → 1 account  → 2300 balance → 1000 transactions
Rahul  → 1 account  → 800 balance  → 0 transactions
Neha   → 0 accounts → 0 balance    → 0 transactions
```

------------------------------------------------------------------------

# 48. Current Phoenix Status

## Completed

-   Python
-   OOP
-   Bank Management System
-   SOLID
-   DSA foundational pass
-   SQL + Database Fundamentals

## Current

**SQL → Interview Preparation**

Focus:

``` text
Practice
→ Reason
→ Write
→ Debug
→ Explain
→ Improve
```

## Next Phoenix Phase

**NumPy → Pandas → Data Analysis**

SQL should remain active through interview questions, but it is no
longer an open-ended learning phase.

------------------------------------------------------------------------

# Final Rule

> **Do not memorize SQL queries. Learn the patterns.**

For every interview question, first ask:

``` text
What am I returning?
What is my main entity?
Which tables do I need?
How are they related?
Do I need aggregation?
Do I need a row filter or group filter?
Could my JOIN duplicate rows?
Do I need a subquery, CTE, or window function?
```

Then write the SQL.
