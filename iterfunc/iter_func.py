class iter_func:
    def __init__(self, func, inputstr, l="0123456789", sp_char="?"):
        self.func, self.inputstr, self.l, self.sp_char = func, inputstr, l, sp_char
        self.n, self.ln, self.num = inputstr.count(sp_char), len(l), 0
        self.finum = self.ln**self.n
        self.spstr = inputstr.split(sp_char)

    def __iter__(self):
        return self

    def __len__(self):
        return self.finum

    def __next__(self):
        if self.num == self.finum: raise StopIteration()
        stnum = "".join(["0" for _ in range(self.n-len(str(self.num)))])+str(self.num)
        self.num += 1
        return self.func(generate_string(self.inputstr, [self.l[int(stnum[i])] for i in range(self.n)], self.sp_char))

def generate_string(s, l, sp_char="?"):
    if len(l)+1 != len(sps := s.split(sp_char)): raise ValueError(f"Length of l must be equal to the number of sp_char('{sp_char}') in s.") #例外の種類これでいい？
    return "".join(sps[i] + l[i] for i in range(len(l)))+sps[-1]
