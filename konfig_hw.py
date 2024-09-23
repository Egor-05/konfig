import argparse
import tarfile
import os


def exep(name, *args):
    print(f'{name} : команда не найдена')


def ls_funcs(files, command):
    files = [j for j in files if '.' in j]
    dirs = [j for j in files if '.' not in j]
    lst = files + dirs
    delim = '\n'
    for j in command:
        if j == 'r':
            lst.sort(reverse=True)
        elif j == 's':
            lst.sort()
        elif j == '1':
            delim = '\n'
    return delim.join(lst)


def ls(name, *args):
    com = ''
    if len(args) == 2:
        a = current + '/' + args[1].strip('/')
        if args[0][0] != '-':
            print('ls: unrecognised option: ' + args[1])
            return
        com = args[0][1:]
    elif not args or args[0] == '.':
        a = current
    elif len(args) == 1:
        a = current + '/' + args[0].strip('/')
    else:
        print('ls: unrecognised option: ' + args[2])
        return
    b = file_system.get(a, False)

    if b:
        print(ls_funcs(b, com))


def cd(name, *args):
    global current

    if len(args) > 1:
        print('bash: cd: слишком много аргументов')

    a = file_system[current]
    if args[0] in a:
        current += '/' + args[0]
    elif args[0] == '..':
        if len(current.split('/')) > 1:
            current = '/'.join(current.split('/')[:-1])
    elif args[0] == '.':
        pass
    else:
        print(f'bash: cd: {args[0]}: Нет такого файла или каталога')


def clear():
    os.system('clear')


def echo(name, *args):
    print(' '.join(args).strip('"'))


def ex(*args):
    os.system('exit')


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', default='default_user')
parser.add_argument('-p', '--path', required=True)
parser.add_argument('-s', '--script', required=True)

args = parser.parse_args()

file_system = {}
commands = {'ls': ls, 'cd': cd, 'echo': echo, 'clear': clear, 'exit': ex}
user = args.user
glob_path = args.path
path = args.script
# user = 'egor'
# glob_path = 'fs.tar'
# path = 'fs/ts1/script.txt'
with tarfile.open(glob_path, 'r') as f:
    with f.extractfile(path) as file:
        script = file.read().decode('utf-8')
    for i in f.getmembers():
        a = i.name.split('/')
        key = '/'.join(a[:-1])
        value = a[-1]
        file_system[key] = file_system.get(key, []) + [value]
    current = file_system[''][0]

for i in script.strip().split('\n'):
    s = i.split()
    func = commands.get(s[0], exep)
    func(*s)
while True:
    s = input(f'{user} ~/{current}$ ').split()
    func = commands.get(s[0], exep)
    func(*s)
