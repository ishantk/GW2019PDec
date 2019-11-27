# Multi Value Container

# Single Value
instagramUserName = "auribises"
profilePic = "auribisesLogo.png"

# Multi Value - tuple
# READ-ONLY | IMMUTABLE

# myAlbum = "pic1.jpg", "pic2.jpg", "pic3.png"
# yourAlbum = "pic1.jpg", "pic2.jpg", "pic3.png", "video1.mp4"
# userData = "john", 20, "john@example.com", 4.5, "Redwood Shores"

myAlbum = ("pic1.jpg", "pic2.jpg", "pic3.png")
yourAlbum = ("pic1.jpg", "pic2.jpg", "pic3.png", "video1.mp4")
userData = ("john", 20, "john@example.com", 4.5, "Redwood Shores")

print("instagramUserName is: ", instagramUserName, "and type is:", type(instagramUserName))
print("profilePic is: ", profilePic, "and type is:", type(profilePic))
print("myAlbum is: ", myAlbum, "and type is:", type(myAlbum))
print("yourAlbum is: ", yourAlbum, "and type is:", type(yourAlbum))
print("userData is: ", userData, "and type is:", type(userData))

print("============")

# Multi Value - list
# READ-WRITE | MUTABLE

myAlbum = ["pic1.jpg", "pic2.jpg", "pic3.png"]
yourAlbum = ["pic1.jpg", "pic2.jpg", "pic3.png", "video1.mp4"]
userData = ["john", 20, "john@example.com", 4.5, "Redwood Shores"]

print("myAlbum is: ", myAlbum, "and type is:", type(myAlbum))
print("yourAlbum is: ", yourAlbum, "and type is:", type(yourAlbum))
print("userData is: ", userData, "and type is:", type(userData))






