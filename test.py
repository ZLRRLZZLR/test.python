count = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a != b and b != c:
                print(f'{a}{b}{c}')
                count+=1
print(count)