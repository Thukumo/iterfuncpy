class iter_func:
    """
    An iterator class that generates strings by replacing wildcard characters in a given input string.
    Args:
        func (function): The function to be applied to each generated string.
        inputstr (str): The input string containing wildcard characters to be replaced.
        l (str, optional): The list of replacement characters. Defaults to "0123456789".
        begin_at (str, optional): The string to be started from. Defaults to None.
        sp_char (str, optional): The wildcard character. Defaults to "?".
    Raises:
        ValueError: If the length of the list of replacement characters is zero.
    Attributes:
        __func (function): The function to be applied to each generated string.
        __inputstr (str): The input string containing wildcard characters to be replaced.
        __l (str): The list of replacement characters.
        __sp_char (str): The wildcard character.
        __n (int): The number of wildcard characters in the input string.
        __ln (int): The length of the list of replacement characters.
        __finum (int): The total number of possible combinations.
        __spstr (list): The list of substrings between wildcard characters.
        __lspstr (int): The length of the list of substrings.
        __stnum (list): The current state of each wildcard position.
    Methods:
        __iter__(): Returns the iterator object itself.
        __len__(): Returns the total number of possible combinations.
        __next__(): Generates the next string by replacing wildcard characters.
        __gen_string(l): Generates the string by replacing wildcard characters with the given list of replacement characters.
    """
    def __init__(self, func, inputstr, l="0123456789", begin_at: str = None, sp_char="?"):
        self.__func, self.__inputstr, self.__l, self.__sp_char = func, inputstr, l, sp_char
        self.__n, self.__ln = inputstr.count(sp_char), len(l)
        self.__finum = self.__ln**self.__n
        self.__spstr = inputstr.split(sp_char)
        self.__lspstr = len(self.__spstr)
        if self.__ln == 0: raise ValueError("Length of the list of replacement character(s) must not equal zero.")
        self.__stnum = [0 for _ in range(self.__n)]
        self.__stnum[0] = -1
        if begin_at != None:
            for num, i in enumerate([i for i in range(len(inputstr)) if inputstr[i] == sp_char]):
                self.__stnum[self.__n-num-1] = l.index(begin_at[i])
            self.__stnum[0] -= 1

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
        #return self.__func(gen_string(self.s, [self.__l[self.__stnum[self.__n-i-1]] for i in range(self.__n)], self.__sp_char))
        return self.__func(self.__gen_string([self.__l[self.__stnum[self.__n-i-1]] for i in range(self.__n)]))
    def __gen_string(self, l):
        if self.__lspstr == 1: return self.__spstr[0]
        return "".join(self.__spstr[i] + l[i] for i in range(self.__n))+self.__spstr[-1]

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
    if len(l)+1 != (le := len(sps := s.split(sp_char))): raise ValueError(f"Length of l must be equal to the number of sp_char('{sp_char}') in s.")
    if le == 1: return s
    return "".join(sps[i] + l[i] for i in range(len(l)))+sps[-1]
