def main():
    students = {}  # 学号: {"name": 姓名, "scores": {科目: 分}}
    while True:
        print("\n1.录入 2.查询 3.统计 4.退出")
        c = input("选择: ").strip()
        if c == '1':
            sid = input("学号: ").strip()
            if sid in students:
                print("学号已存在!"); continue
            name = input("姓名: ").strip()
            scores = {}
            print("输入科目=分数，空行结束")
            while True:
                e = input().strip()
                if not e: break
                if '=' not in e:
                    print("格式: 科目=分数"); continue
                subj, s = e.split('=', 1)
                try: scores[subj.strip()] = float(s)
                except: print("分数需数字")
            students[sid] = {"name": name, "scores": scores}
            print(f"{name}({sid}) 已录入")
        elif c == '2':
            sid = input("学号: ").strip()
            s = students.get(sid)
            if s: print(f"{s['name']} {s['scores']}")
            else: print("未找到")
        elif c == '3':
            sid = input("学号: ").strip()
            s = students.get(sid)
            if not s or not s['scores']:
                print("无成绩"); continue
            vals = list(s['scores'].values())
            avg = sum(vals)/len(vals)
            mx, mn = max(vals), min(vals)
            print(f"平均:{avg:.2f} 最高:{mx} 最低:{mn}")
        elif c == '4': break
        else: print("无效选项")

if __name__ == "__main__": main()