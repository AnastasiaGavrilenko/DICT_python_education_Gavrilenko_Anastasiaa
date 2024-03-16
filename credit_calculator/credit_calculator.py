import argparse
import math

def diff_payment(principal, periods, interest):
    total_payment = 0
    for m in range(1, periods + 1):
        payment = math.ceil(principal / periods + interest / 100 / 12 * (principal - (principal * (m - 1) / periods)))
        total_payment += payment
        print(f"Month {m}: payment is {payment}")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")

def annuity_payment(principal, periods, interest_rate):
    if periods == 0:
        print("The number of periods cannot be zero.")
        return
    interest = interest_rate / 100 / 12
    annuity = math.ceil(principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
    print(f"Your annuity payment = {annuity}!")
    overpayment = annuity * periods - principal
    print(f"Overpayment = {overpayment}")

def loan_principal(payment, periods, interest):
    principal = math.floor(payment / ((interest / 100 / 12) * (1 - ((1 + (interest / 100 / 12)) ** -periods))))
    print(f"Your loan principal = {principal}!")
    overpayment = (payment * periods) - principal
    print(f"Overpayment = {overpayment}")

def num_of_payments(principal, payment, interest):
    periods = math.ceil(math.log(payment / (payment - (interest / 100 / 12) * principal), 1 + (interest / 100 / 12)))
    years = periods // 12
    months = periods % 12
    if years == 0:
        if months == 1:
            print("You need 1 month to repay this loan!")
        else:
            print(f"You need {months} months to repay this loan!")
    elif months == 0:
        if years == 1:
            print("You need 1 year to repay this loan!")
        else:
            print(f"You need {years} years to repay this loan!")
    else:
        print(f"You need {years} years and {months} months to repay this loan!")
    overpayment = (payment * periods) - principal
    print(f"Overpayment = {overpayment}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["diff", "annuity"], help="Choose the type of payment: 'diff' for differentiated and 'annuity' for annuity")
    parser.add_argument("--principal", type=int, help="Loan principal amount")
    parser.add_argument("--payment", type=int, help="Monthly payment amount")
    parser.add_argument("--periods", type=int, help="Number of months to repay the loan")
    parser.add_argument("--interest", type=float, help="Annual interest rate without percentage sign")
    args = parser.parse_args()

    if args.type is None:
        print("Incorrect parameters")
        return

    if args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        return

    if args.interest is None:
        print("Incorrect parameters")
        return

    if args.principal is not None and args.principal < 0:
        print("Incorrect parameters")
        return

    if args.periods is not None and args.periods < 0:
        print("Incorrect parameters")
        return

    if args.payment is not None and args.payment < 0:
        print("Incorrect parameters")
        return

    if args.type == "diff":
        diff_payment(args.principal, args.periods, args.interest / 12)
    elif args.type == "annuity":
        if args.payment is None:
            annuity_payment(args.principal, args.periods, args.interest / 12)
        elif args.principal is None:
            loan_principal(args.payment, args.periods, args.interest / 12)
        elif args.periods is None:
            num_of_payments(args.principal, args.payment, args.interest / 12)


if __name__ == "__main__":
    main()
