import random
from .utils import assemble, disassemble

rng = random.Random()

excep_dis = ('ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅗ')
chgs = {'ㅏ': 'ㅑ', 'ㅑ': 'ㅏ', 'ㅓ': 'ㅕ', 'ㅕ': 'ㅓ', 'ㅗ': 'ㅛ', 'ㅛ': 'ㅗ', 'ㅜ': 'ㅠ', 'ㅠ': 'ㅜ', }


def _cond_disattach(vlist, base, rng, prob=1.):
    c, v, fc = vlist
    return (fc == ' ') and (v not in base) and (rng.random() < prob)


def _cond_vowel(vlist, base, rng, prob=1.):
    c, v, fc = vlist
    return (fc == ' ') and (v in base) and (rng.random() < prob)


def disattach_letters(text, prob=0.5):
    decomposed = [disassemble(t) for t in text]
    composed = [ ''.join(de) if _cond_disattach(de, excep_dis, rng, prob) else assemble(de) for de in decomposed]
    return ''.join(composed)


def change_vowels(text, prob=0.5):
    decomposed = [disassemble(t) for t in text]
    composed = [ assemble((de[0], chgs[de[1]],de[2])) if _cond_vowel(de, chgs, rng, prob) else assemble(de) for de in decomposed]
    return ''.join(composed)


if __name__ == '__main__':
    print(ord('힣'))
    out = change_vowels('안녕 하세요r', prob=1)
    print(out)