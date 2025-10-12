# 전달값, 반환값


# 계좌 입출금 기능 함수 구현
balance = 0 # 잔액(잔고)
print("잔액: {0}".format(balance))

 # 1. 입금
def deposit(balance, money):
  print("-" * 70 + "[deposit]")
  print("{}원 출금 시도".format(money))
  print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance + money))
  return balance + money
balance = deposit(balance, 1000) # 입금액 1000원
print("잔액: {0}".format(balance))

# 2. 출금
def withdraw(balance, money):
  print("-" * 70 + "[withdraw]")
  if (balance < money): 
    print("{}원 출금 시도".format(money))
    print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
    return balance
  print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
  return balance - money
print("잔액: {0}".format(balance))
balance = withdraw(balance, 1500) # 출금액 1500원
balance = withdraw(balance, 500) # 출금액 500원
print("잔액: {0}".format(balance))

# 3. 출금(저녁 수수료)
def withdraw_night(balance, money):
  print("-" * 70 + "[withdraw_night]")
  print("{}원 출금 시도".format(money))
  commission = 100 # 수수료 100원
  if (balance - commission < money): 
    print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
    return commission, balance
  print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money - commission))
  return commission, balance - money - commission # 튜플 언패킹 형식으로 반환

commission, balance = withdraw_night(balance, 500)
commission, balance = withdraw_night(balance, 300)
print("수수료: {0}, 잔액: {1}".format(commission, balance))