import os

fin = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/59.txt"), "r")
fout = open("output.txt", 'w')

crypted_sentence = []

while True:
  line = fin.readline()
  if not line: break

  crypted_ascii = [int(a) for a in line.split(',')]

# ord, chr

# ascii_to_sentence(key, asciis)
def decrypt_ascii_to_sentence(key, asciis):
  sentence = ''
  decrypted_asciis = []
  for idx,asc in enumerate(asciis):
    k = key[idx%3]
    decrypted_asc = asc^ord(k)
    
    #if not(decrypted_asc == ord('=') or decrypted_asc == ord('*') or decrypted_asc == ord('/') or decrypted_asc == ord('+') or decrypted_asc == ord('-') or decrypted_asc == ord(')') or decrypted_asc == ord('(') or decrypted_asc == ord('.') or decrypted_asc == ord(' ') or decrypted_asc == ord(',') or decrypted_asc == ord('!') or decrypted_asc in range(ord('a'), ord('z')+1) or decrypted_asc in range(ord('A'), ord('Z')+1) or decrypted_asc in range(ord('0'), ord('9')+1)):
    #  return False
    
    if decrypted_asc == ord('/') or decrypted_asc == ord('#') or decrypted_asc == ord('+') or decrypted_asc == ord('|') or decrypted_asc == ord('>') or decrypted_asc == ord('<') or decrypted_asc == ord('~'):
      return False

    sentence += chr(decrypted_asc)
    decrypted_asciis.append(decrypted_asc)

  return (sentence, decrypted_asciis)


for i in range(ord('a'), ord('z')+1):
  for j in range(ord('a'), ord('z')+1):
    for k in range(ord('a'), ord('z')+1):
      key = chr(i) + chr(j) + chr(k)
      decrypt = decrypt_ascii_to_sentence(key, crypted_ascii)
      if decrypt:
        fout.write('########## sentence ##########\n')
        fout.write(decrypt[0])
        fout.write('\n')
        fout.write('## key ##\n')
        fout.write(key)
        fout.write('\n')
        fout.write('## sum ##\n')
        fout.write(str(sum(decrypt[1])))
        fout.write('\n')


fin.close()
fout.close()
#print decrypt_ascii_to_sentence('abc', crypted_ascii)