f = open("report_url.txt", "w+")

prefix = "report_"
report_ext = [
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".png", ".png", ".png", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".gif"
    ]

report_vid_ext = [
    ".mp4",
]

for idx in range(len(report_ext)):
    temp_str = prefix+str(idx+1)+report_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("poster_url.txt", "w+")
prefix = "poster_"
poster_ext= [
        ".jpg", ".jpg", ".jpeg", ".jpg", ".jpg", 
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg"
    ]
poster_vid_ext = [
    ".mp4",
]
for idx in range(len(poster_ext)):
    temp_str = prefix+str(idx+1)+poster_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("paper_url.txt", "w+")
prefix = "paper_"
paper_ext = [
        ".png", ".jpeg", ".JPG", ".JPG", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".png", ".png", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg"
    ]
for idx in range(len(paper_ext)):
    temp_str = prefix+str(idx+1)+paper_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("hard_url.txt", "w+")
prefix = "hard_"
hard_ext = [
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", 
        ".jpg", ".jpg", ".jpg", ".JPG", ".jpg",
        ".jpg", ".jpg", ".jpg"
    ]
for idx in range(len(hard_ext)):
    temp_str = prefix+str(idx+1)+hard_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("drawing_url.txt", "w+")
prefix = "drawing_"
drawing_ext = [
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", 
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".png", ".jpg", ".jpg", ".jpg", ".jpg", ".mp4",
    ]
for idx in range(len(drawing_ext)):
    temp_str = prefix+str(idx+1)+drawing_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("spring_url.txt", "w+")
prefix = "spring_binding_"
spring_ext = [
        ".jpg", ".jpg", ".PNG", ".PNG", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".mp4", ".mp4", ".mp4"
    ]
for idx in range(len(spring_ext)):
    temp_str = prefix+str(idx+1)+spring_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("binder_url.txt", "w+")
prefix = "binder_"
binder_ext = [
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg"
    ]
for idx in range(len(binder_ext)):
    temp_str = prefix+str(idx+1)+binder_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("index_url.txt", "w+")
prefix = "index_"
index_ext = [
        ".jpg", ".jpg", ".jpg"
    ]
for idx in range(len(index_ext)):
    temp_str = prefix+str(idx+1)+index_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("catalog_url.txt", "w+")
prefix = "catalog_"
catalog_ext = [
        ".jpg", ".jpeg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".jpg"
    ]
for idx in range(len(catalog_ext)):
    temp_str = prefix+str(idx+1)+catalog_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("invite_url.txt", "w+")
prefix = "invite_"
invite_ext = [
        ".jpg", ".png", ".jpg", ".png", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".png", ".jpg", ".jpg", ".jpg", ".png", ".jpg"
    ]
for idx in range(len(invite_ext)):
    temp_str = prefix+str(idx+1)+invite_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()


f = open("prize_url.txt", "w+")
prefix = "prize_"
prize_ext = [
        ".jpg",".jpg",".jpg",".jpg",".jpg",".jpg",".jpg",".jpg",".jpg",".jpg",
        ".jpg", ".jpg", ".jpg", ".jpg", ".mp4", ".mp4"
    ]
prize_vid_ext = [ ".mp4" , ".mp4 "]
for idx in range(len(prize_ext)):
    temp_str = prefix+str(idx+1)+prize_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()


f = open("print_url.txt", "w+")
prefix = "print_"
print_ext = [
    ".jpg"
    ]
print_vid_ext = [ ".mp4"]
for idx in range(len(print_ext)):
    temp_str = prefix+str(idx+1)+print_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("memorial_url.txt", "w+")
prefix = "memorial_"
memorial_ext = [
        ".jpg"
    ]
for idx in range(len(memorial_ext)):
    temp_str = prefix+str(idx+1)+memorial_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()


f = open("postit_url.txt", "w+")
prefix = "postit_"
postit_ext = [
        ".jpg"
    ]
for idx in range(len(postit_ext)):
    temp_str = prefix+str(idx+1)+postit_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("sticker_url.txt", "w+")
prefix = "sticker_"
sticker_ext = [
    ".JPG", ".JPG", ".JPG", ".JPG", ".JPG", ".JPG",
    ".JPG", ".JPG", ".JPG", ".JPG"
]
for idx in range(len(sticker_ext)):
    temp_str = prefix+str(idx+1)+sticker_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("general_url.txt", "w+")
prefix = "general_binding_"
general_ext = [
    ".jpg", ".JPG", ".jpg", ".jpg", ".jpg",
    ".jpg", ".jpg", ".jpg", ".png"
]
for idx in range(len(general_ext)):
    temp_str = prefix+str(idx+1)+general_ext[idx]+"\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("formboard_url.txt", "w+")
prefix = "formboard_"
formboard_ext = [
    ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
]
for idx in range(len(formboard_ext)):
    temp_str = prefix + str(idx+1) + formboard_ext[idx] + "\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("exhibit_url.txt", "w+")
prefix = "exhibit_"
exhibit_ext = [
    ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
    ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
    ".jpg", ".jpg", ".jpg", ".jpg", ".jpg",
    ".jpg", ".jpg"
]
for idx in range(len(exhibit_ext)):
    temp_str = prefix + str(idx+1) + exhibit_ext[idx] + "\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("envelope_url.txt", "w+")
prefix = "envelope_"
envelope_ext = [
    ".jpg", ".jpg", ".jpg", ".jpg",
]
for idx in range(len(envelope_ext)):
    temp_str = prefix + str(idx+1) + envelope_ext[idx] + "\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("namecard_url.txt", "w+")
prefix = "namecard_"
namecard_ext = [
    ".jpg", ".jpg", ".jpg", ".jpg",
]
for idx in range(len(namecard_ext)):
    temp_str = prefix + str(idx+1) + namecard_ext[idx] + "\n"
    f.write(temp_str)
    print(temp_str)
f.close()


f = open("bigcoating_url.txt", "w+")
prefix = "bigcoating_"
bigcoating_ext = [
    ".jpg"
]
for idx in range(len(bigcoating_ext)):
    temp_str = prefix + str(idx+1) + bigcoating_ext[idx] + "\n"
    f.write(temp_str)
    print(temp_str)
f.close()

f = open("shoppingbag_url.txt", "w+")
prefix = "shoppingbag_"
shoppingbag_ext = [
    ".jpg", ".jpg"
]
for idx in range(len(shoppingbag_ext)):
    temp_str = prefix + str(idx+1) + shoppingbag_ext[idx] + "\n"
    f.write(temp_str)
    print(temp_str)
f.close()

