import os
import fitz
import datetime
from tkinter import PhotoImage

# Miner -------------------------------------------------------------

def pdf_is_encrypted(file):
	pdf = fitz.Document(file)
	return pdf.isEncrypted

class Miner:
	def __init__(self, filepath, password=None):
		self.filepath = filepath
		self.filename = os.path.basename(self.filepath)
		self.pdf = fitz.open(filepath)
		if password is not None:
			self.pdf.authenticate(password)

	def read_pdf(self):
		metadata = self.pdf.metadata
		numPages = self.pdf.pageCount
		toc = self.pdf.getToC()
		
		page = self.pdf.loadPage(0)
		pagesize = page.MediaBoxSize

		return metadata, numPages, toc, tuple(pagesize)

	def get_page(self, page_num, zoom=None):
		page = self.pdf.loadPage(page_num)
		if zoom:
			mat = fitz.Matrix(zoom, zoom)
			pix = page.getPixmap(matrix=mat)
