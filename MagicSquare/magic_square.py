class MagicSquare:
	"""Crea un cuadrado magico con el numero de filas que le pidas ! """
	square = []
	possible = []
	totalSqs = 0
	adds = 0
	numsquares = 0

	def __init__(self, thenum):
		self.n = thenum
		self.totalSqs = self.n * self.n
		self.adds = self.n*((self.n*self.n)+1)/2
		self.square = [[0 for x in xrange(self.n)] for x in xrange(self.n)]
		#everything is possible at first
		for i in xrange(self.totalSqs):
			self.possible.append(True)

		print "La suma magica es ", self.adds, " y tiene un total de", self.totalSqs, " numeros que acomodar. "
		print ' '
		self.fill(0,0)
		print 'El total de cuadrados magicos posibles de ',self.n,'x',self.n,'es',self.numsquares

	def  fill(self, row, col):

		if self.checkRows() == False or self.checkCols() == False or self.checkDiags() == False:
			return
			
		if row == self.n:
			#print self.square
			for row in self.square:
				print row
			print ' '
			self.numsquares = self.numsquares+1
			return

		for i in xrange(self.totalSqs):
			if self.possible[i] == True:
				self.square[row][col]= i+1
				self.possible[i]= False
				newcol= col+1
				newrow = row
				if newcol == self.n:
					newrow = newrow+1
					newcol = 0
				self.fill(newrow,newcol)
				self.square[row][col] = 0
				self.possible[i]=True


	def checkRows(self):
		for i in xrange(self.n):
			test = 0
			unFilled = False
			for j in xrange(self.n):
				test= test+self.square[i][j]
				if self.square[i][j] == 0:
					unFilled = True
			if unFilled == False and test != self.adds:
				return False
		return True

	def checkCols(self):
		for i in xrange(self.n):
			test = 0
			unFilled = False
			for j in xrange(self.n):
				test= test+self.square[j][i]
				if self.square[j][i] == 0:
					unFilled = True
			if unFilled == False and test != self.adds:
				return False
		return True

	def checkDiags(self):
		diag1 = 0
		diag2 = 0
		k = self.n-1
		unFilled = False

		for i in xrange(self.n):
			diag1 = diag1 + self.square[i][i]
			diag2 = diag2 + self.square[i][k]
			if self.square[i][i] == 0 or self.square[i][k] == 0:
					unFilled = True
			k=k-1

		if (diag1 != self.adds and unFilled == False) or (diag2 != self.adds and unFilled == False):
			return False

		return True

# -----------------------------------------------------------------------

try:
    thenum=int(raw_input('Escribe el numero de filas que quieres que tenga el cuadro magico : '))
    magicsqr = MagicSquare(thenum)
except ValueError:
    print "Escribe un numero."