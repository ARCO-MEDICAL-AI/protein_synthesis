import json
import random

# Create a class to handle proteins with an amino acid chain
class MonomericProteins:
    # Read the dictionaries containing the genetic information of codons necessary for protein synthesis
    def __init__(self):
        with open('C:\\Users\\Lenovo\\Desktop\\Sintese proteica\\Monomeric proteins dict.json') as file:
            # Note: Pay attention to Pyr in TRH, create an exception because it is not a codon.
            self.geneticinfo_monoproteins = json.load(file)
            # Create a list with the keys of the dictionary self.geneticinfo_monoproteins
            self.protein_keynames = list(self.geneticinfo_monoproteins.keys())

        with open("C:\\Users\\Lenovo\\Desktop\\Sintese proteica\\Codons_Aminoacidos.json") as file2:
            self.codons_code = json.load(file2)

    # Create a function that provides a metabolic demand that requires the protein (consider having its own class)
    def metabolic_demand(self):
        # Select a random protein from the list of protein names
        protein_needed = random.choice(self.protein_keynames)
        print(protein_needed)
        protein_aminoacids_code = self.geneticinfo_monoproteins.get(protein_needed)
        # List with the amino acids necessary for the demanded protein
        print(protein_aminoacids_code)
        # Return the amino acids that form the protein
        return protein_aminoacids_code

    # Create a function that gives the codons that form each of these amino acids, including the stop codon.
    # This sequence should be a list with the amino acids
    def create_codon_string(self, sequence):
        codon_string = ''
        for aminoacid in sequence:
            # Select a random value from a dictionary key
            codon = random.choice(self.codons_code.get(aminoacid))
            codon_string += codon
        
        stop = random.choice((self.codons_code.get('Stop')))
        print(stop)
        codon_string += stop

        return codon_string

    

# Test the class
mp = MonomericProteins()

# Give one protein to be synthesized  e its aminoacids
test_protein = mp.metabolic_demand()


# Create a variable to show the codon sequence nedeed to synthesize the given protein 
test_codon_string = mp.create_codon_string(test_protein)
print(test_codon_string)
