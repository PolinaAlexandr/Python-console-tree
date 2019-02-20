# Console tree 
- Show folders with git repos and their commit count in your folder system
    - Choose root directory with os.path.join and sys.argv
    - Find directories with ().git) repos Os.walk() method
    - Skip .git repositories show their root directories  
    - Show git repo statistic for every root folder
    - Choose the type of statistics (git statistic commands archive)(('git rev-list --count HEAD', 'git shortlog -s -n', 'git log --graph', 'git log', 'git rev-list --count --all' <-- used in project ). I tried to use os.system, but chose  subprocesses(It's more interesting) 
    - Statistic of commit count is avaible for all repos and branches 

How to run: python3 + console_tree.py(for cheking all folder system) + chosen directory name(for checking one chosen directory)