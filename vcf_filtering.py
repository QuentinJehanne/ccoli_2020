import sys

if(len(sys.argv) < 4):
	print("ERROR\t\tArguments number incorrect\nERROR\t\tCorrect cmd: python3 file.py inputVCF outputVCF max_represented_genotype")
	print("\nEXAMPLE\t\tpython3 file.py snps.vcf snps_filtered.vcf 300")
	exit()

else:
	inputFile		= sys.argv[1]
	outputFile		= sys.argv[2]
	nMaxGen			= int(sys.argv[3])

	f = open(inputFile, "r")
	f2 = open(outputFile, "w")

	line = f.readline()
	while("##" in line):
		f2.write(line)
		line = f.readline()

	elems = line.split("\t")

	line = f.readline()

	while(line != ""):
		line2 = line.replace("\n", "")
		elems = line2.split("\t")

		i = 9
		Genotypes = {}

		while(i < len(elems)):
			gt = "-1"
			if("./." not in elems[i]):
				val = elems[i].split(":")[1]
				gts = val.split(",")
				for j in range(len(gts)):						
					if(gts[j] == "0"):
						gt = str(j)
			try:
				val = Genotypes[gt]
				val += 1
				Genotypes[gt] = val

			except:
				Genotypes[gt] = 1

			i += 1
			
		validation = True

		for k,v in Genotypes.items():
			if(v > nMaxGen):
				validation = False

		if(validation):
			f2.write(line)

		line = f.readline()

	f2.close()	
	f.close()
