<h1></h1>
<h2>Описание работы команд</h2>
<h3>Команда /start</h3>

<b>После ввода команды:</b>
<ul>
   <li>Выводится приветствие пользователю</li>
</ul>

<h3>Команда /help</h3>
<b>После ввода команды:</b>
<ul>
   <li>Выводится список всех команд, кратким описанием, что делает каждая команда</li>
</ul>

<h3>Команда /low</h3>
<b>После ввода команды у пользователя запрашивается:<b>
<ol>
   <li>Город, где будет проводиться поиск</li>
   <li>Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный</li>
   <li>Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)</li>
   <li>Запрашиваются минимальная и максимальная стоимость отеля в долларах США</li>
   <li>Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)</li>
   <li>Выводится календарь с возможностью выбора даты заезда или выезда.</li>
</ol>

<h3>Команда /high</h3>
<b>После ввода команды у пользователя запрашивается:</b>
<ol>
   <li>Город, где будет проводиться поиск</li>
   <li>Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный</li>
   <li>Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)</li>
   <li>Запрашиваются минимальная и максимальная стоимость отеля в долларах США</li>
   <li>Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)</li>
   <li>Выводится календарь с возможностью выбора даты заезда или выезда.</li>
</ol>

<h3>Команда /custom</h3>
<b>После ввода команды у пользователя запрашивается:<b>
<ol>
   <li>Город, где будет проводиться поиск</li>
   <li>Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный</li>
   <li>Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)</li>
   <li>Запрашиваются минимальная и максимальная стоимость отеля в долларах США</li>
   <li>Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)</li>
   <li>Выводится календарь с возможностью выбора даты заезда или выезда.</li>
   <li>Диапазон расстояния, на котором находится отель от центра</li>
</ol>

<h3>Команда /history</h3>
<b>После ввода команды пользователю выводится история поиска отелей:</b>
<ul>
   <li>Выдает список выполненных пользователем запросом, но не более 5</li>
   <li>Дату и время ввода команды</li>
   <li>То слово (город), по которому пользователь искал отели</li>
   <li>Если пользователю фотографии были не нужны, то они выведены не будут</li>
</ul>

<h2>Описание внешнего вида и UI</h2>
<b>Окно Telegram-бота при запущенном Python-скрипте воспринимает следующие команды:</b>
<ul>
   <li>/start - запуск бота</li>
   <li>/help — помощь по командам бота</li>
   <li>/low — вывод самых дешёвых отелей в городе</li>
   <li>/high — вывод самых дорогих отелей в городе</li>
   <li>/custom — вывод отелей, наиболее подходящих по цене и расположению от центра</li>
   <li>/history — вывод истории поиска отелей</li>
</ul>

<b>Для команд low, high и custom сообщение с результатом содержит краткую информацию по каждому отелю. В эту информацию входит:</b>

<ul>
   <li>Название отеля</li>
   <li>Адрес</li>
   <li>Цена за ночь (в долларах США)</li>
   <li>Как далеко отель расположен от центра</li>
   <li>N фотографий отеля (если пользователь счёл необходимым их вывод)</li>
</ul>

<h3>В разработке использованы</h3>
pyTelegramBotAPI==4.4.0
python-dotenv==0.19.2
pip~=21.1.2
wheel~=0.36.2
certifi~=2022.6.15
requests~=2.28.1
idna~=3.3
urllib3~=1.26.11
setuptools~=57.0.0
loguru~=0.6.0
