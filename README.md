# loan_calculator

This program will take values from a user about their loan in either annuity
or differentiated form. 

The user may only calculate number of payments, the payment amount, or the loan 
principal according to the specifications below. The program is not able to calculate 
the interest rate

--type indicates the type of payment: 'annuity' or 'diff' (differentiated). 
If --type is specified neither as 'annuity' nor as 'diff' or not specified at 
all you will run an error

--payment is the monthly payment amount. 
For --type=diff, the calculator will give a different payment each period based upon 
the loan principle. the user must specify both periods and principal as the calculator 
is unable to calculate values from a list of differentiated monthly payments given by the user.

For --type=annuity the calculator will give a monthly payment that is he same each month 
and therefore, if the user knows the monthly repayment amount they can calculate other values.

--principal is used for calculations of both types of payment. It denotes the loan 
amount and can be calculated for the annuity type if the user inputs the interest, 
annuity payment, and periods.

--periods is used for calculations of both types of payment. It denotes the number 
of months needed to repay the loan. It can be calculated for the annuity type 
if the user provides the interest, annuity payment, and principal.

--interest is specified without a percent sign. Note that it can accept a floating-point
value. 
Our loan calculator can't calculate the interest, so it must always be provided.

The user wll always need to provide the type and interest rate alongside 2 other 
parameters.

Our loan calculator is unable to work with negative values.

Overpayment: the amount of interest paid over the whole term of the loan. will be 
provided on all calculations.
