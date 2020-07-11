import math
import random
from typing import Dict, List, Tuple


def split_data(data: List[str], weights: Tuple = (0.8, 0.2, 0.0), seed: int = 100) -> Dict:
    split = {}
    data2split = data.copy()
    random.seed(seed)
    random.shuffle(data2split)

    total_words = len(data2split)
    train_limit = math.floor(total_words * weights[0])
    test_limit = math.floor(total_words * weights[1] + total_words * weights[0])

    split['train'] = data2split[:train_limit]
    split['test'] = data2split[train_limit:test_limit]
    split['validation'] = data2split[test_limit:]

    return split
