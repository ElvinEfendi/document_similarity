from dataset import *
from rabin import *

def parse_shingles(document, q):
  shingles = []
  for i in range(q, len(document) + 1):
    shingles.append(document[(i-q):i])

  return shingles

# binary document-shingle matrix
def generate_M(q):
  # <shingle fingerprint>: [<doc ids that include this shingle>]
  dictionary = {}
  # collection fingerprinted shingles
  for i in range(len(documents)):
    shingles = parse_shingles(documents[i], q)
    for shingle in shingles:
      fingerprint = fingerprint_of(shingle)
      if dictionary.has_key(fingerprint):
        dictionary[fingerprint] = np.append(dictionary[fingerprint], i)
      else:
        dictionary[fingerprint] = np.array([i])
  
  # generate the matrix
  print "================", len(dictionary)
  M = np.zeros((len(dictionary), len(documents)), dtype=int)
  i = 0
  for fingerprint in dictionary.keys():
    for j in dictionary[fingerprint]:
      M[i, j] = 1
    i += 1
  
  return M

# generate sketch matrix
def generate_Ms(q, number_of_permutations, M):
  Ms = np.zeros((number_of_permutations, M.shape[1]), dtype=int)
  permutation = np.array(range(M.shape[0]))

  for i in range(number_of_permutations):
    random.shuffle(permutation)
    for j in range(M.shape[1]):
      idx_with_one = np.where(M[:, j]==1)[0]
      Ms[i, j] = permutation[idx_with_one].min()

  return Ms
