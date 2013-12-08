PDBParser
=========
Written: Connor Fourt
Updated: December 8th 2013

!!TL;DR: PDB in, XYZ out for some atoms in a protein.

This is a simple script in python that reads in a PDB (Protein Database) file and outputs the positional data of specific atoms within a protein.


Purpose: To parse a PDB file for any number of parameters and output into a xyz file

Syntax: python pdbparser.py ~/Location/inputFile.pdb PARAMETER1 PARAMETER2
    *Replace Location with location of PDB file
    *Parameters can only be positional such as "344" for "ATOM 344" in PDB format

Output: A xyz file compatible with Psi 4. The filename is editable within the 
      the script. The comments line will show all arguments for that file.

