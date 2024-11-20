with open("traffic.in") as read:
	num_miles = int(read.readline())

	segment_type = []
	start = []
	end = []

	for m in range(num_miles):
		curr_type, s, e = read.readline().split()
		segment_type.append(curr_type)
		start.append(int(s))
		end.append(int(e))

low = 0
high = float("inf")

for m in range(num_miles - 1, -1, -1):
	if segment_type[m] == "none":
		# Set a new range based on sensor reading.
		low = max(low, start[m])
		high = min(high, end[m])
	elif segment_type[m] == "off":
		# Update range of possible traffic flows
		low += start[m]
		high += end[m]
	elif segment_type[m] == "on":
		low -= end[m]
		high -= start[m]
		# Set to zero if low becomes negative
		low = max(0, low)

write = open("traffic.out", "w")
print(low, high, file=write)

low = 0
high = float("inf")

# Process again, this time scanning the other way
for m in range(num_miles):
	if segment_type[m] == "none":
		low = max(low, start[m])
		high = min(high, end[m])
	elif segment_type[m] == "on":
		low += start[m]
		high += end[m]
	elif segment_type[m] == "off":
		low -= end[m]
		high -= start[m]
		low = max(0, low)

print(low, high, file=write)