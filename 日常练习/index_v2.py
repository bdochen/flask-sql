<!DOCTYPE html>
<html>
<head>
<meta charse="utf-8">
<title>{{name}}'s movielist</title>
</head>
<body>
<h1>{{name}}'s moveslist</h1>
<p> {{movies|length}} titles</p>
<br>
<img src="{{url_for('static',filename='lm.jpg')}}">
<ul>
{% for movie in movies%}
<li>{{movie.index}}--{{movie.title}}--{{movie.actor}}--{{movie.time}}--<img src="{{movie.image}}"></li>
{% endfor %}
</ul>
</body>
</html>
