# Console tree 
- Show git repositories in file system
    - Choose root directory with os.path.join and sys.argv
    - Find directories with git repos Os.walk() method
    - Skip .git repositories show their root directories  
    - Show git repo statistic for every root folder
    - Choose the type of statistics (git system call variaty (git rev-list --count HEAD, git shortlog -s -n, git log --graph )( topdown=True))
- Add graphic thee view 

How to run: python3 + console_tree.py + chosen directory name