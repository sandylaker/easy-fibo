import pytest

from easy_fibo import fibonacci


def test_fibonacci_neg_n():
    with pytest.raises(ValueError, match="n must be non-negative"):
        fibonacci(-1)


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4])
def test_fibonacci(n):
    ground_truth_dict = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}
    gt = ground_truth_dict[n]
    assert fibonacci(n) == gt
