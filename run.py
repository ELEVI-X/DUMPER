import os, platform
print(' checking updates');os.system('git pull -q')
bit = platform.architecture()[0]
if bit == '32bit':
    print(f' 32bit version not available ');exit()
elif bit == '64bit':
    import DUMPER
else:exit()
