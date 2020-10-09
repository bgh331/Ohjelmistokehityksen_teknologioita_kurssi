
import urllib.request
import json

JSON_URL = 'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'


def hae_postinumerot():  
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())

def toimipaikat_ja_numerot(postinumerot):
    toimipaikat_ja_numerot = {}
    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]
    return toimipaikat_ja_numerot


def populate():
    postinumerot = hae_postinumerot()
    toimipaikat_ja_numerot = {}
    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]
    return toimipaikat_ja_numerot



def inputword(inputSearch, toimipaikat_ja_numerot):
    if inputSearch in toimipaikat_ja_numerot:
        loydetyt = toimipaikat_ja_numerot[inputSearch]
        #print('Postinumerot: ' + ', '.join(loydetyt))
        return loydetyt
    else:
        return {}
        #print('Postitoimipaikkaa ei löytynyt :(')


def main():
    postinumerot = hae_postinumerot()
    toimipaikat = toimipaikat_ja_numerot(postinumerot)
    inputSearch = input('Kirjoita postitoimipaikka: ').strip().upper()
    loydetyt = inputword(inputSearch, toimipaikat)
    if (inputword(inputSearch, toimipaikat)):  # If this returns TRUE.
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Postitoimipaikkaa ei löytynyt :(')


if __name__ == '__main__':
    main()
