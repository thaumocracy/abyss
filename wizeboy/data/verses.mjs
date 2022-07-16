// for testing purposes
const verses = [
  {
    id: 0,
    author: "Николай Карамзин",
    title: "Прости",
    tags: [],
    text: `
Кто мог любить так страстно,
Как я любил тебя?
Но я вздыхал напрасно,
Томил, крушил себя!

Мучительно плениться,
Быть страстным одному!
Насильно полюбиться
Не можно никому.

Не знатен я, не славен,-
Могу ль кого прельстить?
Не весел, не забавен,-
За что меня любить?

Простое сердце, чувство
Для света ничего.
Там надобно искусство —
А я не знал его!

(Искусство величаться,
Искусство ловким быть,
Умнее всех казаться,
Приятно говорить.)

Не знал — и, ослепленный
Любовию своей,
Желал я, дерзновенный,
И сам любви твоей!

Я плакал, ты смеялась,
Шутила надо мной,-
Моею забавлялась
Сердечною тоской!

Надежды луч бледнеет
Теперь в душе моей…
Уже другой владеет
Навек рукой твоей!..

Будь счастлива — покойна,
Сердечно весела,
Судьбой всегда довольна,
Супругу — ввек мила!

Во тьме лесов дремучих
Я буду жизнь вести,
Лить токи слез горючих,
Желать конца — прости!`,
  },
  {
    id: 1,
    author: "Гавриил Державин",
    title: "Властителям и судиям",
    tags: [],
    text: `
Восстал всевышний бог, да судит
Земных богов во сонме их;
Доколе, рек, доколь вам будет
Щадить неправедных и злых?

Ваш долг есть: сохранять законы,
На лица сильных не взирать,
Без помощи, без обороны
Сирот и вдов не оставлять.

Ваш долг: спасать от бед невинных,
Несчастливым подать покров;
От сильных защищать бессильных,
Исторгнуть бедных из оков.

Не внемлют! видят — и не знают!
Покрыты мздою очеса:
Злодействы землю потрясают,
Неправда зыблет небеса.

Цари! Я мнил, вы боги властны,
Никто над вами не судья,
Но вы, как я подобно, страстны,
И так же смертны, как и я.

И вы подобно так падете,
Как с древ увядший лист падет!
И вы подобно так умрете,
Как ваш последний раб умрет!

Воскресни, боже! боже правых!
И их молению внемли:
Приди, суди, карай лукавых,
И будь един царем земли!
     `,
  },
  {
    id: 2,
    author: "Омар Хайям",
    title: "Чтоб мудро жизнь прожить, знать надобно немало",
    tags: [],
    text: `
Чтоб мудро жизнь прожить, знать надобно немало,
Два важных правила запомни для начала:
Ты лучше голодай, чем что попало есть,
И лучше будь один, чем вместе с кем попало. `,
  },
  {
    id: 3,
    author: "Эмили Дикинсон",
    title: "Гордись моим сломанным сердцем",
    tags: [],
    text: `
Гордись моим сломанным сердцем, сломавший его,
Гордись моей болью, неведомой мне до того,

Гордись моей ночью, чью тьму погасил ты луной,
Смиреньем моим перед страстью твоей, но не мной,

Не полною чашей девичьих страданий и слез,
Которой ты мог бы хвалиться, хмельной, как Христос,

Раскрыв мне манящие новым мученьем объятия.
Смотри! Я краду у тебя распятье! `,
  },
  {
    id: 4,
    author: "Эдгар Аллан По",
    title: "Гимн",
    tags: [],
    text: `
Зарей, — днем, — в вечера глухие, —
Мой гимн ты слышала, Мария!
В добре и зле, в беде и счастьи,
Целенье мне — твое участье!
Когда часы огнем светали,
И облака не тмили далей,
Чтоб не блуждать как пилигрим,
Я шел к тебе, я шел к твоим.
Вот бури Рока рушат явно
Мое «теперь», мое «недавно»,
Но «завтра», веруют мечты,
Разгонят мрак — твои и ты! `,
  },
  {
    id: 5,
    author: "Жан де Лафонтен",
    title: "Безумец и Мудрец",
    tags: [],
    text: ` 
Безумец раз бросал каменья в Мудреца,
Преследуя его; Мудрец ему на это:
«Мой друг! ты в поте своего лица
Трудился; вот тебе за то монета:
Труд по заслугам должен быть вознагражден.
Взгляни, вот человек проходит, он
Богат безмерно,
И щедро за твои дары воздаст наверно».

К прохожему Глупец направился, спеша
Нанесть ему удар, в надежде барыша;
Но воздаяния дождался он иного:
Прохожий слуг созвал, и те спешат скорей
Избить Глупца и прочь прогнать едва живого.
Таких безумцев видим мы вблизи царей:

Чтоб господина позабавить,
Они на смех поднять готовы вас всегда.
Не стоит трогать их, чтоб замолчать заставить.
Притом же, если вы не в силе, то тогда,
Как вы ни гневайтесь, вам это не поможет;
Направьте их к тому, кто отплатить им может.`,
  },
  {
    id: 6,
    author: "Сергей Есенин",
    title: "Мне грустно на тебя смотреть",
    tags: [],
    text: `
Мне грустно на тебя смотреть,
Какая боль, какая жалость!
Знать, только ивовая медь
Нам в сентябре с тобой осталась.

Чужие губы разнесли
Твое тепло и трепет тела.
Как будто дождик моросит
С души, немного омертвелой.

Ну что ж! Я не боюсь его.
Иная радость мне открылась.
Ведь не осталось ничего,
Как только желтый тлен и сырость.

Ведь и себя я не сберег
Для тихой жизни, для улыбок.
Так мало пройдено дорог,
Так много сделано ошибок.

Смешная жизнь, смешной разлад.
Так было и так будет после.
Как кладбище, усеян сад
В берез изглоданные кости.

Вот так же отцветем и мы
И отшумим, как гости сада…
Коль нет цветов среди зимы,
Так и грустить о них не надо. `,
  },
  {
    id: 7,
    author: "Владимир Маяковский",
    title: "Послушайте",
    tags: [],
    text: `
Послушайте!
Ведь, если звезды зажигают —
значит — это кому-нибудь нужно?
Значит — кто-то хочет, чтобы они были?
Значит — кто-то называет эти плевочки

жемчужиной?
И, надрываясь
в метелях полуденной пыли,
врывается к богу,
боится, что опоздал,
плачет,
целует ему жилистую руку,
просит —
чтоб обязательно была звезда! —
клянется —
не перенесет эту беззвездную муку!
А после
ходит тревожный,
но спокойный наружно.
Говорит кому-то:
«Ведь теперь тебе ничего?
Не страшно?
Да?!»
Послушайте!
Ведь, если звезды
зажигают —
значит — это кому-нибудь нужно?
Значит — это необходимо,
чтобы каждый вечер
над крышами
загоралась хоть одна звезда?! `,
  },
  {
    id: 8,
    author: "Эрих Мария Ремарк",
    title: "Вечерняя песня",
    tags: [],
    text: `
Пусть день был мрачен и жесток сполна,
Разъеденный насмешкой и бедою, —
Твой поцелуй, твоих волос волна —
И муки дня забуду я с тобою.

Пусть день беды в безжалостном огне
В жизнь веру сгложет вновь, подобно зверю, —
Щекой своей прижмешься ты ко мне,
И я опять в себя и в жизнь поверю.

И пусть все то, чем жил я, чем храним,
С начала до конца встает напрасным, —
Оно прелестно — ведь всегда над ним
Благословенье рук твоих прекрасных.`,
  },
  {
    id: 9,
    author: "Борис Пастернак",
    title: "Быть знаменитым некрасиво",
    tags: [],
    text: ` 
Быть знаменитым некрасиво.
Не это подымает ввысь.
Не надо заводить архива,
Над рукописями трястись.

Цель творчества — самоотдача,
А не шумиха, не успех.
Позорно, ничего не знача,
Быть притчей на устах у всех.

Но надо жить без самозванства,
Так жить, чтобы в конце концов
Привлечь к себе любовь пространства,
Услышать будущего зов.

И надо оставлять пробелы
В судьбе, а не среди бумаг,
Места и главы жизни целой
Отчеркивая на полях.

И окунаться в неизвестность,
И прятать в ней свои шаги,
Как прячется в тумане местность,
Когда в ней не видать ни зги.

Другие по живому следу
Пройдут твой путь за пядью пядь,
Но пораженья от победы
Ты сам не должен отличать.

И должен ни единой долькой
Не отступаться от лица,
Но быть живым, живым и только,
Живым и только до конца.`,
  },
  {
    id: 10,
    author: "Анна Ахматова",
    title: "Сероглазый король",
    tags: [],
    text: `
Слава тебе, безысходная боль!
Умер вчера сероглазый король.

Вечер осенний был душен и ал,
Муж мой, вернувшись, спокойно сказал:

«Знаешь, с охоты его принесли,
Тело у старого дуба нашли.

Жаль королеву. Такой молодой!..
За ночь одну она стала седой».

Трубку свою на камине нашел
И на работу ночную ушел.

Дочку мою я сейчас разбужу,
В серые глазки ее погляжу.

А за окном шелестят тополя:
«Нет на земле твоего короля…» `,
  },
];

export default verses;
