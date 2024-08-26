class iter_func:
    """
    A class that generates an iterator for a given function and input string.
    Args:
        func (function): The function to be applied to each generated string.
        inputstr (str): The input string containing placeholders.
        l (str, optional): The characters to be used for replacement. Defaults to "0123456789".
        sp_char (str, optional): The placeholder character. Defaults to "?".
    Methods:
        __iter__(): Returns the iterator object.
        __len__(): Returns the total number of iterations.
        __next__(): Returns the next generated string.
    Raises:
        StopIteration: Raised when there are no more iterations.
    Example:
        # Create an instance of iter_func
        iterator = iter_func(lambda x: x, "abc?def")
        # Iterate over the generated strings
        for string in iterator:
            print(string) # abc0def, abc1def, ..., abc9def
        # This is same as
        for _ in iter_func(print, "abc?def"): pass
    """
    def __init__(self, func, inputstr, l="0123456789", sp_char="?"):
        self.__func, self.__inputstr, self.__l, self.__sp_char = func, inputstr, l, sp_char
        self.__n, self.__ln, self.__num = inputstr.count(sp_char), len(l), 0
        self.__finum = self.__ln**self.__n
        self.__spstr = inputstr.split(sp_char)
        if self.__n <= 0 or self.__ln <= 0: raise ValueError("Number of placeholders and replacement characters must be greater than 0.")
        self.__stnum = [0 for _ in range(self.__n)]
        self.__stnum[0] = -1

    def __iter__(self):
        return self

    def __len__(self):
        return self.__finum

    def __next__(self):
        if all(i == self.__ln-1 for i in self.__stnum): raise StopIteration()
        self.__stnum[0] += 1
        for i in range(self.__n-1):
            if self.__stnum[i] == self.__ln:
                self.__stnum[i] = 0
                self.__stnum[i+1] += 1
            else:
                break
        return self.__func(generate_string(self.__inputstr, [self.__l[self.__stnum[self.__n-i-1]] for i in range(self.__n)], self.__sp_char))

def generate_string(s, l, sp_char="?"):
    """
    Generate a string by inserting elements from list `l` into string `s` at each occurrence of `sp_char`.

    Args:
        s (str): The original string.
        l (list): The list of elements to be inserted into `s`.
        sp_char (str, optional): The special character used to identify the insertion points in `s`. Defaults to "?".

    Raises:
        ValueError: If the length of `l` is not equal to the number of occurrences of `sp_char` in `s`.

    Returns:
        str: The generated string with elements from `l` inserted at the appropriate positions.

    Example:
        >>> generate_string("Hello ? ? world", ["beautiful", "cruel"])
        'Hello beautiful cruel world'
    """
    if len(l)+1 != len(sps := s.split(sp_char)): raise ValueError(f"Length of l must be equal to the number of sp_char('{sp_char}') in s.")
    return "".join(sps[i] + l[i] for i in range(len(l)))+sps[-1]
