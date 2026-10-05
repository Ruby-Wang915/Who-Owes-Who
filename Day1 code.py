money=float(input('請輸入總金額:'))
people=int(input('人數:'))
payer=input('付款人:')
friends=[]
for i in range(people):
    name=input('Name:')
    friends.append(name)

each=money/people
other_owe=money-each

print('參與者:',friends)
print('each one:',each)
print(payer,'收取',other_owe,'元')

for friend in friends:
    if friend!=payer:
        print(friend,'->',payer,each,'元')

