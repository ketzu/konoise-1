# 한국어 노이즈 추가 (konoise)
한국어 문서에 노이즈를 추가하는 것을 돕는 파이썬 라이브러리입니다(Library for generating the noise in Korean).

## 설치 방법
```
$ pip install konoise
```

## 실행 방법
```
from konoise import NoiseGenerator

text = "행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다."
generator = NoiseGenerator(num_cores=8)
text = generator.generate(text, methods='disattach-letters', prob=1., delimeter='newline', verbose=1)
print(text)
>> 행복한 ㄱㅏ정은 모두ㄱㅏ 닮았ㅈㅣ만, 불행한 ㄱㅏ정은 모두 ㅈㅓㅁㅏㄷㅏ의 ㅇㅣ유로 불행ㅎㅏㄷㅏ.
```
-- text: 노이즈를 생성할 텍스트입니다.
-- methods: 노이즈 생성 방법입니다(사용가능한 방법들은 아래를 참고, default:).
-- prob: 노이즈를 생성하는 확률입니다(delimeter별로 적용, 0-1사이의 실수).
-- delimeter: 노이즈 적용, 멀티 프로세싱 적용의 기준이 되는 단위 입니다('total':전체,'newline':개행(\n),'sentence':문장).
-- verbose: 로그 표시에 대한 변수입니다(0:표시 안함, 1: 표시).

## 노이즈 생성 방법
노이즈를 생성하는 방법은 총 6가지가 구현되어 있습니다.
```
'disattach-letters': disattach_letters,
'change-vowels': change_vowels,
'palatalization': partial(phonetic_change, func='palatalization'),
'linking': partial(phonetic_change, func='linking'),
'liquidization': partial(phonetic_change, func='liquidization'),
'nasalization': partial(phonetic_change, func='nasalization'),
'assimilation': partial(phonetic_change, func='assimilation'),
'yamin-jungum': yamin_jungum
```
- 쉼표(,)로 구분하여 여러 방법들을 같이 사용할 수 있습니다.
- 전체 방법을 사용하려면 methods에 'all'을 입력합니다.

**[disattach-letters]** 자모 분리(alphabet separation)에 의한 노이즈 추가 방법. 글자의 자음과 모음을 분리합니다. 단, 가독성을 위해 종성이 없으며 중성이  'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅗ' 가 아닐 경우 실행합니다(예: 안녕하세요 > 안녕ㅎㅏㅅㅔ요)

**[change-vowels]** 모음 변형에 의한 노이즈 추가 방법입니다. 글자의 모음을 변형시킵니다. 단, 가독성을 위해 종성이 없으며 중성이 'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ' 일 경우 실행합니다(예: 안녕하세요 > 안녕햐세오).

**[palatalization]** 음운변화 중, 구개음화를 구현하는 함수입니다.

**[linking]** 음운변화 중, 연음을 구현하는 함수입니다.

**[liquidization]** 음운변화 중, 유음화를 구현하는 함수입니다.

**[nasalization]** 음운변화 중, 비음화를 구현하는 함수입니다.

**[assimilation]** 음운변화 중, 음운동화를 구현하는 함수입니다.

**[yamin-jungum]** 야민정음으로 일부 글자를 변환합니다. 단, 가독성이 떨어지는 일부 표현은 제외되었습니다(귀여워 > 커여워).



**변형 예시**
```
[original]  행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다.

[disattach-letters, prob=1.] 행복한 ㄱㅏ정은 모두ㄱㅏ 닮았ㅈㅣ만, 불행한 ㄱㅏ정은 모두 ㅈㅓㅁㅏㄷㅏ의 ㅇㅣ유로 불행ㅎㅏㄷㅏ.

[change-vowels, prob=1.] 행복한 갸정은 묘듀갸 닮았지만, 불행한 갸정은 묘듀 져먀댜의 이우료 불행햐댜.

[palatalization, prob=1.] 행보칸 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다.

[linking, prob=1.] 행복한 가정은 모두가 달맜지만, 불행한 가정은 모두 저마다의 이유로 불행하다.

[liquidization, prob=1.] 행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다.(No Change)

[nasalization, prob=1.] 행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다. (No Change)

[assimilation, prob=1.] 행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다. (No Change)

[yamin-jungum, prob=1.] 행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이윾로 불행하다.
```

## 기타
- 비음화, 유음화, 구개음화, 연음, 음운동화의 모든 규칙이 구현되지 않은 상태이며, 추후 확대될 예정입니다(누락된 규칙이 있을 수 있으니, 발견 시 피드백 주시면 감사하겠습니다).
- prob는 변형 가능한 글자들에 대해서 해당 확률만큼 확률적으로 실행됩니다(prob가 1이라고 해서 모든 텍스트가 변경되는 것이 아닙니다).
- 두 개 이상의 방법을 사용할 경우(쉼표로 구분), 한 단위 텍스트에서 두 개의 방법이 사용되는 것이 아니라 각 단위 텍스트마다 랜덤하게 방법을 결정하여 실행합니다. 
