# Inventory Fundamentals (Python)

## Description

This program is a basic inventory system that allows the user to register products by entering their name, price, and amount.

---

## Objective
The objective of this project is to:
- Register products with name, price, and amount  
- Calculate the total cost (price * amount)    
- Display results clearly in the console  

---

## Functionality

The program asks the user to input the product name, price, and amount.  

To ensure correct data, it validates that both price and amount are numeric. If the user enters invalid data, the program shows an error message and keeps asking until a valid value is entered.

After validation, the program calculates the total cost by multiplying the price by the amount.  

All the product information (name, price, amount, and total) is stored in a dictionary and then added to a list, allowing multiple products to be registered.

---

## Process Logic

The program follows three main stages:

1. **Input**  
   The user enters the product name, price, and amount.

2. **Processing**  
   The program validates the numeric inputs and calculates the total cost.

3. **Output**  
   The product is stored in a list with all its information.

---

## Validation
- Price is validated using numeric conversion (`int`)
- Amount is also validated as a number  
- If invalid data is entered, the program displays an error and asks again  

---

## Data Structure
Products are stored in a list, where each product contains:
- Name  
- Price  
- Amount  
- Total cost  

This allows organized storage and easy access to the data.

---

## Flow Chart
![flow_chart](https://github.com/user-attachments/assets/315c7c29-8fdf-45a8-8d6a-0a619b8dfd17)

