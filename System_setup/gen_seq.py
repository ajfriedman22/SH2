from modeller import *
import argparse

#Create the parser
parser = argparse.ArgumentParser()

#Input argument for PDB file
parser = argparse.ArgumentParser(description = 'Generate a Modeller Sequence File from a PDB Input')
parser.add_argument('-i', type=str, required=True, help = 'Name of PDB input file')

#Import Arguments
args = parser.parse_args()
code = args.i

#Write to an alignment file
e = Environ()
m = Model(e, file=code)
aln = Alignment(e)
aln.append_model(m, align_codes=code)
aln.write(file=code+'.seq')
