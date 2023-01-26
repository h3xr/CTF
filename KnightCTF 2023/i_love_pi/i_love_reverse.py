import base64

# lengths = [--REDACTED--]
# len(lengths) = 10
# len(flag) = 39

lengths = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
flag = "KCTF{*******************************}" # Flag is not 39 it is 37. Need to add some "*"
print("Flag should be 39 ->", len(flag))
flag = "KCTF{*********************************}"
print("Flag should be 39 ->", len(flag))

flag_list = []
s = 0
encoded_flag = ""
for l in lengths:
    seg = flag[s:s+l]
    for _ in range(len(seg)):
        seg = base64.b64encode(seg.encode('ascii')).decode('ascii')
    s+=l
    flag_list.append(seg)  # List of encoded seg
    encoded_flag += seg

flag_to_decode = "VXpCT1ZRPT0=Rg==V2xod1UxcHNWa0pRVkRBOQ==MQ==VmpCb2QxVXhjSE5UYTFaV1ZrUkJPUT09Vm0wd2QyVkhVWGhUV0doaFUwVndVRlp0TVZOV01XeFZVbTVrVlUxV2NIbFdNalZyVmpKS1NHVkliRmRpVkVaSVZtMTRTMk15VGtWUmJIQk9VakF4TkZkWGRHRmtNRFZ5VFZWV2FHVnFRVGs9U0RNPQ==Vm1wQ1UxRXlTbkpOVldSVFYwZFNjVlJVU1RSUFVUMDk=VjFSS2QxWXhjSEpPVldSYVpXcEJPUT09VGtac09RPT0="

# We need to put in our flag_list encoded CORRECT flag, divided by element
s1 = 0
for i, j in enumerate(flag_list):
    len_j = len(j)
    flag_list[i] = flag_to_decode[s1: s1 + len_j]
    s1 += len_j

print("Encoded flag divided by element:", flag_list)  # Printing the list
print("-" * 10)

# Decoding
i_ = 0
decoded_list = []
for el in flag_list:
    for _ in range(0, lengths[i_]):
        dec = base64.b64decode(el.encode('ascii')).decode('ascii')
        el = dec
    decoded_list.append(el)
    i_ += 1

print("Decoded List:", decoded_list)
print("-" * 10)
flag = "".join(decoded_list)
print(flag)

# len(lengths) = 10
print("len(lengths) should be = 10 ->", len(lengths))
# len(flag) = 39
print("len(flag) should be 39 ->", len(flag))