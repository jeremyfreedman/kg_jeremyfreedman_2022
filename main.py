import sys
from collections import Counter

print(len(Counter(sys.argv[1])) >= len(Counter(sys.argv[2])))
