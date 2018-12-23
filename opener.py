import sys
import os
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Opener(QObject):
	project = ""
	seq = ""
	shot = ""
	task = ""
	filename = ""
	root = "/project"
	def __init__(self, ui_file, parents=None):
		ui_file = QFile(ui_file)
		ui_file.open(QFile.ReadOnly)
		loader = QUiLoader()
		self.window = loader.load(ui_file)
		ui_file.close()

		self.projectList = self.window.findChild(QListWidget,"projectList")
		# btn.accepted.connect(self.accepted_handler)
		# btn.rejected.connect(self.rejected_handler)
		self.initProject()
		self.window.show()
		# event
		self.projectList.itemClicked.connect(self.projectClick)
	
	def initProject(self):
		projects = os.listdir(self.root)
		self.projectList.addItems(projects)

	def projectClick(self, project):
		self.project = project.text()
		print project.text()

	def accepted_handler(self):
		print("accepted")

	def rejected_handler(self):
		print("rejected")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = Opener("opener.ui")
	sys.exit(app.exec_())
