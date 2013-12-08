PDBParser
=========
Written: Connor Fourt

Updated: December 8th 2013

Use? Yes. MIT License

###TL;DR: PDB in, XYZ out for some atoms in a protein.###

Purpose: PDBParser is a quick python scrpt to take in a Protein Database file
      and several parameters and output their positional data in an xyz file. 

*The parameters are the atom number within the molecule

*XYZ file is for use in [Psi4][dl]
[dl]: http://www.psicode.org


Syntax: python pdbparser.py ~/Location/inputFile.pdb PARAMETER1 PARAMETER2

*Replace Location with location of PDB file

*Parameters can only be positional such as "344" for "ATOM 344" in PDB format

Output: A xyz file compatible with Psi 4. The filename is editable within the 
      the script. The comments line will show all arguments for that file.

