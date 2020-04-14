import pytest


def is_prime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
        return True


@pytest.mark.parametrize(
    "num, expect",
    [(1,False),
     (13,True),
     (4,False),
     ],
    ids=["case1","case2","case3"]
)

def test_is_prine(num, expect):
    assert is_prime(num) == expect