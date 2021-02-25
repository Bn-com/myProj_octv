__author__ = 'zhangben'

#Collect Files Menu Node
collectMenu = nuke.menu("Nodes").addMenu("Collect_Files")
collectMenu.addCommand('Collect Files', 'collectFiles.collectFiles()')
collectMenu.addCommand('Help', 'collectFiles.myBlog()')