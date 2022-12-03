import argparse
import sys
from math import ceil, floor, log, pow

parser = argparse.ArgumentParser(description='loan calculator compute all the parameters of the loan '
                                             'including loan with annuity payment and with differentiated payment')
parser.add_argument('--type', choices=['annuity', 'diff'], help='You need to choose type of payment: '
                                                                '"annuity" or "diff" (differentiated)')
parser.add_argument('--payment', type=float, help='the monthly payment amount only for type=annuity')
parser.add_argument('--principal', type=float, help='the loan principal')
parser.add_argument('--periods', type=int, help='the number of months needed to repay the loan')
parser.add_argument('--interest', type=float, help='interest is specified without a percent sign')

args = parser.parse_args()
list_args = sys.argv

if len(list_args) != 5 \
        or args.type is None \
        or args.interest is None \
        or args.interest < 0 \
        or (args.type == 'diff' and args.payment is not None) \
        or (args.payment is not None and args.payment < 0) \
        or (args.principal is not None and args.principal < 0) \
        or (args.periods is not None and args.periods < 0):
    print("Incorrect parameters.")
    exit()


def diff_payment(periods, principal):
    payments_all = 0
    for m in range(1, periods + 1):
        month_m = ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
        payments_all += month_m
        print(f'Month {m}: payment is {month_m}')
    overpayment = payments_all - principal
    print('Overpayment =', round(overpayment))


def annuity_overpayment(payment, periods, principal):
    overpayment = payment * periods - principal
    print('Overpayment =', round(overpayment))


def annuity_payment(periods, principal):
    payment = ceil(principal * (i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    print(f'Your annuity payment = {payment}!')
    annuity_overpayment(payment, periods, principal)


def annuity_principal(payment, periods):
    principal = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    print(f'Your loan principal = {principal:.0f}!')
    annuity_overpayment(payment, periods, principal)


def annuity_periods(principal, payment):
    x = payment / (payment - i * principal)
    base = 1 + i
    periods = ceil(log(x, base))

    if periods == 1:
        print('It will take 1 month to repay this loan!')
    elif periods >= 12:
        years = floor(periods / 12)
        months = periods - years * 12
        if months == 0:
            print(f'It will take {years} years to repay this loan!')
        else:
            print(f'It will take {years} years and {months} months to repay this loan!')
    else:
        print(f'It will take {periods} months to repay this loan!')
    annuity_overpayment(payment, periods, principal)


i = args.interest / (12 * 100)  # nominal interest rate
if args.type == 'diff':
    diff_payment(args.periods, args.principal)
elif args.type == 'annuity':
    if args.payment is None:
        annuity_payment(args.periods, args.principal)
    elif args.principal is None:
        annuity_principal(args.payment, args.periods)
    elif args.periods is None:
        annuity_periods(args.principal, args.payment)
