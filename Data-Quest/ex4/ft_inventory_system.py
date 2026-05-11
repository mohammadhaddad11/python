import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    result = {}

    for arg in sys.argv[1:]:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")

        if parts[0] in result:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue

        try:
            val = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
            continue

        result[parts[0]] = val

    print(f"Got inventory: {result}")

    res_lst = list(result.keys())
    print(f"Item list: {res_lst}")

    total = sum(result.values())
    print(f"Total quantity of the {len(result)} items: {total}")

    if len(res_lst) == 0:
        result.update({"magic_item": 1})
        print(f"Updated inventory: {result}")
    else:
        for i in res_lst:
            percentage = round(result[i] / total * 100, 1)
            print(f"Item {i} represents {percentage}%")

        most = res_lst[0]
        least = res_lst[0]

        for i in res_lst:
            if result[i] > result[most]:
                most = i
            if result[i] < result[least]:
                least = i

        print(f"Item most abundant: {most} with quantity {result[most]}")
        print(f"Item least abundant: {least} with quantity {result[least]}")

        result.update({"magic_item": 1})
        print(f"Updated inventory: {result}")