# Enter your code here. Read input from STDIN. Print output to STDOUT

s = [i for i in input()]

upper = ''.join(sorted(list(filter(lambda x: x.isupper(), s))))
lower =  ''.join(sorted(list(filter(lambda x: x.islower(), s))))
odd =  ''.join(sorted(list(filter(lambda x: (x.isdigit() == True) and (int(x)%2 != 0), s))))
even =  ''.join(sorted(list(filter(lambda x: (x.isdigit() == True) and (int(x)%2 == 0), s))))

print(''.join([lower, upper, odd, even]))
