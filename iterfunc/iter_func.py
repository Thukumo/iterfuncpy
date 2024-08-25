def generate_string(s, l):
    """
    Replaces each occurrence of "?" in the string `s` with the elements of the list `l` one by one.

    Args:
        s (str): The input string.
        l (list): The list of elements to replace "?" with.

    Returns:
        str: The modified string with "?" replaced by elements from the list.
    """
    """
    for i in range(len(l)):
        s = s.replace("?", l[i], 1)
    return s
    """
    sps = s.split("?")
    if len(l)+1 != len(sps): Exception("Length of l must be equal to the number of '?' in s.")
    return "".join(sps[i] + l[i] for i in range(len(l)))+sps[-1]

def iter_func(func, inputstr, l="0123456789", tqdm=None):
    """
    Generate combinations of characters based on the given input string.

    Args:
        func (function): The function to apply to each generated combination.
        inputstr (str): The input string containing '?' as placeholders for characters to be replaced.
        l (str, optional): The characters to use for replacement. Defaults to "0123456789".
        tqdm (function, optional): A progress bar function. Defaults to None.

    Returns:
        list: A list of results obtained by applying the given function to each generated combination.
    """
    n, ln = inputstr.count("?"), len(l)
    lis = [0 for _ in range(n)] #位がでかいほうが前
    lis[-1] = -1
    res = []
    for _ in (tqdm if tqdm != None else lambda x: x)(range(ln**n)):
        lis[-1] += 1
        for i in range(n-1, 0, -1):
            if lis[i] == ln:
                lis[i] = 0
                lis[i-1] += 1
        res.append(func(generate_string(inputstr, [l[lis[i]] for i in range(n)])))
    return res
