import os
import time
import re


def line_break(line=20):
    print('='*line)

#main func
def help():
    os.system('clear')
    line_break(30)
    print(
'''
///// HELP ////////
[clone] - To clone private repo please enter the github repo url,
Enter your generated ghp keys in github to able use this.

[exit] - Input exit on command line to close the script
//////////////////
'''
    )
    line_break(30)

def pop_up(params):
    os.system(f"xdg-open '{params}'")


def main(uri, token):
    if not token.startswith('ghp'):
        print('[!] Wrong or Invalid token!, please open your github and set an token for this operation.')
        time.sleep(5)
        pop_up('https://github.com/settings/tokens')
    else:
        
        username = re.search('/(?:github\.com)\/([^\/]*)/', uri).group(1)
        project_name = re.search(r"(?:github\.com)\/[\S]+\/([\S]+).+?(?=git)", uri).group(1)
        print(project_name, username)
        #os.system(f'https://{token}@github.com/{username}/{project_name}.git')


def temporary():
    project_name = str(input('project name ----> '))
    username  = str(input('username ----> '))
    ghp =  str(input('Token ----> '))

    os.system(f' git clone https://{ghp}@github.com/{username}/{project_name}.git')

def front():
    line_break(30)
    print(
'''
Welcome to Private Github REPO cloner v.1
--------- Info -------------------------
> for help or instructions please type [h]
> for exiting the script please type [exit]
'''
    )
    line_break(30)
front()
while True:
    url = (input('[*] Please input Github Private repo URL ----> '))
    try:
        username = re.search('/(?:github\.com)\/([^\/]*)/', url).group(1)
    except:
        username = False
    if url == 'h' or url == 'H':
        help()
    if url == 'exit' or url == 'Exit':
        break
    if url == 't' or url == 'T':
        temporary()
    elif username:
        os.system('clear')
        print(f'Github Repo: {url}')
        line_break()
        ghp = str(input('[*] Please Input your Github Token ----> '))
        main(url, ghp)
    else:
        os.system('clear')
        front()
        print('[!] Wrong or Invalid url, please try again')


