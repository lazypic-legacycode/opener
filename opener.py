#coding:utf8
import sys
import os
import subprocess
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Opener(QObject):
	root = "/project"
	project = ""
	middle = "shot"
	seq = ""
	shot = ""
	task = ""
	filename = ""
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
		self.taskList.itemClicked.connect(self.taskClick)
		self.fileList.itemClicked.connect(self.fileClick)
		self.fileList.itemDoubleClicked.connect(self.fileDoubleClick)
	
	def initProject(self):
		projects = os.listdir(self.root)
		projects.reverse()
		self.projectList.addItems(projects)

	def projectClick(self, item):
		self.seqList.clear()
		self.shotList.clear()
		self.taskList.clear()
		self.fileList.clear()
		self.project = str(item.text())
		seqPath = "/".join([self.root, self.project, self.middle])
		if not os.path.exists(seqPath):
			self.seqList.clear()
			self.shotList.clear()
			self.taskList.clear()
			self.fileList.clear()
			return
		seqList = os.listdir(seqPath)
		seqList.reverse()
		self.seqList.addItems(seqList)

	def seqClick(self, item):
		self.shotList.clear()
		self.taskList.clear()
		self.fileList.clear()
		self.seq = str(item.text())
		shotPath = "/".join([self.root, self.project, self.middle, self.seq])
		if not os.path.exists(shotPath):
			self.shotList.clear()
			self.taskList.clear()
			self.fileList.clear()
			return
		shotList = os.listdir(shotPath)
		shotList.reverse()
		self.shotList.addItems(shotList)

	def shotClick(self, item):
		self.taskList.clear()
		self.fileList.clear()
		self.shot = str(item.text())
		taskPath = "/".join([self.root, self.project, self.middle, self.seq, self.shot])
		if not os.path.exists(taskPath):
			self.taskList.clear()
			self.fileList.clear()
			return
		taskList = os.listdir(taskPath)
		taskList.reverse()
		self.taskList.addItems(taskList)

	def taskClick(self, item):
		self.fileList.clear()
		self.task = str(item.text())
		filePath = "/".join([self.root, self.project, self.middle, self.seq, self.shot, self.task])
		if not os.path.exists(filePath):
			self.fileList.clear()
			return
		fileList = os.listdir(filePath)
		fileList.reverse()
		self.fileList.addItems(fileList)

	def fileClick(self, item):
		self.filename = str(item.text())
	
	def fileDoubleClick(self, item):
		self.filename = str(item.text())
		filePath = "/".join([self.root, self.project, self.middle, self.seq, self.shot, self.task, self.filename])
		if os.path.isdir(filePath):
			subprocess.Popen(["open",filePath], stdout=subprocess.PIPE)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = Opener("opener.ui")
	sys.exit(app.exec_())
