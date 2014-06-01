import numpy as np

def binary_to_decimal(arr):
  return int(''.join(str(e) for e in arr), 2)

def fingerprint_of(data):
  """ return Rabin's fingerprint - coefficients of remainder
  input string
  output fingerprint in decimal representation
  """
  # irreducible polinomial chosen uniformly at random
  # (1)*X^16+(1)*X^15+(1)*X^14+(1)*X^13+(1)*X^7+(1)*X^6+(1)*X^4+(1)*X^3+(1)
  irreducible_poly = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1])

  # respective polinomial for the binary representation of given data
  binary_str = ''.join(format(i,'b').zfill(8) for i in bytearray(data))
  data_poly = np.array(list(binary_str), dtype=int)
 
  # normalize irreducible_poly
  padding = data_poly.size - irreducible_poly.size
  if padding < 0:
    # the length of nominator is less than the length denominator
    return binary_to_decimal(data_poly)
  else:
    irreducible_poly = np.concatenate([np.zeros(data_poly.size - irreducible_poly.size, dtype=int), irreducible_poly])

  while True:
    tmp = irreducible_poly.copy()
    ones_in_data_poly = np.where(data_poly==1)[0]
    if ones_in_data_poly.size == 0:
      break

    shift = np.where(irreducible_poly==1)[0][0] - ones_in_data_poly[0]

    if shift < 0:
      break
    else:
      for i in range(shift):
	tmp = np.delete(tmp, 0)
        tmp = np.append(tmp, 0)
      data_poly = np.bitwise_xor(data_poly, tmp)

  return binary_to_decimal(data_poly)
