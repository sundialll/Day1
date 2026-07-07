import math, os

HIST = "calc_history.txt"

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b==0: raise ValueError("除数0")
    return a/b
def pwr(a,b): return a**b
def sqr(a):
    if a<0: raise ValueError("负数无实根")
    return math.sqrt(a)

def log(op, res):
    with open(HIST,"a",encoding="utf-8") as f:
        f.write(f"{op} = {res}\n")

def show_hist():
    if not os.path.exists(HIST) or os.stat(HIST).st_size==0:
        print("无历史"); return
    print("===历史===")
    with open(HIST,"r",encoding="utf-8") as f:
        for l in f: print(l.strip())

def get2():
    try: return float(input("a:")), float(input("b:"))
    except: print("需数字"); return None,None

def get1():
    try: return float(input("a:"))
    except: print("需数字"); return None

def main():
    while True:
        print("\n1.+ 2.- 3.* 4./ 5.^ 6.√ 7.历史 8.退出")
        c = input("选择: ").strip()
        if c in '12345':
            a,b = get2()
            if a is None: continue
            try:
                res = [add,sub,mul,div,pwr][int(c)-1](a,b)
            except ValueError as e: print(e); continue
            op = f"{a}{'+-*/^'[int(c)-1]}{b}"
            print(res); log(op,res)
        elif c == '6':
            a = get1()
            if a is None: continue
            try: res = sqr(a)
            except ValueError as e: print(e); continue
            print(res); log(f"√{a}",res)
        elif c == '7': show_hist()
        elif c == '8': break
        else: print("无效")

if __name__ == "__main__": main()