from Rating_data import *

Board=[["r","k","b","q","a","b","k","r" ],
		["p","p","p","p","p","p","p","p" ],
		[" "," "," "," "," "," "," "," " ],
		[" "," "," "," "," "," "," "," " ],
		[" "," "," "," "," "," "," "," " ],
		[" "," "," "," "," "," "," "," " ],
		["P","P","P","P","P","P","P","P" ],
		["R","K","B","Q","A","B","K","R" ]]

Board1=[["r","k","b","q","a","b","k","r" ],
		["p","p","p","p","p","p","p","p" ],
		[" "," "," "," "," "," "," "," " ],
		[" "," "," "," "," "," "," "," " ],
		[" "," "," "," "," "," "," "," " ],
		[" "," "," "," "," "," "," "," " ],
		["P","P","P","P","P","P","P","P" ],
		["R","K","B","Q","A","B","K","R" ]]

class chess:
	def show(self):
		for i in range(9):
			if i ==0:
				print(" ",end=" ")
			else:
				print(i-1,end=" ")
		print()
		for i in range(8):
			for j in range(9):
				if j==0:
					print(i,end=" ")
				else:
					print(Board[i][j-1],end=" ")
			print()

	def makemove(self,ans):
		for i in range(64):
			if Board[i%8][i//8]=="A":
				kingC=i		
		if ans[4]!="P":
			Board[int(ans[2])][int(ans[3])]=Board[int(ans[0])][int(ans[1])]
			Board[int(ans[0])][int(ans[1])]=" "
			if "A"==Board[int(ans[2])][int(ans[3])]:
				kingC=int(ans[2])*8+int(ans[3])
		else:
			Board[1][int(ans[0])]=" "
			Board[0][int(ans[1])]=int(ans[2])

	def finalmove(self,ans):
		for i in range(64):
			if Board1[i%8][i//8]=="A":
				kingC=i		
		if ans[4]!="P":
			Board1[int(ans[2])][int(ans[3])]=Board1[int(ans[0])][int(ans[1])]
			Board1[int(ans[0])][int(ans[1])]=" "
			if "A"==Board1[int(ans[2])][int(ans[3])]:
				kingC=int(ans[2])*8+int(ans[3])
		else:
			Board1[1][int(ans[0])]=" "
			Board1[0][int(ans[1])]=int(ans[2])

		for i in range(64):
			Board[i%8][i//8]=Board1[i%8][i//8]

	def undomove(self,ans):
		#print("i was called")
		for i in range(64):
			if Board[i%8][i//8]=="A":
				kingC=i			
		if ans[4]!="P":
			Board[int(ans[0])][int(ans[1])]=Board[int(ans[2])][int(ans[3])]
			Board[int(ans[2])][int(ans[3])]=" "
			if "A"==Board[int(ans[0])][int(ans[1])]:
				kingC=int(ans[0])*8+int(ans[1])
		else:
			Board[1][int(ans[0])]="P"
			Board[0][int(ans[1])]=int(ans[3])

	def possibleA(self,i):
		ans=""
		r = i % 8
		c = i // 8
		kingC=i
		for j in range(9):
			try:
				if j != 4:
					if ((r - 1 + j // 3) < 0 or (c - 1 + j % 3) < 0):
						raise NameError()
					if (Board[r-1+j//3][c-1+j%3] == " " or Board[r - 1 + j // 3][c-1+j%3].islower()):
						oldpiece = Board[r - 1 + j // 3][c - 1 + j % 3]	
						Board[r][c] = " "
						Board[r - 1 + j // 3][c - 1 + j % 3] = "A"
						kingtemp = kingC
						kingC = i + (j // 3) * 8 + (j % 3) * 8 - 9
						if self.kingsafe() == True:
							ans = ans + str(r) + str(c) + str((r - 1 + j // 3)) + str((c - 1 + j % 3)) + oldpiece
						Board[r][c] = "A"
						Board[r - 1 + j // 3][c - 1 + j % 3] = oldpiece
						kingC = kingtemp
			except:
				pass
		return ans	

	def kingsafe(self):
		for i in range(64):
			if Board[i%8][i//8]=="A":
				kingC=i
		#bishop+queen
		r=kingC%8
		c=kingC//8
		temp=1
		for j in range(-1,2,2):
			for k in range(-1,2,2):
				try:
					while Board[r+temp*j][c+temp*k]==" ":
						temp=temp+1

					if Board[r+temp*j][c+temp*k]=="b" or Board[r+temp*j][c+temp*k]=="q" :
						return False
				except:
					pass
				temp=1
					
		#rook+queen
		for j in range(-1,2,2):
			try:			
				while Board[r][c+temp*j]==" " and r+temp*j>=0 and r+temp*j<8:
					temp=temp+1
				#print(Board[r+temp*j][c],r+temp*j,c)
				if Board[r][c+temp*j]=="r" or Board[r][c+temp*j]=="q":
					return False
			except:
				pass
			temp=1
			try:
				while Board[r+temp*j][c]==" " and c+temp*j>=0 and c+temp*j<8:
					temp=temp+1
				if Board[r+temp*j][c]=="r" or Board[r+temp*j][c]=="q":
					return False
			except:
				pass
			temp=1
		#knight
		for i in range(-1,2,2):
			for j in range(-1,2,2):
				try:
					if Board[r+i][c+j*2]=="k":
						return False
				except:
					pass
				try:
					if Board[r+i*2][c+j]=="k":
						return False
				except:
					pass
		#pawn	
		if kingC>=16:
			try:
				if Board[r -1][c-1]=="p":
					return False
			except:
				pass
			try:
				if Board[r-1][c-1]=="p":
					return False
			except:
				pass
		#king
		for i in (-1,2):
			for j in (-1,2):
				if(i!=0 or j!=0):
					try:
						if Board[r+i][c+j]=="a":
							return False
					except:
						pass
		return True

	def possibleQ(self,i):
		ans=""
		r=i%8
		c=i//8
		temp=1
		for j in range(-1,2):
			for k in range(-1,2):
				try:
					while Board[r+temp*j][c+temp*k]==" ":
						#print(r+temp*j,c+temp*k)
						oldpiece=Board[r+temp*j][c+temp*k]
						Board[r][c]=" "
						Board[r+temp*j][c+temp*k]="Q"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:						
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking
						Board[r][c]="Q"
						Board[r+temp*j][c+temp*k]=oldpiece
						temp=temp+1

					if Board[r+temp*j][c+temp*k].islower():
						oldpiece=Board[r+temp*j][c+temp*k]
						Board[r][c]=" "
						Board[r+temp*j][c+temp*k]="Q"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:						
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking  
						Board[r][c]="Q"
						Board[r+temp*j][c+temp*k]=oldpiece
					temp=1
				except:
					pass
		return ans

	def possibleB(self,i):
		ans=""
		r=i%8
		c=i//8
		temp=1
		for j in range(-1,2,2):
			for k in range(-1,2,2):
				try:
					#print("here",Board[r+temp*j][c+temp*k])
					while Board[r+temp*j][c+temp*k]==" ":
						#print("here")
						oldpiece=Board[r+temp*j][c+temp*k]
						Board[r][c]=" "
						Board[r+temp*j][c+temp*k]="B"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking
						Board[r][c]="B"
						Board[r+temp*j][c+temp*k]=oldpiece
						temp=temp+1

					if Board[r+temp*j][c+temp*k].islower():
						oldpiece=Board[r+temp*j][c+temp*k]
						Board[r][c]=" "
						Board[r+temp*j][c+temp*k]="B"
						if r+temp*j>=0 and c+temp*k>=0:
							if self.kingsafe()==True:
								ans=ans+str(r)+str(c)+str(r+temp*j)+str(c+temp*k)+oldpiece
						#backtracking  
						Board[r][c]="B"
						Board[r+temp*j][c+temp*k]=oldpiece
					temp=1
				except:
					pass
		return ans

	def possibleR(self,i):
		ans=""
		r=i%8
		c=i//8
		temp=1
		for j in range(-1,2):
			try:	
				while Board[r+temp*j][c]==" ":
					oldpiece=Board[r+temp*j][c]
					Board[r][c]=" "
					Board[r+temp*j][c]="R"
					if r+temp*j>=0:
						if self.kingsafe()==True:				
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c)+oldpiece
					#backtracking
					Board[r][c]="R"
					Board[r+temp*j][c]=oldpiece
					temp=temp+1


				if Board[r+temp*j][c].islower():
					oldpiece=Board[r+temp*j][c]
					Board[r][c]=" "
					Board[r+temp*j][c]="R"
					if r+temp*j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r+temp*j)+str(c)+oldpiece
					#backtracking
					Board[r][c]="R"
					Board[r+temp*j][c]=oldpiece

				temp=1


				while Board[r][c+temp*j]==" ":
					oldpiece=Board[r][c+temp*j]
					Board[r][c]=" "
					Board[r][c+temp*j]="R"
					if c+temp*j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r)+str(c+temp*j)+oldpiece
					#backtracking
					Board[r][c]="R"
					Board[r][c+temp*j]=oldpiece
					temp=temp+1


				if Board[r][c+temp*j].islower():
					oldpiece=Board[r][c+temp*j]
					Board[r][c]=" "
					Board[r][c+temp*j]="R"
					if c+temp*j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r)+str(c+temp*j)+oldpiece
					#backtracking
					Board[r][c]="R"
					Board[r][c+temp*j]=oldpiece
				temp=1
			except:
				pass

		return ans

	def possibleK(self,i):
		ans=""
		r=i%8
		c=i//8	
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if (Board[r + j][c+ k*2]==" " or Board[r+j][c+k*2].islower()) :
						oldpiece=Board[r+j][c+k*2]
						Board[r][c]=" "
						Board[r+j][c+k*2]="K"
						if self.kingsafe()==True:
							if r+j>=0 and c +k*2>=0:
								ans=ans+str(r)+str(c)+str(r+j)+str(c+k*2)+oldpiece
						Board[r][c]="K"
						Board[r+j][c+k*2]=oldpiece
				except:
					pass
				k=k+2
			j=j+2
	
		j=-1
		while j<2:
			k=-1
			while k<2:
				try:
					if (Board[r+2*j][c+ k]==" " or Board[r+j*2][c+k].islower()) :
						oldpiece=Board[r+j*2][c+k]
						Board[r][c]=" "
						Board[r+j*2][c+k]="K"
						if self.kingsafe()==True:
							if r+j*2>=0 and c +k>=0:											
								ans=ans+str(r)+str(c)+str(r+j*2)+str(c+k)+oldpiece
						Board[r][c]="K"
						Board[r+j*2][c+k]=oldpiece
				except:
					pass
				k=k+2
			j=j+2
		return ans

	def possibleP(self,i):
		#print(i)
		ans=""
		r=i%8
		c=i//8
		for j in range(-1,2,2):
			try:
				if Board[r-1][c+j].islower() and i%8<2:
					oldpiece=Board[r-1][c+j]
					Board[r][c]=" "
					Board[r-1][c+j]="P"
					if r-1>=0 and c+j>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r-1)+str(c+j)+oldpiece
					#backtracking
					Board[r][c]="P"
					Board[r-1][c+j]=oldpiece

				"""if Board[r-1][c+j].islower() and i<16:
					temp=["Q","R","B","K"]
					for k in range(0,4):
						oldpiece=Board[r-1][c+j]
						Board[r][c]=" "
						Board[r-1][c+j]=temp[k]
						if r-1>=0 and c+j>=0:
							if self.kingsafe()==True:
							#column1,column2,captured-pice,new-piece,P
								ans=ans+str(c)+str(c+j)+oldpiece+temp[k]+"P"
						#backtracking
						Board[r][c]="P"
						Board[r-1][c+j]=oldpiece"""
			except:
				pass

		try:
			if Board[r-1][c]==" " and i%8>=2:
					oldpiece=Board[r-1][c]
					Board[r][c]=" "
					Board[r-1][c]="P"
					if r-1>=0 and c>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r-1)+str(c)+oldpiece
					#backtracking
					Board[r][c]="P"
					Board[r-1][c]=oldpiece
		
			"""if Board[r-1][c]==" " and i<16:
					temp=["Q","R","B","K"]
					for k in range(0,4):
						oldpiece=Board[r-1][c]
						Board[r][c]=" "
						Board[r-1][c]=temp[k]
						if r-1>=0 and c+j>=0:
							if self.kingsafe()==True:
						#column1,column2,captured-pice,new-piece,P
								ans=ans+str(c)+str(c)+oldpiece+temp[k]+"P"
						#backtracking
						Board[r][c]="P"
						Board[r-1][c]=oldpiece"""

			if Board[r-2][c]==" " and Board[r-1][c]==" " and i%8>=6:
					oldpiece=Board[r-2][c]
					Board[r][c]=" "
					Board[r-2][c]="P"
					if r-2>=0 and c>=0:
						if self.kingsafe()==True:
							ans=ans+str(r)+str(c)+str(r-2)+str(c)+oldpiece
					#backtracking
					Board[r][c]="P"
					Board[r-2][c]=oldpiece

		except:
			pass
		return ans

	def moves(self):
		ans=""
		for i in range(64):
			if Board[i%8][i//8]=='P':
				ans+=self.possibleP(i)
			if Board[i%8][i//8]=='R':
				ans+=self.possibleR(i)
			elif Board[i%8][i//8]=='B':
				ans+=self.possibleB(i)
			elif Board[i%8][i//8]=='K':
				ans+=self.possibleK(i)
			elif Board[i%8][i//8]=='A':
				ans+=self.possibleA(i)
			elif Board[i%8][i//8]=='Q':
				ans+=self.possibleQ(i)
		return ans

	def alphabeta(self,depth,beta,aplha,move,player):
		r=Rating()
		ans=self.moves()
		if depth==0 or len(ans)==0:
			print(r.rating(len(ans),depth)*(player*2 -1 ))
			return move+str(r.rating(len(ans),depth)*(player*2 -1 ))
		#ans=self.sortmove(ans)		
		player=1-player #either 1 or 0
		for i in range(0,len(ans),5):
			self.makemove(ans[i:i+5])
			self.flipboard()
			rtnstr=self.alphabeta(depth-1,beta,aplha,ans[i:i+5],player)
			val=float(rtnstr[5:])
			val=int(val)
			self.flipboard()
			self.undomove(ans[i:i+5])
			#self.show()
			if player==0:
				if val<=beta:
					beta=val
					if depth==4:
						move=rtnstr[0:5]
			else:
				if val>aplha:
					aplha=val
					if depth==4:
						move=rtnstr[0:5]
			if aplha>=beta:
				if player==0:
					return move+str(beta)
				else:
					return move +str(aplha)

		if player==0:
			return move + str(beta) 
		else:
			return move + str(aplha)

	def flipboard(self):
		for i in range(32):
			r=i%8
			c=i//8
			if Board[r][c].isupper()==True:
				temp=Board[r][c].lower()
			else:
				temp=Board[r][c].upper()
			if Board[7-r][7-c].isupper()==True:
				Board[r][c]=Board[7-r][7-c].lower()
			else:
				Board[r][c]=Board[7-r][7-c].upper()
			Board[7-r][7-c]=temp

def main():
	print("Hello ! Welcome to alphabeta chess simulator")
	print("Here is a sample of Board")
	a=chess()
	a.show()
	print("Enter the moves in form of 1234b")
	while True:
		t=input("enter move ")
		a.makemove(t)
		a.finalmove(t)
		print("Your move")
		a.show()
		ans=a.alphabeta(4,1000000,-1000000,"",0)
		print("Computer's move")
		a.makemove(ans)
		a.finalmove(ans)
		a.show()

if __name__ == '__main__':
		main()	