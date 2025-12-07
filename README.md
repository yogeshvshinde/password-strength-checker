About the project:
-------------------
Security is a crucial aspect, and ensuring strong passwords is essential. 
Create a Python script to check the strength of the password. 
● Implement a Python function called check_password_strength that takes a password string as input. 

● The function should check the password against the following criteria: 
  ○ Minimum length: The password should be at least 8 characters long. 
  ○ Contains both uppercase and lowercase letters. 
  ○ Contains at least one digit (0-9). 
  ○ Contains at least one special character (e.g., !, @, #, $, %). 

● The function should return a boolean value indicating whether the password meets the criteria. ● Write a script that takes user input for a password and calls the check_password_strength function to validate it. 
● Provide appropriate feedback to the user based on the strength of the password.

=================================================================================================

-> Password Strength Checker

A simple Python utility to evaluate the strength of passwords based on length, uppercase, lowercase and special characters.

Features
- Checks for minimum length.
- Evaluates presence of uppercase, lowercase, digits, and special characters.
- Detects common weak patterns (e.g., "123456", "password").

- Returns a mnessage as below:
  Please enter a password to check its strength (or type 'exit' to quit): test
  Your password is weak. It is missing the following criteria:
      at least 8 characters long
      at least one uppercase letter
      at least one digit
      at least one special character
  
- Returns a detailed feedback : 
Length: Not Met
Uppercase: Met/Not Met
Lowercase: Met/Not Met

===========================================

Output screenshot:
<img width="385" height="227" alt="image" src="https://github.com/user-attachments/assets/1744b7b2-bf77-4c24-ab90-ecc28f492ae0" />

