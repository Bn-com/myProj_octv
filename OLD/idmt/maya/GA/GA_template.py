# -*- coding: utf-8 -*-

'''
Created on 2017-8-9

@author:韩虹

改自CG365
'''
import maya.cmds as mc

class templateWindow(object):
    """A base class for an options window"""

    @classmethod
    def showUI(cls):
        """A function to instantiate the options window"""
        win = cls()
        win.create()
        return win

    def __init__(self):
        """Initialize common data attributes"""
        self.uiContent = {'window': 'ar_optionsWindow',
         'title': 'Options Window',
         'size': (546, 350),
         'supportsToolAction': False,
         'commonButton': False,
         'commonButtonName': 'Apply'}

    def create(self):
        """Draw the window"""
        if mc.window(self.uiContent['window'], exists=True):
            mc.deleteUI(self.uiContent['window'], window=True)
        self.uiContent['window'] = mc.window(self.uiContent['window'], title=self.uiContent['title'], menuBar=True)
        self.uiContent['mainForm'] = mc.formLayout(nd=100, parent=self.uiContent['window'])
        self.commonMenu()
        self.uiContent['optionsBorder'] = mc.tabLayout(parent=self.uiContent['mainForm'], tabsVisible=False, childResizable=True)
        self.uiContent['optionsForm'] = mc.formLayout(nd=100, parent=self.uiContent['optionsBorder'])
        self.displayOptions()
        if self.uiContent['commonButton']:
            self.commonButtons()
            mc.formLayout(self.uiContent['mainForm'], e=True, attachForm=([self.uiContent['optionsBorder'], 'top', 0], [self.uiContent['optionsBorder'], 'left', 2], [self.uiContent['optionsBorder'], 'right', 2]), attachControl=([self.uiContent['optionsBorder'],
              'bottom',
              5,
              self.uiContent['actionBtn']],))
        else:
            mc.formLayout(self.uiContent['mainForm'], e=True, attachForm=([self.uiContent['optionsBorder'], 'top', 0],
             [self.uiContent['optionsBorder'], 'left', 2],
             [self.uiContent['optionsBorder'], 'right', 2],
             [self.uiContent['optionsBorder'], 'bottom', 0]))
        mc.showWindow()

    def doIt(self, *args):
        pass

    def commonMenu(self):
        """Create common menu items for all option boxes"""
        self.uiContent['editMenu'] = mc.menu(label='Edit')
        self.uiContent['editMenuSave'] = mc.menuItem(label='Save Settings', command=self.editMenuSaveCmd)
        self.uiContent['editMenuReset'] = mc.menuItem(label='Reset Settings', command=self.editMenuResetCmd)
        self.uiContent['editMenuDiv'] = mc.menuItem(d=True)
        self.uiContent['editMenuRadio'] = mc.radioMenuItemCollection()
        self.uiContent['editMenuTool'] = mc.menuItem(label='As Tool', radioButton=True, enable=self.uiContent['supportsToolAction'], command=self.editMenuToolCmd)
        self.uiContent['editMenuAction'] = mc.menuItem(label='As Action', radioButton=True, enable=self.uiContent['supportsToolAction'], command=self.editMenuActionCmd)
        self.uiContent['helpMenu'] = mc.menu(label='Help')
        self.uiContent['helpMenuItem'] = mc.menuItem(label='Help on %s' % self.uiContent['title'], command=self.helpMenuCmd)

    def helpMenuCmd(self, *args):
        """Override this method to display custom help"""
        win = mc.window(title='About', widthHeight=(400, 250), sizeable=False, minimizeButton=True, maximizeButton=False)
        mf = mc.formLayout(nd=100)
        tl = mc.tabLayout(tabsVisible=False, childResizable=True)
        mc.rowLayout(adj=True, nc=3, columnWidth3=(20, 150, 200), adjustableColumn=3, columnAlign=(1, 'left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
        mc.text(label='')
        mc.image(image='gCore.png')
        mc.columnLayout(adj=True)
        mc.text(align='left', label='Version: G-Core Beta 1.0\n')
        mc.text(align='left', label='Contact: ')
        mc.text(align='left', label='  Mail: 33266162@qq.com')
        mc.text(align='left', label='  Phone: (086) 136-9300-4459')
        mc.formLayout(nd=100)
        mc.formLayout(mf, e=True, attachForm=([tl, 'top', 0],
         [tl, 'left', 2],
         [tl, 'right', 2],
         [tl, 'bottom', 0]))
        mc.showWindow(win)

    def editMenuSaveCmd(self, *args):
        """Override this method to implement Save Settings"""
        pass

    def editMenuResetCmd(self, *args):
        """Override this method to implement Reset Settings"""
        pass

    def editMenuToolCmd(self, *args):
        """Override this method to implement tool mode"""
        pass

    def editMenuActionCmd(self, *args):
        """Override this method to implement action mode"""
        pass

    def actionBtnCmd(self, *args):
        """Apply actions and close window"""
        self.applyBtnCmd()
        self.closeBtnCmd()

    def applyBtnCmd(self, *args):
        """Override this method to apply actions"""
        self.doIt()

    def closeBtnCmd(self, *args):
        """Close window"""
        mc.deleteUI(self.uiContent['window'], window=True)

    def commonButtons(self):
        """Create common buttons for all option boxes"""
        self.uiContent['commonBtnSize'] = ((self.uiContent['size'][0] - 18) / 3, 26)
        self.uiContent['actionBtn'] = mc.button(parent=self.uiContent['mainForm'], label='%s and Close' % self.uiContent['commonButtonName'], height=self.uiContent['commonBtnSize'][1], command=self.actionBtnCmd)
        self.uiContent['applyBtn'] = mc.button(parent=self.uiContent['mainForm'], label=self.uiContent['commonButtonName'], height=self.uiContent['commonBtnSize'][1], command=self.applyBtnCmd)
        self.uiContent['closeBtn'] = mc.button(parent=self.uiContent['mainForm'], label='Close', height=self.uiContent['commonBtnSize'][1], command=self.closeBtnCmd)
        mc.formLayout(self.uiContent['mainForm'], e=True, attachForm=([self.uiContent['actionBtn'], 'left', 5],
         [self.uiContent['actionBtn'], 'bottom', 5],
         [self.uiContent['applyBtn'], 'bottom', 5],
         [self.uiContent['closeBtn'], 'bottom', 5],
         [self.uiContent['closeBtn'], 'right', 5]), attachPosition=([self.uiContent['actionBtn'],
          'right',
          1,
          33], [self.uiContent['closeBtn'],
          'left',
          0,
          67]), attachControl=([self.uiContent['applyBtn'],
          'left',
          4,
          self.uiContent['actionBtn']], [self.uiContent['applyBtn'],
          'right',
          4,
          self.uiContent['closeBtn']]), attachNone=([self.uiContent['actionBtn'], 'top'], [self.uiContent['applyBtn'], 'top'], [self.uiContent['closeBtn'], 'top']))

    def displayOptions(self):
        """Override this method to display options controls"""
        pass


if __name__ == '__main__':
    templateWindow().create()
