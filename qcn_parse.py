# QCN open source editor
# This will allow you to replace the IMEI in any QCN file with whatever you want
# I have no idea how ot find IMEI2? but i assume its a string as well
# If you can make this better? Please shoot a pull request
# By: John Hale (john.b.hale@gmail.com)

replacer = True #to toggle the replace thing on and off
def imiefy(foundhex):
  hexlist = foundhex
  hexlist = hexlist.replace(" ", "") #cleanup
  newhexlist = "" #variable for the result
  for index in range(0, len(hexlist), 2): #loops from index 0 and increments by 2
    newhexlist = newhexlist+(hexlist[index+1])+hexlist[index] #flips the current index and the index after
  return newhexlist[-15:] #only last 15 digits
def abomination(wantedimei):
  hexlist = "80A"+wantedimei
  hexlist = hexlist.replace(" ", "") #cleanup
  newhexlist = "" #variable for the result
  for index in range(0, len(hexlist), 2): #loops from index 0 and increments by 2
    newhexlist = newhexlist+(hexlist[index+1])+hexlist[index] #flips the current index and the index after
  return newhexlist #the new stuff to write
with open("test.qcn", "rb") as f:
    # read the file content as bytes
    data = f.read()
    # convert the hex string to bytes
    hex_bytes = bytes.fromhex("8800010026020000") # NEVER CHANGE THIS OR YOU WILL BREAK YOUR QCN FILE - YOU HAVE BEEN WARNED
    # find the index of the hex bytes in the file
    index = data.find(hex_bytes)
    # check if the hex bytes are found
    if index != -1:
        # get the next 9 bytes after the hex bytes
        next_bytes = data[index + len(hex_bytes) : index + len(hex_bytes) + 9] # This is the IMEI in the file in NVRAM HEX
        if replacer:
          newdata = data.replace(data[index + len(hex_bytes) : index + len(hex_bytes) + 9], bytearray.fromhex(abomination(input('new imei:')))) # WHEN IT PROMPTS YOU, ENTER THE IMEI NORMALLY AS YOU WOULD SEE IT ON A PHONE
          with open('result.qcn', 'wb') as res: # THIS IS A NEW FILE SO WE DONT MESS UP THE ORIG
            res.write(newdata)
            print("replaced")
        # convert the next bytes to hex string
        next_hex = next_bytes.hex()
        # print the output
        print("imei:", imiefy(next_hex))
    else:
        # print an error message if the hex bytes are not found
        print("The hex bytes are not found in the file.")
