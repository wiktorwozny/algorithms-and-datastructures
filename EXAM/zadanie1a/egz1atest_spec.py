# egz1atest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n  s hint
    (5, 5, 8),
    (10, 10, 36),
    (15, 15, 72),
    (20, 20, 95),
    (25, 25, 148),
    (30, 30, 224),
    (35, 35, 329),
    (40, 40, 408),
]


from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)

def gentest(n, s, hint):
    S = [my_randint(1, s+1) for _ in range(n)]
    return [S], hint

