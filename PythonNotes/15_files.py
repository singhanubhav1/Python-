# #f = open("data.txt", "r") #read file
# with open("data.txt") as f:

# # open("data.txt", "w") #write file


# # print(f.readline())
# # print(f.readline())


# # for line in f:
# #     print(line)


# print(f.read(15))
# print(f.read(18))




# with open("Data_folder/data.txt", "r") as f:
#     f.write("Anubhav")



import qrcode as qr
img = qr.make("https://drive.usercontent.google.com/u/0/uc?id=1m-O06dJO8m998ga8CBgOhh4FcSaQPuj1&export=download")


img.save("Soft Skill Development.jpg")