file = open('quotes.txt','a')

print('Keep Entering Quotes. Type quit to break .......')
quote = input('Enter a Quote : ')

while quote != 'quit' :
    file.write(quote)
    file.write('\n')
    print('Quote Saved.......')
    quote = input('Enter a Quote : ')