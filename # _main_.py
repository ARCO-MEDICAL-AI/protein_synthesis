# _main_

from ferramentas import *
# Test the class
mp = MonomericProteins()

# Give one protein to be synthesized  e its aminoacids
test_protein = mp.metabolic_demand()


# Create a variable to show the codon sequence nedeed to synthesize the given protein 
test_codon_string = mp.create_codon_string(test_protein)
print(test_codon_string)