def balance(openingSum, interestRate, taxFreeLimit, taxRate, numMonths):
    interestRate = interestRate/100
    taxRate = taxRate/100

    month = 0
    while month < numMonths:
        interest = openingSum*interestRate
        if openingSum >= taxFreeLimit:
            taxed = (openingSum-taxFreeLimit)*taxRate

        openingSum = openingSum + interest - (taxed if openingSum >= taxFreeLimit else 0)
        month += 1

    return openingSum


if __name__ == "__main__":
    balance = balance(19800, 2, 20000, 1, 2)
    print(balance)