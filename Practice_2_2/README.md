# Requirements

* Python 3.\*
* NumPy \*
* Pandas \*

# Exercise: Practice 2.2

```
Створіть структуру DataFrame та заповніть його випадковими числами
строковими даними (наприклад, турнірна таблиця). Виконайте
фільтрацію даних за довільними признаками.
```

# How to run

**1.1**

From the command prompt start `main.py` in the project folder

*This realization has no GUI support so all work will be done in the console*

---

**1.2**

This realization has no user input, so after running you will see the result of the work

**Sample:**
```
Generated tournament table 
       Name Grade  Class
0     Emil     C      1
1     Beta     F      2
2     Emil     C      5
3      Jim     A      5
4  Daniels     D      4
Filtered by bigger than grade 
   Name Grade  Class
3  Jim     A      5
Filtered by smaller than grade 
       Name Grade  Class
0     Emil     C      1
1     Beta     F      2
2     Emil     C      5
4  Daniels     D      4
Filtered by bigger than class 
       Name Grade  Class
1     Beta     F      2
2     Emil     C      5
3      Jim     A      5
4  Daniels     D      4
Filtered by smaller than class 
    Name Grade  Class
0  Emil     C      1
1  Beta     F      2
```

---