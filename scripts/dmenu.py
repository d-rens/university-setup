import subprocess

def dmenu(prompt, options, dmenu_args=[]):
    optionstr = '\n'.join(str(option).replace('\n', ' ') for option in options)
    args = ['dmenu']
    #if fuzzy:
        #args += ['-f']
    args += ['-p', prompt]
    args += dmenu_args
    args = [str(arg) for arg in args]

    result = subprocess.run(args, input=optionstr, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    returncode = result.returncode
    stdout = result.stdout.strip()

    if returncode != 0:
        # If there's an error, print stderr for debugging
        print(result.stderr)

    selected = stdout.strip()
    try:
        index = [str(opt).strip() for opt in options].index(selected)
    except ValueError:
        index = -1

    if returncode == 0:
        key = 0
    elif returncode == 1:
        key = -1
    elif returncode > 9:
        key = returncode - 9

    return key, index, selected
