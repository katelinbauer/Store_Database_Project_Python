# Store Database Project 

## Description:

This project is a 5-module Python program for a store management system that builds databases of customers, purchases, and employees.

The program includes a set up module for database initialization and a query module allowing a manager to extract valuable statistics on customer purchases. Additional modules explore store profit margins and analyze customer spending and work attendance trends.

## Modules: 

## 1. Database Set Up 

The set-up module consists of two databases:

a. A people database is represented as a list. Each person is denoted by a list containing a 3-element tuple, a string indicating employee/customer status, and either an integer (for employees) or a list (for customers). The data for individuals consists of fixed details stored in tuples, including name, ID, and birth year. Variable information is stored in lists, such as salary, employee/customer status, days missed (for employees), and a list of purchases (for customers). The store's overhead cost is also considered.
   
b. A purchases database structured as a dictionary. Customer IDs serve as keys, and the corresponding values are lists containing purchase details in the form of two-element lists

## 2. Query the Customer Database

In this module, users input a customer ID, and the system responds by displaying a list of all purchases made by that customer and the total purchase price. If the provided ID corresponds to an employee, the program communicates that the ID doesn't pertain to a customer. The option to cease querying is available by entering 0.

## 3. Store Profit Margin 

The objective of this module is to determine the financial status of the store, whether it is operating with a profit (in the black) or facing a deficit (in the red). The assessment is conducted through the following logic:
If the result of [(Total Customers’ Purchases) - (Total Employees’ Salaries + Overhead)] is greater than 0, the store is considered to be in the black; otherwise, it is in the red.

## 4. Spending and Skipping Behavior Analysis

This module aims to investigate the potential influence of age and salary on the following aspects:

a. Customer Spending Behavior

- Age/Salary Low: Average expenses incurred by younger customers with lower salaries.
- Age/Salary High: Average expenses incurred by younger customers with higher salaries.
- Age/Salary Low: Average expenses incurred by older customers with lower salaries.
- Age/Salary High: Average expenses incurred by older customers with higher salaries.

b. Work Attendance

- Age/Salary Low: Average number of missed workdays for younger employees with lower salaries.
- Age/Salary High: Average number of missed workdays for younger employees with higher salaries.
- Age/Salary Low: Average number of missed workdays for older customers with lower salaries.
- Age/Salary High: Average number of missed workdays for older customers with higher salaries.

## 5. Greatest (Count) Behavior Analysis

The objective of this module is to identify:

The top spender:
The customer whose total purchases surpass those of all other customers.

The most frequent absentee:
The employee or employees who have the highest count of missed workdays.
