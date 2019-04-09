#Variables
year = 12

#Savings account
sfee = 10
sinterest = 0.04

#Checking account
cfee = 25
cinterest = 0.03
cinterest2 = 0.05

#Code begins here
acc = int(input('Enter account number:'))
accType = raw_input('Enter S for savings\nEnter C for checking\n')

#Savings account
if accType is 's' or accType is 'S':
   minBalance = int(input('Enter minimum balance for savings account:'))
   balance = int(input('Enter your saving account balance:'))
   
   if balance < minBalance:
      balance -= sfee
      print 'Your account number is:',acc
      print 'Your account type is a savings account'
      print 'Your current balance is: $',format(balance,'.2f')
      print 'You were charged a $',format(sfee,'.2f'),' fee for not maintaining the minimum balance on your savings account'
   
   elif balance >= minBalance:
      totalI = (sinterest * balance)/year
      balance += totalI
      print 'Your account number is:',acc
      print 'Your account type is a savings account'
      print 'Your current balance is: $',format(balance,'.2f')
      print 'You received $',format(totalI,'.2f'),' in interest for mainintaining more than the minimum balance on your savings account'
      
#Checking account
elif accType is 'c' or accType is 'C':
   minBalance = int(input('Enter minimum balance for checking account:'))
   balance = int(input('Enter your checking account balance:'))
   
   if balance < minBalance:
      balance -= cfee
      print 'Your account number is:',acc
      print 'Your account type is a checking account'
      print 'Your current balance is: $',format(balance,'.2f')
      print 'You were charged a $',format(cfee,'.2f'),' fee for not maintaining the minimum balance on your checking account'
   
   elif balance >= minBalance + 5000:
      totalI = (cinterest * balance)/year
      balance += totalI
      print 'Your account number is:',acc
      print 'Your account type is a checking account'
      print 'Your current balance is: $',format(balance,'.2f')
      print 'You received $',format(totalI,'.2f'),' in interest for mainintaining more than the minimum balance on your checking account'
      
   else:
      totalI = (cinterest2 * balance)/year
      balance += totalI
      print 'Your account number is:',acc
      print 'Your account type is a checking account'
      print 'Your current balance is: $',format(balance,'.2f')
      print 'You received $',format(totalI,'.2f'),' in interest for mainintaining more than the minimum balance on your checking account'