# Ladder if/else structure for coupon-based discounts

promo_code = input('Enter Promo Code: ')
amount = float(input('Enter Amount: '))

if promo_code == 'zomato':
    if amount > 300:
        discount = 0.20 * amount
        if discount > amount:
            discount = amount
        print('You got a discount of ₹', discount)
        print('Please pay: ₹', amount - discount)
    else:
        print('Add ₹', (301 - amount), 'more to apply coupon.')

elif promo_code == 'bingo':
    if amount > 500:
        discount = 0.50 * amount
        if discount > 150:
            discount = 150
        print('You got a discount of ₹', discount)
        print('Please pay: ₹', amount - discount)
    else:
        print('Add ₹', (501 - amount), 'more to apply coupon.')

else:
    print('Invalid Coupon Code')