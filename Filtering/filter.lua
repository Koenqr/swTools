---@diagnostic disable: lowercase-global, undefined-global, undefined-field
--vscode bs


--sample generated data 6th order butterworth filter with cutoff 5Hz
b={0.00058481,0.00292404,0.00584809,0.00584809,0.00292404,0.00058481}
a={1,-3.31080756,4.58460628,-3.27498161,1.19916474,-0.17926796}

function createFilter(b,a)
	x={}
	y={}
	for i=1,#b do
		x[i]=0
	end
	for i=1,#a do
		y[i]=0
	end
	return {b=b,a=a,
		x=x,y=y,len=#b,
		run = function(self,var)
			local total=0
			table.remove(self.x)
			table.insert(self.x,1,var)
			for i=1,self.len do
				total = total + self.b[i]*self.x[i]
				total = total - self.a[i]*self.y[i]
			end
			table.remove(self.y)
			table.insert(self.y,1,total)
			return total
		end
	}
end



function createExponential(alpha)
	return {alpha=alpha,s=0,
		run = function(self,var)
			self.s = self.s + self.alpha*(var-self.s)
			return self.s
		end,
		set = function(self,var)
			self.s = var or 0
		end
	}
end

