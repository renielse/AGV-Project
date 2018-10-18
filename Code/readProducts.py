
import xml.etree.ElementTree as ET
import numpy as np

productDescrURL = "./Products_Composition/ProductsDescription.xml"
compDescrURL = "./Products_Composition/ComponentsDescription.xml"

dicProd = {}
dicCompPos = {}

def productsSetUp():

	prodDesc = ET.parse(productDescrURL)
	compDesc = ET.parse(compDescrURL)

	rootProd = prodDesc.getroot()
	rootComp = compDesc.getroot()

	prodDic = {}
	for prod in rootProd:
		comPosArr = np.array([])
		prodID = prod.attrib["name"]
		print(prodID)
		for comp in prod:
			xVal = int(rootComp[int(comp.text)-1][0].text)
			yVal = int(rootComp[int(comp.text)-1][1].text)
			print("[", xVal, yVal,"]")
			if comPosArr.size == 0:
				comPosArr = np.array([[xVal, yVal]])
			else:
				comPosArr = np.insert(comPosArr, len(comPosArr), [xVal, yVal], 0)
		prodDic[prodID] = comPosArr

	print("\n",prodDic)


productsSetUp()
