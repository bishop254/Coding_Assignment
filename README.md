# Coding_Assignment - Fermat Near Misses.

# Given the equation (a^n + b^n = c^n) where n > 2.

  We begin by taking a random rational fraction, raise it to (n) , lets call it (k/j).
  Perform (1 - Result)^(1/n).
  Convert the above result to a fraction to obtain a second rational fraction, lets call it (p/q).
  
  (k/j) and (p/q) are our two fractions.
  To find the common denominator we multiply (j) with (q).
  Our two fractions now look like (kq/jq) and (pj/qj).
  (kq/jq)^n + (pj/qj)^n = 1
  
  Our first number (a) equates to (kq)
  Our second number (b) equates to (pj)
  our third number (c) equates to (qj)
  
# Challenges
  Answers may not be very accurate but the ratio is close to one
  Some numbers are very large especially if 10000 is included in the max denominations when limiting descriptors
 
 # To-Do
  Will be checked to improve efficiency of the output especially by utilizing other libraries
  
# Run the file using the command
 - python3 fermat.py
 
 You are required to input (n) which is the power 
 And the number of trials to be done.
 

 
  
  
  
  
