from collections import Counter
line_seen = set()
with open( '/Users/student/Downloads/inputfile1.txt', 'r') as f:
        d = 0

        c = Counter(c.strip() for c in f if c.strip())
        for line in c:
                if c[line]>1:
                        print(line)
                d += 1
        if d >= 1:
                print("Duplicates tasks found:",d)
        else:
                print("No duplicates found, all ready to go!")
