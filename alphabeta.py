class alphabeta:
	def __init__(self,depth,beta,alpha,player):
		self.depth=depth
		self.alpha=alpha
		self.beta=beta
		self.player=player

	def logic(self):
		self.list="1"
		if self.depth==0 or len(self.list)==0:
			return str(self.Rating())
		self.list=""
		ree=int(input("how many moves "))	
		self.player=1-self.player 
		for i in range(ree):
			rtn=alphabeta(self.depth-1,self.beta,self.alpha,self.player)
			rtnstr=rtn.logic()
			val=int(rtnstr)
			if self.player==0:
				if val<=self.beta:
					self.beta=val
			else:
				if val>self.alpha:
					self.alpha=val
			if self.alpha>=self.beta:
				if self.player==0:
					return str(self.beta)
				else:
					return str(self.alpha)

		if self.player==0:
			return str(self.beta) 
		else:
			return str(self.alpha)


	def Rating(self):
		return int(input("enter score "))

def main():
	print("hey this is alphabeta pruning tree  ")
	ab=alphabeta(4, 1000000, -1000000, 0)
	t=ab.logic()
	print("the best number is",t)

if __name__ == '__main__':
	main()