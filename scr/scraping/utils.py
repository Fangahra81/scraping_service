cirillic_l = {
    u'а': u'a',
    u'б': u'b',
    u'в': u'v',
    u'г': u'g',
    u'д': u'd',
    u'е': u'e',
    u'ё': u'yo',
    u'Ж': u'j',
    u'з': u'z',
    u'и': u'i',
    u'й': u'y',
    u'к': u'k',
    u'л': u'l',
    u'м': u'm',
    u'н': u'n',
    u'о': u'o',
    u'п': u'p',
    u'р': u'r',
    u'с': u's',
    u'т': u't',
    u'у': u'u',
    u'ф': u'f',
    u'х': u'h',
    u'ц': u'c',
    u'ч': u'ch',
    u'ш': u'sh',
    u'щ': u'sch',
    u'ъ': u'',
    u'ы': u'i',
    u'ь': u'',
    u'э': u'e',
    u'ю': u'u',
    u'я': u'ya'

}


def from_cirillic_to_lat(text: str):
    text = text.replace(' ', '_').lower()
    tmp = ''

    for ch in text:
        tmp += cirillic_l.get(ch, ch)
    return tmp