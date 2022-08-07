import os
ind = 0
file = '/etc/hosts'
if os.geteuid() != 0:
    print("Please run with sudo, as it is required to edit /etc/hosts")
    quit(1)
print("Hello and welcome to webblock.py")
action = input("Choose action (unblock: 0/block: 1)")
if action == '1':
    w_addr = input("Enter address(es) to be blocked(sep with comma): ").split(',')
    with open(file, 'a') as w:
        for i in w_addr:
            w.write(i)
            w.write('\n')
elif action == '0':
    w_addr = input("address(es) to remove(sep with comma): ").split(',')
    with open(file, 'r') as f:
        l = f.readlines()
    with open(file, 'w') as f:
        for line in l:
            if line.strip("\n") not in w_addr:
                f.write(line)
        f.write("\n")
            