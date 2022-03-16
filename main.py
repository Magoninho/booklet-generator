from turtle import back
from pdf2image import convert_from_path
from PIL import Image

def generate_back_pages(total_pages):
	result = []
	interactions = total_pages // 2

	back_first = total_pages
	back_second = 1

	# back
	for i in range(interactions, 0, -2):
		result.append([back_first, back_second])
		back_first -= 2
		back_second += 2

	return result

def generate_front_pages(total_pages):
	result = []
	interactions = total_pages // 2

	front_first = 2
	front_second = total_pages - 1

	# front
	for i in range(interactions, 0, -2):
		result.append([front_first, front_second])
		front_first += 2
		front_second -= 2
	
	return result


NUM_OF_PAGES = int(input("How many pages does your book has? "))
if (NUM_OF_PAGES % 2) != 0: 
	print("Must be an Even number of pages!")
	exit()

back_pages = generate_back_pages(NUM_OF_PAGES)
front_pages = generate_front_pages(NUM_OF_PAGES)


# extracting images from pdf
images = convert_from_path(str(input("File name: ")))

counter = 0
for img in images:
	counter += 1
	img.save(f'images/{counter}.jpg', 'JPEG')


page_counter = 0
back_image_list = []
front_image_list = []
# generating back pages
for b in range(len(back_pages)):
	page_counter += 1
	image1 = Image.open(f'images/{back_pages[b][0]}.jpg')
	image2 = Image.open(f'images/{back_pages[b][1]}.jpg')
	new_image = Image.new('RGB',(2*image1.size[0], image2.size[1]), (250,250,250))
	new_image.paste(image1,(0,0))
	new_image.paste(image2,(image1.size[0],0))
	new_image.save(f"images/merged_pages/back_pages/{page_counter}_{back_pages[b][0]}_{back_pages[b][1]}.jpg","JPEG")
	back_image_list.append(new_image)

# generating pdf from back pages
back_image_list[0].save(r'back_pages.pdf', save_all=True, append_images=back_image_list[1:])

# generating front pages
for f in range(len(front_pages)):
	page_counter += 1
	image1 = Image.open(f'images/{front_pages[f][0]}.jpg')
	image2 = Image.open(f'images/{front_pages[f][1]}.jpg')
	new_image = Image.new('RGB',(2*image1.size[0], image2.size[1]), (250,250,250))
	new_image.paste(image1,(0,0))
	new_image.paste(image2,(image1.size[0],0))
	new_image.save(f"images/merged_pages/front_pages/{page_counter}_{front_pages[f][0]}_{front_pages[f][1]}.jpg","JPEG")
	front_image_list.append(new_image)


# generating pdf from front pages

front_image_list[0].save(r'front_pages.pdf', save_all=True, append_images=front_image_list[1:])