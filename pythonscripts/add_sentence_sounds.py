#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  add_sentence_sounds.py
#  
#  Copyright 2020 TIm Leverentz <levtim@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from bs4 import BeautifulSoup

def find_paragraphs(link):
	paragraphsoup = BeautifulSoup(open("..//" + link),"html5lib")
	paragraphs = [x.get_text().rstrip().replace("\n","").replace("  ","") for x in paragraphsoup.find_all("p") if x.get_text() not in ["","\n",None]]
	#for p in paragraphs:
		#print(p)
	#print(paragraphs)
	return paragraphs

def main(args):
	linksoup = BeautifulSoup(open("../storyindex.html"),"html5lib")
	links = [x["href"] for x in linksoup.find_all("a")]
	all_text = []
	for link in links:
		for line in find_paragraphs(link):
			all_text.append(line)
	print(all_text)
	print(len(all_text))
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
