# ALL THESE CRASH ON 10GB FILES 💥
with open('10GB.csv') as f:
    data = f.read()              # 10GB string → OOM
    lines = f.readlines()        # 10GB list → OOM  
    all_lines = list(f)          # 10GB list → OOM


# ✅ SAFE (Constant RAM):
# for line in f: pass     # ~8KB forever
# ❌ DANGEROUS (10GB+ RAM):
# f.read()               # 10GB string
# f.readlines()          # 10GB list  
# list(f)                # 10GB list


# this will not load whole file in memory, it would go on each line 1 by 1
# with open(filepath, 'r') as f:
    # for line_num, line in enumerate(f, 1):
        # event = parse_line(line)

