from preprocessing import *

NUMBER_OF_FUNCTIONS = 100
Q = [2] #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def jaccard():
  for q in Q:
    print ""
    print "q = ", q
    M = generate_M(q)
    idx_of_ones_on_first_column = np.where(M[:, 0]==1)[0]
    
    Ms = generate_Ms(q, NUMBER_OF_FUNCTIONS, M)
    first_ms_column = Ms[:, 0]

    for j in range(1, M.shape[1]):
      # for M
      intersection_size = np.where(M[:, j][idx_of_ones_on_first_column] == 1)[0].size
      union_size = idx_of_ones_on_first_column.size + np.where(M[:, j]==1)[0].size - intersection_size
      jaccard_M = intersection_size * 1.0 / union_size

      # for Ms
      count = 0.0
      next_column = Ms[:, j]
      for i in range(Ms.shape[0]):
        if first_ms_column[i] == next_column[i]:
	  count += 1.0
      jaccard_Ms = count / NUMBER_OF_FUNCTIONS

      print "Similarity between D_1 and D_" + str(j+1) + ": is ", jaccard_M, " using M and ", jaccard_Ms, " using Ms"

if __name__ == "__main__":
  jaccard()
