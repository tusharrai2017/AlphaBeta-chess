from chess_game import *
class Rating:
	def __init__(self,lent,depth):
		self.counter=0
		self.c=chess()
		self.len=lent
		self.depth=depth
		self.pawnBoard=[[ 0,  0,  0,  0,  0,  0,  0,  0],
						[50, 50, 50, 50, 50, 50, 50, 50],
						[10, 10, 20, 30, 30, 20, 10, 10],
						[ 5,  5, 10, 25, 25, 10,  5,  5],
						[ 0,  0,  0, 20, 20,  0,  0,  0],
						[ 5, -5,-10,  0,  0,-10, -5,  5],
						[ 5, 10, 10,-20,-20, 10, 10,  5],
						[ 0,  0,  0,  0,  0,  0,  0,  0]]

		self.rookBoard=[[ 0,  0,  0,  0,  0,  0,  0,  0],
						[ 5, 10, 10, 10, 10, 10, 10,  5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[-5,  0,  0,  0,  0,  0,  0, -5],
						[ 0,  0,  0,  5,  5,  0,  0,  0]]

		self.knightBoard= [[-50,-40,-30,-30,-30,-30,-40,-50],
						   [-40,-20,  0,  0,  0,  0,-20,-40],
						   [-30,  0, 10, 15, 15, 10,  0,-30],
						   [-30,  5, 15, 20, 20, 15,  5,-30],
						   [-30,  0, 15, 20, 20, 15,  0,-30],
						   [-30,  5, 10, 15, 15, 10,  5,-30],
						   [-40,-20,  0,  5,  5,  0,-20,-40],
						   [-50,-40,-30,-30,-30,-30,-40,-50]]

		self.bishopBoard=[[-20,-10,-10,-10,-10,-10,-10,-20],
						  [-10,  0,  0,  0,  0,  0,  0,-10],
						  [-10,  0,  5, 10, 10,  5,  0,-10],
						  [-10,  5,  5, 10, 10,  5,  5,-10],
						  [-10,  0, 10, 10, 10, 10,  0,-10],
						  [-10, 10, 10, 10, 10, 10, 10,-10],
						  [-10,  5,  0,  0,  0,  0,  5,-10],
						  [-20,-10,-10,-10,-10,-10,-10,-20]]

		self.queenBoard=[[-20,-10,-10, -5, -5,-10,-10,-20],
						 [-10,  0,  0,  0,  0,  0,  0,-10],
						 [-10,  0,  5,  5,  5,  5,  0,-10],
						 [ -5,  0,  5,  5,  5,  5,  0, -5],
						 [  0,  0,  5,  5,  5,  5,  0, -5],
						 [-10,  5,  5,  5,  5,  5,  0,-10],
						 [-10,  0,  5,  0,  0,  0,  0,-10],
						 [-20,-10,-10, -5, -5,-10,-10,-20]]

		self.kingMidBoard=[[-30,-40,-40,-50,-50,-40,-40,-30],
						   [-30,-40,-40,-50,-50,-40,-40,-30],
						   [-30,-40,-40,-50,-50,-40,-40,-30],
						   [-30,-40,-40,-50,-50,-40,-40,-30],
						   [-20,-30,-30,-40,-40,-30,-30,-20],
						   [-10,-20,-20,-20,-20,-20,-20,-10],
						   [ 20, 20,  0,  0,  0,  0, 20, 20],
						   [ 20, 30, 10,  0,  0, 10, 30, 20]]

		self.kingEndBoard=[[-50,-40,-30,-20,-20,-30,-40,-50],
						   [-30,-20,-10,  0,  0,-10,-20,-30],
						   [-30,-10, 20, 30, 30, 20,-10,-30],
						   [-30,-10, 30, 40, 40, 30,-10,-30],
						   [-30,-10, 30, 40, 40, 30,-10,-30],
						   [-30,-10, 20, 30, 30, 20,-10,-30],
						   [-30,-30,  0,  0,  0,  0,-30,-30],
						   [-50,-30,-30,-30,-30,-30,-30,-50]]

	def rateAttack(self):
		count=0
		for i in range(64):
			r=i%8
			c=i//8
			if Board[r][c]=='P':
				self.p.kingC=i
				if self.c.kingsafe()==False:
					count=count-64
			elif Board[r][c]=='R':
				self.p.kingC=i
				kc=kingsafe(self.p,self.p.kingC)
				if kc.test()==False:
					count=count-500
			elif Board[r][c]=='K':
				self.p.kingC=i
				kc=kingsafe(self.p,self.p.kingC)
				if kc.test()==False:
					count=count-300
			elif Board[r][c]=='B':
				self.p.kingC=i
				kc=kingsafe(self.p,self.p.kingC)
				if kc.test()==False:
					count=count-300
			elif Board[r][c]=='Q':
				self.p.kingC=i
				kc=kingsafe(self.p,self.p.kingC)
				if kc.test()==False:
					count=count-900
		self.p.kingC=temp
		kc=kingsafe(self.p,self.p.kingC)
		if kc.test()==False:
			count=count-200
		return count//2

	def rateMaterial(self):
		count=0
		biscount=0
		for i in range(64):
			if Board[i//8][i%8]=='P':
				count=count+100
			elif Board[i//8][i%8]=='R':
				count=count+500
			elif Board[i//8][i%8]=='K':
				count=count+300
			elif Board[i//8][i%8]=='B':
				biscount=biscount+1
			elif Board[i//8][i%8]=='Q':
				count=count+900
		if biscount==2:
			count=count+600
		elif biscount==1:
			count=count+250
		return count

	def rateMoveability(self,lent,depth,material):
		count=0
		count=count+lent
		if lent==0:
			kc=kingsafe(self.p,self.p.kingC)
			if kc.test()==False:
				count=count+(-200000)*depth
			else:
				count=count+(-150000)*depth
		return count

	def ratePosition(self,material):
		count=0
		for i in range(64):
			r=i//8
			c=i%8
			if Board[r][c]=='P':
				count=count+self.pawnBoard[r][c]
			if Board[r][c]=='R':
				count=count+self.rookBoard[r][c]
			if Board[r][c]=='B':
				count=count+self.bishopBoard[r][c]
			if Board[r][c]=='K':
				count=count+self.knightBoard[r][c]
			if Board[r][c]=='Q':
				count=count+self.queenBoard[r][c]
			if Board[r][c]=='A':
				if material>=1750:
					count=count+self.kingMidBoard[r][c]
					self.pA=scratch(self.p.kingC)
					count=count+len(self.pA.calcmove())*10		
				else:
					count=count+self.kingEndBoard[r][c]
					self.pA=possibleA(self.p.kingC)
					count=count+len(self.pA.calcmove())*30					

		return count

	def checking(self):
		material=self.rateMaterial()
		self.counter=self.counter+self.rateAttack()
		self.counter=self.counter+self.rateMaterial()
		self.counter=self.counter+self.rateMoveability(self.len,self.depth,material)
		self.counter=self.counter+self.ratePosition(material)
		self.c.flipboard()
		self.counter=self.counter-self.rateAttack()
		self.counter=self.counter-self.rateMaterial()
		self.counter=self.counter-self.rateMoveability(self.len,self.depth,material)
		self.counter=self.counter-self.ratePosition(material)
		self.c.flipboard()
		return -(self.counter+self.depth*50)