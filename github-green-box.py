import datetime
import os

from random import randint

def write_log(date):
  f = open('log.txt', 'a+')
  f.writelines(date.isoformat() + '\n')
  f.close()

def commit_github(date):
  os.system('git add .')
  os.system('git commit --date={date} -m "Update {date}."'.format(date=date.isoformat()))

def transformation(date) -> datetime.date:
  return datetime.timedelta(hours=randint(0, 24), minutes=randint(0, 60), seconds=randint(0, 60))

if __name__ == "__main__":
  while True:
    print('Please enter you want to commit date (like 20190902): ', end='')

    commit_date = input()

    if commit_date == '' or len(commit_date) != 8:
      print('\033[31mUnknown date, please enter the correct format !!')
      exit(1)

    print('Please enter the number of times you want to commit, it must be a number value: ', end='')

    commit_count = int(input())

    if commit_count <= 0:
      print('\033[31mPlease enter number and it greater than zero !!')
      exit(1)

    while commit_count > 0:
      date = datetime.datetime.strptime(commit_date, '%Y%m%d')
      date += transformation(date)

      write_log(date)
      commit_github(date)

      commit_count -= 1
