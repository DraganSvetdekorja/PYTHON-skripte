import requests
from selectorlib import Extractor
import pandas as pd

# Create an Extractor object with the selectorlib configuration
e = Extractor.from_yaml_string('''
product:
    css: row-offcanvas-left
    type: Text
    children:
		naziv:
			css: h1.card-title
			type: Text
		kolekcija_naziv:
			xpath: '//*[@id="stage-item-coll"]/a'
			type: Text
		kolekcija:
			xpath: '//*[@id="stage-item-coll"]/a/strong'
			type: Text
		slika:
			css: a.thumb
			multiple: true
			type: Attribute
			attribute: data-stage-img

''')

# List of URLs to scrape
urls = [
"https://www.tapetenshop.de/cremeweisse-tapete-seidenmatt-mit-natuerlichem-struktureffekt-3772380981/",
"https://www.tapetenshop.de/tapete-graublau-hell-seidenmatt-mit-struktureffekt-3772380982/",
"https://www.tapetenshop.de/vliestapete-taupe-einfarbig-seidenmatt-mit-struktureffekt-3772380983/",
"https://www.tapetenshop.de/rosa-vliestapete-seidnematt-uni-mit-struktureffekt-3772380984/",
"https://www.tapetenshop.de/vliestapete-taubengrau-seidenmatt-uni-mit-struktureffekt-3772380985/",
"https://www.tapetenshop.de/tapete-mintgruen-uni-seidnematt-mit-strukturmuster-3772380986/",
"https://www.tapetenshop.de/blaue-vliestapete-einfarbig-seidenmatt-mit-struktureffekt-3772380987/",
"https://www.tapetenshop.de/tapete-metallic-weiss-mit-natuerlichem-struktureffekt-3772380988/",
"https://www.tapetenshop.de/hellgraue-vliestapete-mit-sturkutmuster-einfarbig-seidenmatt-3772380989/",
"https://www.tapetenshop.de/einfarbige-tapete-beige-grau-mit-seidenmatt-finish-3772380991/",
"https://www.tapetenshop.de/einfarbige-tapete-creme-beige-mit-seindenmatt-finish-3772380992/",
"https://www.tapetenshop.de/marmoroptik-tapete-in-creme-mit-strukturdesign-3933388171/",
"https://www.tapetenshop.de/marmortapete-mit-metallic-glanz-und-strukturdesign-3933388172/",
"https://www.tapetenshop.de/gold-marmor-tapete-mit-metallic-strukturdesign-weiss-metallic-3933388173/",
"https://www.tapetenshop.de/graue-marmortapete-mit-metallic-effekt-grau-beige-3933388174/",
"https://www.tapetenshop.de/schwarze-marmortapete-mit-gold-marmor-effekt-3933388175/",
"https://www.tapetenshop.de/retro-tapete-50er-starburst-motiv-schwarz-metallic-3933388181/",
"https://www.tapetenshop.de/tapete-retro-design-starburst-blau-metallic-3933388182/",
"https://www.tapetenshop.de/designtapete-mit-50er-retro-muster-creme-metallic-3933388183/",
"https://www.tapetenshop.de/weisse-tapete-mit-retro-metallic-muster-starburst-weiss-3933388184/",
"https://www.tapetenshop.de/tapete-mit-textildesign-und-linieneffekt-schwarz-3933388191/",
"https://www.tapetenshop.de/unitapete-mit-graublauer-textiloptik-blau-metallic-3933388192/",
"https://www.tapetenshop.de/einfarbige-tapete-hellgrau-mit-feinem-linienmuster-3933388193/",
"https://www.tapetenshop.de/hellgraue-tapete-mit-linienmuster-metallic-grau-3933388194/",
"https://www.tapetenshop.de/greige-tapete-metallic-glanz-und-linienmuster-grau-3933388195/",
"https://www.tapetenshop.de/metallic-tapete-in-beige-mit-linienstruktur-beige-3933388196/",
"https://www.tapetenshop.de/unifarbene-tapete-elfenbein-mit-linienstruktur-creme-3933388197/",
"https://www.tapetenshop.de/metallic-tapete-gold-beige-mit-linienmuster-3933388198/",
"https://www.tapetenshop.de/tapete-lila-grau-liniert-mit-metallic-glanz-grau-violett-3933388199/",
"https://www.tapetenshop.de/rosa-tapete-vlies-liniert-mit-metallic-glanz-rosa-3933388201/",
"https://www.tapetenshop.de/tapete-blumendesign-im-vintage-stil-blau-gelb-3933388211/",
"https://www.tapetenshop.de/blumentapete-im-kunststil-mit-rosen-gelb-braun-3933388212/",
"https://www.tapetenshop.de/vintage-blumentapete-klassik-rosen-muster-creme-braun-3933388213/",
"https://www.tapetenshop.de/rosen-tapete-im-vintage-stil-metallic-schwarz-weiss-3933388214/",
"https://www.tapetenshop.de/retro-tapete-50er-jahre-linienmuster-weiss-metallic-3933388221/",
"https://www.tapetenshop.de/tapete-50er-jahre-retro-design-blau-metallic-3933388222/",
"https://www.tapetenshop.de/retro-tapete-50er-jahre-linienmuster-creme-metallic-3933388223/",
"https://www.tapetenshop.de/tapete-50er-jahre-retro-design-schwarz-metallic-3933388224/",
"https://www.tapetenshop.de/putzoptik-tapete-mit-strukturmuster-grau-beige-3933388231/",
"https://www.tapetenshop.de/graue-betonoptik-tapete-mit-used-optik-grau-3933388232/",
"https://www.tapetenshop.de/hellgraue-betontapete-mit-strukturdesign-grau-3933388233/",
"https://www.tapetenshop.de/schwarze-strukturtapete-mit-rustikaler-betonoptik-3933388234/",
"https://www.tapetenshop.de/petrol-tapete-betonoptik-mit-strukturdesign-gruen-metallic-3933388235/",
"https://www.tapetenshop.de/beige-tapete-mit-rustikalem-strukturdesign-in-putzoptik-3933388236/",
"https://www.tapetenshop.de/putzoptik-tapete-creme-beige-mediterran-stil-3933388237/",
"https://www.tapetenshop.de/textiloptik-tapete-mit-rauten-muster-metallic-grau-3933388241/",
"https://www.tapetenshop.de/rauten-tapete-mit-melierter-textiloptik-metallic-gruen-3933388242/",
"https://www.tapetenshop.de/textiloptik-tapete-mit-rauten-muster-metallic-weiss-3933388243/",
"https://www.tapetenshop.de/rauten-tapete-mit-textiloptik-metallic-creme-gelb-3933388244/",
"https://www.tapetenshop.de/ethno-tapete-mit-rauten-design-metallic-schwarz-3933388245/",
"https://www.tapetenshop.de/natur-tapete-mit-floral-muster-grau-gruen-rosa-3933388251/",
"https://www.tapetenshop.de/tapete-blumen-beeren-im-landhaus-stil-creme-rot-3933388252/",
"https://www.tapetenshop.de/blumentapete-petrol-mit-floralem-muster-gruen-gelb-3933388253/",
"https://www.tapetenshop.de/schwarze-blumentapete-mit-bluehten-muster-in-grau-und-gruen-3933388254/",
"https://www.tapetenshop.de/hellgraue-vliestapete-metallic-muster-metallic-grau-3933388261/",
"https://www.tapetenshop.de/tapete-creme-beige-mit-metallic-strukturmuster-3933388262/",
"https://www.tapetenshop.de/altrosa-tapete-mit-gold-linienmuster-metallic-rosa-3933388263/",
"https://www.tapetenshop.de/mintgruene-tapete-silber-strukturmuster-metallic-gruen-3933388264/",
"https://www.tapetenshop.de/tapete-senfgelb-mit-metallic-strukturmuster-gelb-3933388265/",
"https://www.tapetenshop.de/ziegelrote-tapete-mit-silbernem-strukturmuster-orange-rot-3933388266/",
"https://www.tapetenshop.de/dunkelgrau-melierte-tapete-mit-metallic-linienmuster-3933388267/",
"https://www.tapetenshop.de/dunkelrote-tapete-mit-silbernem-linienmuster-3933388268/",
"https://www.tapetenshop.de/3d-betonoptik-tapete-mit-strukturdetails-blau-3933388271/",
"https://www.tapetenshop.de/anthrazit-tapete-mit-3d-betonoptik-schwarz-grau-3933388272/",
"https://www.tapetenshop.de/3d-tapete-greige-mit-betonoptik-design-grau-beige-3933388273/",
"https://www.tapetenshop.de/3d-tapete-kalkstein-mit-strukturdesign-weiss-grau-3933388274/",
"https://www.tapetenshop.de/steinoptik-tapete-rote-ziegelmauer-mit-3d-effekt-creme-rot-3933388291/",
"https://www.tapetenshop.de/ziegelwand-tapete-grau-mit-3d-motiv-grau-3933388292/",
"https://www.tapetenshop.de/braune-steintapete-mit-ziegelmaueroptik-braun-grau-3933388293/",
"https://www.tapetenshop.de/steinoptik-tapete-mit-3d-mauerwerk-grau-weiss-3933388294/",
"https://www.tapetenshop.de/skandi-tapete-mit-blaettermuster-in-metallic-blau-gruen-3933388301/",
"https://www.tapetenshop.de/tapete-blaetter-design-im-boho-stil-beige-metallic-3933388302/",
"https://www.tapetenshop.de/metallic-tapete-blaettermuster-im-skandi-stil-grau-metallic-3933388303/",
"https://www.tapetenshop.de/blaue-tapete-mit-gold-design-im-boho-stil-3933388304/",
"https://www.tapetenshop.de/gruene-tapete-blaettermuster-mit-metallic-struktureffekt-3933388311/",
"https://www.tapetenshop.de/graue-blaetter-tapete-mit-strukturdetails-und-metallic-effekt-3933388312/",
"https://www.tapetenshop.de/schwarze-metallic-tapete-mit-floralem-muster-3933388313/",
"https://www.tapetenshop.de/silberne-tapete-mit-blaetter-design-und-struktureffekt-3933388314/",
"https://www.tapetenshop.de/dunkelgruene-tapete-mit-textur-und-metallic-effekt-3933388321/",
"https://www.tapetenshop.de/terracotta-optik-tapete-mit-strukturdesign-metallic-3933388322/",
"https://www.tapetenshop.de/putzoptik-tapete-hellgrau-mit-metallic-strukturdesign-3933388323/",
"https://www.tapetenshop.de/dunkelgraue-putzoptik-tapete-mit-metallic-struktur-3933388324/",
"https://www.tapetenshop.de/schwarze-tapete-rustikale-strukturoptik-mit-metallic-effekt-3933388325/",
"https://www.tapetenshop.de/blaue-tapete-mit-goldenem-metallic-akzent-und-strukturdetails-3933388326/",
"https://www.tapetenshop.de/rustikale-putzoptik-tapete-mit-struktur-blau-gruen-grau-3933388327/",
"https://www.tapetenshop.de/graue-vliestapete-mit-metallic-struktureffekt-3933388328/",
"https://www.tapetenshop.de/cremeweisse-tapete-mit-strukturdesign-creme-metallic-3933388329/",
"https://www.tapetenshop.de/creme-vliestapete-mit-strukturmuster-in-putzoptik-3933388331/",
"https://www.tapetenshop.de/tapete-bronze-einfarbig-mit-metallic-akzent-braun-3933388332/"





]

# List to store extracted data
data_list = []

# Scrape data from each URL
for url in urls:
    # Send a GET request to the web page
    response = requests.get(url)

    # Pass the HTML content to the Extractor's extract() method
    data = e.extract(response.text)

    # Append the extracted data to the list
    data_list.extend(data['product'])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data_list)

# Save the DataFrame to an Excel file
df.to_excel("BOS_extracted_data.xlsx", index=False)

print("Data has been extracted and saved to 'BOS_extracted_data.xlsx'.")
