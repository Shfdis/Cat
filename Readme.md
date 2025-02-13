<h1>Catbot</h1>
<p> Telegram bot, that allows to host  tests </p> 
<hr />
<h1> How to use: </h1>
<p>
Run:

``` poetry install & poetry run python Bot.py```

then input your bot's token
</p>
<hr />
<h1> Config file </h1>
<p>First line contains the description of the test</p>
<p>Second line is a single integer that contains the number of qualities that describe the test result</p>
<p>Third line is a single integer that describes the number of questions</p>
<div>
<h2>Following lines describe the questions in following format</h2>
<p>Question text</p>
<p>Number of answers</p>
<p>Answers</p>
<h2>Answer is in following format:</h2>
<p>number of influences</p>
<p>qualities and numerical influences(every quality and its influence are in a single line separated bu a space)</p>
<h2>Results</h2>
<p>Number of results</p>
<h2>Result in following format: </h2>
<p> name</p>
<p>description</p>
<p>image</p>
<p>number of qualites</p>
<p>qualities in format described earlier</p>
</div>