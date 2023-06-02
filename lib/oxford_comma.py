def oxford_comma(items):
    if (len(items) == 1):
        return "".join(items)
    elif (len(items) == 2):
        return " and ".join(items)
    else:
        items_end = items.pop()
        and_str = ", and "
        items_and = ", ".join(items) + and_str + items_end
        return items_and
        