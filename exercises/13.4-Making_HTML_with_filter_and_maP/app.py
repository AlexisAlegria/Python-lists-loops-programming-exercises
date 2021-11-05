all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]
def filter_colors(color):
	return color["sexy"] == True

sexyColors = list(filter(filter_colors,all_colors))

def generate_li(sexyColors):
	sexy_colors_list = list(map(lambda color: "<li>" + color["label"] + "</li>",sexyColors))
	no_comas_between_lis = "".join(sexy_colors_list)
	return no_comas_between_lis

print(generate_li(sexyColors)) 



