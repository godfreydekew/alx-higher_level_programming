def best_score(a_dictionary):
    if a_dictionary is not None:
        my_max = max(a_dictionary.values())
        for k, v in a_dictionary.items():
            if v == my_max:
                return k
    else:
        return None
