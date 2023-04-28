---@diagnostic disable: lowercase-global, undefined-global, undefined-field


function cumalativeAverage(length) --can also be used as moving average
	b = {}
	a = {}
	for i=1,length do
		b[i] = 1/length
		a[i] = 0
	end
	return b,a
end