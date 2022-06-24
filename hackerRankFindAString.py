s = input()
sub = input()
ct = 0

while sub in s:  # 1
    ct += 1  # 2
    s = s[s.find(sub) + 1:]  # 3

print(ct)