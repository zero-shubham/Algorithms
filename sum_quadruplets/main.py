from datetime import datetime


def get_nplets(list_of_numbers, target, placeholder):
    res = []
    for idx, n in enumerate(list_of_numbers):
        if placeholder == 0:
            return []
        if placeholder == 1:
            return [target] if target in list_of_numbers else []

        if n == 0:
            continue
        factor = target // n
        if (
            factor > placeholder
        ):  # * with this we can avoid a lot of unnecessary iterations
            # * with - completed in  0:00:00.000066
            # * without -completed in  0:00:00.000099
            continue

        while factor > 0:
            res_list = [n] * factor

            ret_list = get_nplets(
                list_of_numbers[idx + 1 :],
                target - (factor * n),
                placeholder - factor,
            )
            for r in ret_list:
                if isinstance(r, list):
                    res.append([*res_list, *r])
                else:
                    res.append([*res_list, r])

            if factor == placeholder and target - (factor * n) == 0:
                res.append(res_list)

            factor -= 1

    return res


def quadruplets(list_of_numbers, target):
    start = datetime.now()
    list_of_numbers.sort()
    list_of_numbers = list(reversed(list_of_numbers))
    resulting_combinaitons = get_nplets(list_of_numbers, target, 4)
    print("completed in ", datetime.now() - start)
    return [tuple(r) for r in resulting_combinaitons]


print(quadruplets([0, 5, 2, 3, 4, 1], 11))


print(quadruplets([0, 5, 2, 3, 4, 1, 7, 8, 12], 29))

print(quadruplets([i for i in range(0, 100)], 33))
