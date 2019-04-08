username = "rivenblades"
git_repo_name = "Armory-rivenblades"
branch_name = "master"
file_name = "camera.h"

url = "https://raw.githubusercontent.com/"+\
username+"/"+git_repo_name+"/"+branch_name+"/"+file_name


print("Downloading " + file_name + " from " + git_repo_name+" git repository")



import math
import random
import threading
import pygit2
import os
import sys
import requests
from clint.textui import progress
import shutil #for terminal size
sys.path.append('/home/kostas/Documents/python/')
import term_colors as c

# You must define a proxy list
# I suggests https://free-proxy-list.net/
proxies = {
	0: {'http': 'http://34.208.47.183:80'},
	1: {'http': 'http://40.69.191.149:3128'},
	2: {'http': 'http://104.154.205.214:1080'},
	3: {'http': 'http://52.11.190.64:3128'}
}
term_width  = shutil.get_terminal_size((80,20))[0]
term_height = shutil.get_terminal_size((80,20))[1]-2
# you must define the list for files do you want download

downloaderses = list()


def clamp(value,max):
	if value > max:
		value = max;
	return value

def downloaders(file, path = None, selected_proxy=proxies):
	print("Downloading file named {} by proxy {}...".format(file, selected_proxy))
	r = requests.get(file, stream=True, proxies=selected_proxy)
	
	filename = file.split("/")[-1]
	if path != None:
		if path[-1] != '/':
			path = path + '/'
	with open(path + filename, 'wb') as f:
		total_length = int(r.headers.get('content-length'))
		# for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
		#     if chunk:
		#         f.write(chunk)
		#         f.flush()
		chunk_size = 1024
		expected_size=(total_length / chunk_size) + 1

		iteration = 0
		for chunk in r.iter_content(chunk_size=chunk_size):
			if chunk:
				f.write(chunk)
				f.flush()
				remainingSize = total_length - chunk_size
				iteration += 1
				times = int(100/int(expected_size)*iteration)
				#print("\r[{}%:100%]" .format(int(100/int(expected_size)*iteration)), end = "")
				indicator = '[{}%:100%]'.format(times)
				print("\r{}{}".format('█'*int(clamp(times,term_width)-len(indicator)),indicator), end = "")
		print()
		print('{}Sir, downloading {} completed!'.format(c.CYELLOW+'[Veronica]:'+c.CEND,filename))

def clone_repo(url,path=None,bare=False, repository=None, remote=None, checkout_branch=None, callbacks=None):
	if path == None:
		path = os.getcwd()+"/"+url.split("/")[-1][:-4]
	print("Saving at Path:"+path)
	pygit2.clone_repository(url, path, 
	bare, repository, remote, checkout_branch, callbacks)

#files to download
files = \
[
	url,
	"https://stackoverflow.com/questions/23645212/requests-response-iter-content-gets-incomplete-file-1024mb-instead-of-1-5gb",
	"https://publicliterature.org/2008/02/08/dracula",
]

for file in files:
	selected_proxy = proxies[math.floor(random.random() * len(proxies))]
	t = threading.Thread(target=downloaders, args=(file, os.getcwd()+'/',selected_proxy))
	downloaderses.append(t)

for _downloaders in downloaderses:
	_downloaders.start()

# print("Cloning a git repo: ", "https://github.com/rivenblades/Armory-rivenblades.git")
# clone_repo("https://github.com/rivenblades/Armory-rivenblades.git")