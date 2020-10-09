
from postinumero import toimipaikat_ja_numerot, inputword, hae_postinumerot, populate


def test_fetching_works():
    postinumerot_dict = hae_postinumerot()
    assert len(postinumerot_dict) > 200

    for i in range(0, len(postinumerot_dict) - 1):
        first = list(postinumerot_dict)[i]
        second = list(postinumerot_dict)[i+1]

        assert first != second

postalNumb = {
    10120: "RÄMÄLÄ",
    10211: "RÄMÄLÄ",
    10140: "KÄRKELÄ",
    10160: "HATTIVATTILA",
    
}
def test_populating_toimipaikat_and_numerot_with_mock_up_data():
    Fdict = toimipaikat_ja_numerot(postalNumb)

    assert "RÄMÄLÄ" in Fdict and "KÄRKELÄ" in Fdict and "HATTIVATTILA" in Fdict and "HELSINKI" not in Fdict


def test_searching_by_a_certain_word_with_mock_up_data():
    hae_first = "HELSINKI"
    hae_second = "INKOO"
    Fdict = toimipaikat_ja_numerot(postalNumb)
    postalCodeForHelsinki = inputword(
        hae_first, Fdict)
    postalCodeForRÄMÄLÄ = inputword(
        hae_second, Fdict)

   
    assert hae_first not in Fdict and hae_second in Fdict and postalCodeForHelsinki == {} and len(
        postalCodeForHelsinki) == 0 and postalCodeForRÄMÄLÄ == [10210, 10211] and len(postalCodeForRÄMÄLÄ) > 1 and len(
            postalCodeForRÄMÄLÄ) == 2



#Kiia Kaukonen


    