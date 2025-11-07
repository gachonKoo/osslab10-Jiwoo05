import sys

# 명령줄에서 입력받은 첫 번째 숫자
n = int(sys.argv[1])

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
