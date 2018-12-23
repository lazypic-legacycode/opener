#coding:utf8
import sys
import os
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Opener(QObject):
	root = "/project"
	currentProject = ""
	middle = "shot"
	currentSeq = ""
	currentShot = ""
	currentTask = ""
	currentFilename = ""
	def __init__(self, ui_file, parents=None):
		ui_file = QFile(ui_file)
		ui_file.open(QFile.ReadOnly)
		loader = QUiLoader()
		self.window = loader.load(ui_file)
		ui_file.close()

		self.projectList = self.window.findChild(QListWidget,"projectList")
		self.seqList = self.window.findChild(QListWidget,"seqList")
		self.shotList = self.window.findChild(QListWidget,"shotList")
		self.taskList = self.window.findChild(QListWidget,"taskList")
		self.fileList = self.window.findChild(QListWidget,"fileList")
		self.initProject()
		self.window.show()
		# event
		self.projectList.itemClicked.connect(self.projectClick)
		self.seqList.itemClicked.connect(self.seqClick)
		self.shotList.itemClicked.connect(self.shotClick)
		#self.taskList.itemClicked.connect(self.taskClick)
	
	def initProject(self):
		projects = os.listdir(self.root)
		projects.reverse()
		self.projectList.addItems(projects)

	def projectClick(self, project):
		self.seqList.clear()
		self.currentProject = str(project.text())
		seqPath = "/".join([self.root, self.currentProject, self.middle])
		if not os.path.exists(seqPath):
			print("%s 경로가 존재하지 않습니다." % (seqPath))
			return
		seqList = os.listdir(seqPath)
		seqList.reverse()
		self.seqList.addItems(seqList)

	def seqClick(self, seq):
		self.shotList.clear()
		self.currentSeq = str(seq.text())
		shotPath = "/".join([self.root, self.currentProject, self.middle, self.currentSeq])
		if not os.path.exists(shotPath):
			print("%s 경로가 존재하지 않습니다." % (shotPath))
			return
		shotList = os.listdir(shotPath)
		shotList.reverse()
		self.shotList.addItems(shotList)

	def shotClick(self, shot):
		self.taskList.clear()
		self.currentShot = str(shot.text())
		taskPath = "/".join([self.root, self.currentProject, self.middle, self.currentSeq, self.currentShot])
		if not os.path.exists(taskPath):
			print("%s 경로가 존재하지 않습니다." % (taskPath))
			return
		taskList = os.listdir(taskPath)
		taskList.reverse()
		self.taskList.addItems(taskList)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = Opener("opener.ui")
	sys.exit(app.exec_())
