#!/usr/bin/env python
# encoding: utf-8

from BeautifulSoup import BeautifulSoup
import urllib2

url = "http://www.gran-turismo.com/local/jp/data1/products/gt5/carlist_en.html"

pagina = urllib2.urlopen(url).read()

soup = BeautifulSoup(pagina)
soup.prettify()  					# Refaz a estrutura do codigo como html

table = soup.find('table')
rows = table.findAll('tr')

for tr in rows:
	
  # Estrai informações de standard	
  cols1 = tr.findAll('td')		 		# [<td class="icon2">&nbsp;</td>, <td class="icon"><img src="./images/icon02.jpg" width="16" 
										#   height="14" alt="standard" /></td>, <td><p>AC Cars 427 S/C '66</p></td>]
									
  # Pega o codigo do Carro.										
  textID = ''.join(tr.find(text=True)) 
  
  #textCarro = ''.join(cols1.find(text=True))

  print textID, cols1 
  										          	
  #splT1 = str((cols1[1])).split('"')	# <td class="icon"><img src="./images/icon02.jpg" width="16" height="14" alt="standard" /></td>
  #print (textID, splT1[9])				# Retira da string a informacao de standard/premium
  # ------------
   
print