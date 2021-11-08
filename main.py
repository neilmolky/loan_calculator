# loan calculator by neilmolky
# part of a project with jet brains academy
# https://hyperskill.org/

import math
import argparse

parser = argparse.ArgumentParser(
    description="This program will take values from a user about their loan in either annuity "
                "or differentiated form. "
                "The user may only calculate number of payments, the payment amount, or the loan "
                "principal according to the specifications below. The program is not able to calculate "
                "the interest rate"
                "--type indicates the type of payment: 'annuity' or 'diff' (differentiated). "
                "If --type is specified neither as 'annuity' nor as 'diff' or not specified at "
                "all you will run an error"
                "--payment is the monthly payment amount. "
                "For --type=diff, the calculator will give a different payment each period based upon "
                "the loan principle. the user must specify both periods and principal as the calculator "
                "is unable to calculate values from a list of differentiated monthly payments given by the user."
                "For --type=annuity the calculator will give a monthly payment that is he same each month "
                "and therefore, if the user knows the monthly repayment amount they can calculate other values."
                "--principal is used for calculations of both types of payment. It denotes the loan "
                "amount and can be calculated for the annuity type if the user inputs the interest, "
                "annuity payment, and periods."
                "--periods is used for calculations of both types of payment. It denotes the number "
                "of months needed to repay the loan. It can be calculated for the annuity type "
                "if the user provides the interest, annuity payment, and principal."
                "--interest is specified without a percent sign. Note that it can accept a floating-point"
                " value. "
                "Our loan calculator can't calculate the interest, so it must always be provided. "
                "The user wll always need to provide the type and interest rate alongside 2 other "
                "parameters"
                "Our loan calculator is unable to work with negative values"
                "Overpayment: the amount of interest paid over the whole term of the loan. will be "
                "provided on all calculations."
)

# Defining all possible inputs a user would need to access through the cmd console or terminal
# choices return None if left blank
# whereas integers and floats will return 0 as their default for the purposes of the program

parser.add_argument(
    "--type",
    choices=["annuity", "diff"],
    help="You must choose to calculate for either annuity or differentiated repayments"
)
parser.add_argument(
    "--principal",
    type=int,
    default=0,
    help="You may provide the loan principle if you know this"
)
parser.add_argument(
    "--payment",
    type=int,
    default=0,
    help="You may provide the annuity monthly payments if you know this"
)
parser.add_argument(
    "--periods",
    type=int,
    default=0,
    help="You may provide the repayment periods in months if you know this"
)
parser.add_argument(
    "--interest",
    type=float,
    default=0.0,
    help="You must provide an interest rate"
)

# transform the returned arguments into python variables

args = parser.parse_args()
annuity_or_diff = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest

# calculate nominal interest ie. monthly interest as a decimal
nominal = interest / 1200

# logic loop to eliminate negative values
if int(principal or periods or payment or interest) < 0:
    print("Incorrect parameters")
# following removing negative values we can move into calculations
else:
    # logic for annuity or differential repayments
    if annuity_or_diff == "diff":

        # Logic loop to isolate differential parameters for calculation
        # differential repayment require all parameters except payment
        # missing parameters at default value 0 return an error
        if (principal or periods or nominal) == 0:
            print("Incorrect parameters")

        # if payment parameter is missing, calculate differential monthly payments
        elif payment == 0:

            # first create a list to store monthly results in
            diff_payment = []

            # then use a for loop to complete calculation for each month
            # nb. as python indexes lists from 0, p in range periods begins at 0 months
            # the equation has been adjusted to accommodate this
            for p in range(periods):
                monthly_payment = math.ceil(
                    principal / periods + nominal * (principal - (principal * p / periods))
                                            )
                print(f"month {p + 1}: payment is {monthly_payment}")
                diff_payment.append(monthly_payment)

            # calculate overpayment by summing the values in the list and subtracting the principal
            overpayment = sum(diff_payment) - principal
            print(f"Overpayment = {overpayment}")

        # and in case someone enters all 5 parameters in an attempt to crash the program
        else:
            print("Incorrect parameters")

    # returning to logic loop for differential and annuity payments
    elif annuity_or_diff == "annuity":

        # There are 3 annuity calculations that could be requested.
        # another logic loop will derive which calculation to attempt from the values input by the user.
        # values that have not been input default to 0
        # but if more than 1 value is missing there will be an error

        # calculate principal providing we have values for payment interest and periods
        if principal == 0 and (payment and interest and periods) != 0:
            principal = math.floor(
                payment / ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1))
            )

            # return value to user for principal and overpayment
            print(f"Your loan principal = {principal}!")
            overpayment = payment * periods - principal
            print(f"Overpayment = {overpayment}")

        # calculate payment providing we have values for principal interest and periods
        elif payment == 0 and (principal and periods and interest) != 0:
            payment = math.ceil(
                (principal * ((nominal * (nominal + 1) ** periods) / ((1 + nominal) ** periods - 1)))
                                 )

            # return value to user for annuity payment and overpayment
            print(f"Your annuity payment = {payment}")
            overpayment = payment * periods - principal
            print(f"Overpayment = {overpayment}")

        # calculate repayment periods providing we have values for principal payment and interest
        elif periods == 0 and (principal and payment and interest) != 0:
            periods = math.ceil(
                math.log(payment / (payment - nominal * principal), (1 + nominal))
                                )

            # to return correct grammar new variables for month and year are defined
            # logic then returns another variable that is a string with correct grammar
            # there will be occasions where it will take exactly a year or not quite years
            # for these occasions the variable will be set to None
            years = (periods // 12)
            if years == 1:
                y = "1 year"
            elif years > 1:
                y = str(years) + " years"
            else:
                years = None

            months = (periods % 12)
            if months == 1:
                m = "1 month"
            elif months > 1:
                m = str(months) + " months"
            else:
                m = None

            # three possible sentence structures can be returned after the integer values have
            # been transformed to string values with their plural.
            # otherwise there are 8 sentence structures required
            if y is None:
                print(f"it will take {m} to repay your loan")
            elif m is None:
                print(f"it will take {y} to repay your loan")
            else:
                print(f"it will take {y} and {m} to repay your loan")

            # don't forget to return the overpayment too!
            overpayment = payment * periods - principal
            print(f"Overpayment = {overpayment}")

        # and finally, there is still the possibility someone will return all 5 parameters
        # to try and crash the program
        else:
            print("Incorrect parameters")
