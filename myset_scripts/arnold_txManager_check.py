class MtoATxManager(object):

    use = None
    def __init__(self):
        MtoATxManager.use = A
        path = os.path.dirname(os.path.abspath(__file__))
        uiFile = os.path.join(path, 'txManager.myuis');
        window = '';
        txItems = []  # arrays [texture_name, status, colorSpace, nodeList, inputFiles]
        # where status is:
        #   -1 (does not exists),
        #    0 (.tx file),
        #    1 (has a processed .tx file),
        #    2 (does not have a processed .tx file)
        listElements = []
        selectedItems = []
        filesToCreate = 0

        filesCreated = 0
        createdErrors = 0
        deletedFiles = 0

        thread = []
        process = True
        lineIndex = {}

    def create(self):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window);
        window = cmds.loadUI(uiFile=uiFile, verbose=False)

        cmds.showWindow(window);
        try:
            initPos = cmds.windowPref(window, query=True, topLeftCorner=True)
            if initPos[0] < 0:
                initPos[0] = 0
            if initPos[1] < 0:
                initPos[1] = 0
            cmds.windowPref(window, edit=True, topLeftCorner=initPos)
        except:
            pass

        ctrlPath = '|'.join([window, 'radioButton']);
        cmds.radioButton(ctrlPath, edit=True, select=True);

        ctrlPath = '|'.join([window, 'groupBox_4']);
        cmds.control(ctrlPath, edit=True, enable=False);

        ctrlPath = '|'.join([window, 'groupBox_2', 'pushButton_7']);
        cmds.button(ctrlPath, edit=True, enable=False);

        ctrlPath = '|'.join([window, 'groupBox_2', 'lineEdit']);
        cmds.textField(ctrlPath, edit=True, text="-v -u --unpremult --oiio");

# Update the Scroll List with the texture files in the scene and check its status
def updateList():
    txItems = []

    texturesList = []
    colorSpaces = []
    nodes = []

    list = cmds.ls(type='file')
    for node in list:
        texture = cmds.getAttr(node + '.fileTextureName')
        if texture:
            texturesList.append(texture)
            colorSpace = cmds.getAttr(node + '.colorSpace')
            colorSpaces.append(colorSpace)
            nodes.append(node)

    list = cmds.ls(type='aiImage')
    for node in list:
        texture = cmds.getAttr(node + '.filename')
        if texture:
            texturesList.append(texture)
            colorSpace = cmds.getAttr(node + '.colorSpace')
            colorSpaces.append(colorSpace)
            nodes.append(node)

    list = cmds.ls(type='imagePlane')
    for node in list:
        texture = cmds.getAttr(node + '.imageName')
        if texture:
            texturesList.append(texture)
            colorSpace = cmds.getAttr(node + '.colorSpace')
            colorSpaces.append(colorSpace)
            nodes.append(node)

    totalFiles = 0
    missingFiles = 0

    textureSearchPaths = cmds.getAttr('defaultArnoldRenderOptions.texture_searchpath')
    searchPaths = []

    if platform.system().lower() == 'windows':
        searchPaths = textureSearchPaths.split(';')
    else:
        searchPaths = textureSearchPaths.split(':')

    for i in range(len(texturesList)):

        inputFiles = makeTx.expandFilename(texturesList[i])

        if len(inputFiles) == 0:
            # file not found, need to search in the Texture Search Paths
            for searchPath in searchPaths:
                if searchPath.endswith('/'):
                    currentSearchTexture = searchPath + texturesList[i]
                else:
                    currentSearchTexture = searchPath + '/' + texturesList[i]

                inputFiles = makeTx.expandFilename(currentSearchTexture)
                if len(inputFiles) > 0:
                    break

        totalFiles += len(inputFiles)

        txFlag = 0

        if len(inputFiles) == 0:
            # missing input file
            txFlag = -1
            missingFiles += 1
        else:
            ext = os.path.splitext(texturesList[i])[1]
            # A .tx texture
            if (ext == '.tx'):
                txFlag = 0
            else:
                # Not a .tx texture
                # loop over files since we need to make sure each expanded texture has its .tx version
                txFlag = 1
                for inputFile in inputFiles:
                    # note that inputFile is already expanded here
                    outputTx = os.path.splitext(inputFile)[0] + '.tx'
                    outputTxFiles = makeTx.expandFilename(outputTx)

                    if len(outputTxFiles) == 0:
                        # un-processed File
                        txFlag = 2
                        break

        # set textures element as a list : [filename, txFlag, textureColorSpace, node]
        nodesList = [nodes[i]]
        txItems.append([texturesList[i], txFlag, colorSpaces[i], nodesList, inputFiles])

    ctrlPath = '|'.join([window, 'groupBox', 'listWidget']);

    listSize = cmds.textScrollList(ctrlPath, query=True, numberOfItems=True);
    for x in range(listSize, 0, -1):
        cmds.textScrollList(ctrlPath, edit=True, removeIndexedItem=x);

    textureIndex = 0
    lineIndex = {}

    for txItem in txItems:

        texturePrefix = ''

        if (txItem[1] == 0):
            texturePrefix = '[tx] '
        elif (txItem[1] == 1):
            texturePrefix = '(tx) '
        elif (txItem[1] == 2):
            texturePrefix = '       '
        elif (txItem[1] == -1):
            texturePrefix = '~~  '

        textureLine = texturePrefix + txItem[0]

        maya_version = versions.shortName()
        if int(float(maya_version)) >= 2017:
            textureLine += ' (' + txItem[2] + ')'

        if textureLine not in lineIndex:
            cmds.textScrollList(ctrlPath, edit=True, append=[textureLine]);
            lineIndex[textureLine] = textureIndex

            # textureIndex += 1
        else:
            prevIndex = lineIndex[textureLine]
            if prevIndex < len(txItems):
                txItems[prevIndex][3].append(txItem[3][0])
        # modify
        textureIndex += 1
    listElements = cmds.textScrollList(ctrlPath, query=True, ai=True);

    ctrlPath = '|'.join([window, 'groupBox', 'label_5']);
    cmds.text(ctrlPath, edit=True, label="Total Files: {0}".format(totalFiles));

    ctrlPath = '|'.join([window, 'groupBox', 'label_6']);
    if (missingFiles > 0):
        cmds.text(ctrlPath, edit=True, label="<font color=#FE6565>Missing Files: {0}</font>".format(missingFiles));
    else:
        cmds.text(ctrlPath, edit=True, label="");

def stopCreation( *args):
    process = False

# Updates the Scroll List and also the process progress message
# Only to be used when a refresh button is pressed, as it will remove any progress information shown
def refreshList( *args):
    updateList()

    # Only update this text when button is pressed, not when called from createTx or deleteTx
    updateProgressMessage(window, 0, 0, 0)
    ctrlPath = '|'.join([window, 'groupBox_3', 'label_10']);
    cmds.text(ctrlPath, edit=True, label="");

def selectAll( *args):
    updateList()
    if listElements:
        all_idx = [i + 1 for i, texture in enumerate(listElements) if
                   texture.startswith('       ') or texture.startswith('(tx) ')]
        ctrlPath = '|'.join([window, 'groupBox', 'listWidget']);
        cmds.textScrollList(ctrlPath, edit=True, deselectAll=True);
    cmds.textScrollList(ctrlPath, edit=True, selectIndexedItem=all_idx);

    selectedFilesFromList()

# Select all textures that does not have a processed .tx file
def selectNonTx( *args):
    updateList()
    if listElements:
        all_idx = [i + 1 for i, texture in enumerate(listElements) if texture.startswith('       ')]
        ctrlPath = '|'.join([window, 'groupBox', 'listWidget']);
        cmds.textScrollList(ctrlPath, edit=True, deselectAll=True);
        cmds.textScrollList(ctrlPath, edit=True, selectIndexedItem=all_idx);

        selectedFilesFromList()

def selectChange( *args):
    selectedFilesFromList()

def selectLine( *args):
    ctrlPath = '|'.join([window, 'groupBox', 'listWidget']);

    selectedList = cmds.textScrollList(ctrlPath, query=True, si=True);

    lineText = selectedList[0];
    lineIndex = lineIndex[lineText]

    if lineIndex >= len(txItems):
        return

    selectedItem = txItems[lineIndex]
    nodes = selectedItem[3]

    cmds.select(clear=True)

    print (selectedItem[0] + '(' + selectedItem[2] + ')')
    print 'Used by file node(s) : '

    for node in nodes:
        if node:
            print ('  ' + node)
            cmds.select(node, add=True)

# Set the variables selectedItems, filesToCreate, filesCreated and createdErrors
#  from the Scroll List selection
def selectedFilesFromList():

    ctrlPath = '|'.join([window, 'groupBox', 'listWidget']);
    selectedLines = cmds.textScrollList(ctrlPath, query=True, si=True);
    selectedLinesIdx = cmds.textScrollList(ctrlPath, query=True, sii=True);

    filesToCreate = 0
    filesCreated = 0
    createdErrors = 0
    selectedItems = []

    if not selectedLines:
        updateProgressMessage(window, 0, 0, 0)
        return

    list = cmds.textScrollList(ctrlPath, query=True, ai=True);
    lineIndex = 0

    for i in range(len(selectedLines)):
        lineText = selectedLines[i]

        # if python allows a better way to do this (find the index of this element), please get rid of this hash
        lineIndex = lineIndex[lineText]

        # all my information is in txItems[lineIndex]
        if lineIndex >= len(txItems):
            # shouldn't happen !
            continue

        selectedItems.append(txItems[lineIndex])
        texture = selectedItems[i][0]

        filesToCreate += len(selectedItems[i][4])

    updateProgressMessage(window, filesCreated, filesToCreate, 0)
    ctrlPath = '|'.join([window, 'groupBox_3', 'label_10']);
    cmds.text(ctrlPath, edit=True, label="");

# Set the variables selectedItems, filesToCreate, filesCreated and createdErrors
#  from the Folder selected
def selectedFilesFromFolder( *args):
    ctrlPath = '|'.join([window, 'groupBox_4', 'lineEdit_2']);
    folder = cmds.textField(ctrlPath, query=True, text=True);

    selectedItems = []

    filesToCreate = 0
    filesCreated = 0
    createdErrors = 0

    ctrlPath = '|'.join([window, 'groupBox_4', 'checkBox']);
    recursive = cmds.checkBox(ctrlPath, query=True, value=True);

    selectedItems = []
    if os.path.isdir(folder):
        if recursive:
            for root, dirs, files in os.walk(folder):
                for texture in files:
                    if (isImage(texture)):
                        # item = [os.path.join(root, texture), 0, '', '', [os.path.join(folder, texture)]]
                        item = [os.path.join(root, texture), 0, '', '', [os.path.join(root, texture)]]
                        selectedItems.append(item)
                        filesToCreate += 1
        else:
            files = os.listdir(folder)
            for texture in files:
                if (isImage(texture)):
                    item = [os.path.join(folder, texture), 0, '', '', [os.path.join(folder, texture)]]
                    selectedItems.append(item)
                    filesToCreate += 1

    updateProgressMessage(window, filesCreated, filesToCreate, 0)
    ctrlPath = '|'.join([window, 'groupBox_3', 'label_10']);
    cmds.text(ctrlPath, edit=True, label="");

# Open a dialog to select a folder and update the information about it
def selectFolder( *args):
    ctrlPath = '|'.join([window, 'groupBox_4', 'lineEdit_2']);
    folder = cmds.textField(ctrlPath, query=True, text=True);
    if not os.path.isdir(folder):
        folder = cmds.workspace(query=True, directory=True)
    ret = cmds.fileDialog2(cap='Select Folder', okc='Select', fm=2, startingDirectory=folder)
    if ret is not None and len(ret):
        ctrlPath = '|'.join([window, 'groupBox_4', 'lineEdit_2']);
        cmds.textField(ctrlPath, edit=True, text=ret[0]);
        selectedFilesFromFolder()

# Delete the processed .tx files selected
def deleteTx( *args):
    ctrlPath = '|'.join([window, 'radioButton']);
    selection = cmds.radioButton(ctrlPath, query=True, select=True);

    deletedFiles = 0
    ctrlPath = '|'.join([window, 'groupBox_3', 'label_10']);

    if selection:
        selectedFilesFromList()
    else:
        selectedFilesFromFolder()

    if not selectedItems:
        cmds.text(ctrlPath, edit=True, label="Deleted: {0}".format(deletedFiles));
        return

    for textureLine in selectedItems:
        texture = textureLine[0]
        if not texture:
            continue;

        # loop over the previously listed files
        for inputFile in textureLine[4]:
            txFile = os.path.splitext(inputFile)[0] + ".tx"
            if os.path.isfile(txFile):
                AiTextureInvalidate(txFile)
                os.remove(txFile)
                deletedFiles += 1

        cmds.text(ctrlPath, edit=True, label="Deleted: {0}".format(deletedFiles));
    updateList()

# Create the processed .tx files in another thread to avoid locking the UI
def createTx( *args):
if not thread:
thread = MakeTxThread()
thread.start()

def createTx(self):
if not self.txManager.selectedItems:
    return

ctrlPath = '|'.join([self.txManager.window, 'groupBox_2', 'pushButton_7'])
utils.executeDeferred(cmds.button, ctrlPath, edit=True, enable=True)

for textureLine in self.txManager.selectedItems:
    texture = textureLine[0]

    # we could use textureLine[2] for the colorSpace
    # but in case it hasn't been updated correctly
    # it's still better to ask maya again what is the color space
    nodes = textureLine[3]
    colorSpace = 'auto'
    conflictSpace = False
    for node in nodes:
        nodeColorSpace = cmds.getAttr(node + '.colorSpace')
        if colorSpace != 'auto' and colorSpace != nodeColorSpace:
            conflictSpace = True

        colorSpace = nodeColorSpace

    if not texture:
        continue
    # stopCreation has been called
    if not self.txManager.process:
        break

    # if a conflict is found, pop-up a dialog
    if conflictSpace:
        msg = os.path.basename(texture)
        msg += '\n'
        msg += 'has conflicting Color Spaces.\n'
        msg += 'Use ('
        msg += colorSpace
        msg += ') ?'

        result = cmds.confirmDialog(
            title='Conflicting Color Spaces',
            message=msg,
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel')

        if result == 'Cancel':
            break

    # Process all the files that were found previously for this texture (eventually multiple tokens)
    for inputFile in textureLine[4]:
        # here inputFile is already expanded, and only corresponds to existing files

        if not self.txManager.process:
            # stopCreation has been called
            break

        status = self.runMakeTx(inputFile, colorSpace)
        self.filesCreated += status[0]
        self.createdErrors += status[2]

        utils.executeDeferred(updateProgressMessage, self.txManager.window, self.filesCreated, self.txManager.filesToCreate, self.createdErrors)

ctrlPath = '|'.join([self.txManager.window, 'groupBox_2', 'pushButton_7'])
utils.executeDeferred(cmds.button, ctrlPath, edit=True, enable=False)
self.txManager.process = True
utils.executeDeferred(self.txManager.updateList)


def createTx(self):
if not self.txManager.selectedItems:
return

ctrlPath = '|'.join([self.txManager.window, 'groupBox_2', 'pushButton_7'])
utils.executeDeferred(cmds.button, ctrlPath, edit=True, enable=True)

for textureLine in self.txManager.selectedItems:
texture = textureLine[0]

# we could use textureLine[2] for the colorSpace
# but in case it hasn't been updated correctly
# it's still better to ask maya again what is the color space
nodes = textureLine[3]
colorSpace = 'auto'
conflictSpace = False
for node in nodes:
    nodeColorSpace = cmds.getAttr(node + '.colorSpace')
    if colorSpace != 'auto' and colorSpace != nodeColorSpace:
        conflictSpace = True

    colorSpace = nodeColorSpace

if not texture:
    continue
# stopCreation has been called
if not self.txManager.process:
    break

# if a conflict is found, pop-up a dialog
if conflictSpace:
    msg = os.path.basename(texture)
    msg += '\n'
    msg += 'has conflicting Color Spaces.\n'
    msg += 'Use ('
    msg += colorSpace
    msg += ') ?'

    result = cmds.confirmDialog(
        title='Conflicting Color Spaces',
        message=msg,
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if result == 'Cancel':
        break

# Process all the files that were found previously for this texture (eventually multiple tokens)
for inputFile in textureLine[4]:
    # here inputFile is already expanded, and only corresponds to existing files

    if not self.txManager.process:
        # stopCreation has been called
        break

    status = self.runMakeTx(inputFile, colorSpace)
    self.filesCreated += status[0]
    self.createdErrors += status[2]

    utils.executeDeferred(updateProgressMessage, self.txManager.window, self.filesCreated, self.txManager.filesToCreate, self.createdErrors)

ctrlPath = '|'.join([self.txManager.window, 'groupBox_2', 'pushButton_7'])
utils.executeDeferred(cmds.button, ctrlPath, edit=True, enable=False)
self.txManager.process = True
utils.executeDeferred(self.txManager.updateList)