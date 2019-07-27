<!DOCTYPE html>
<html>
<head>
<meta charse="utf-8">
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" type="text/css">
<title>{{name}}'s movielist</title>
</head>
<body>
<h1>{{name}}'s moveslist</h1>
<p> {{movies|length}} titles</p>
<br>
<ul>
{% for movie in movies%}
<li>{{movie.index}}--{{movie.title}}--{{movie.actor}}--{{movie.time}}</li>
<p><img src="{{movie.image}}"></p>
<br>
{% endfor %}
</ul>

<img alt="haha" class="totoro" src="{{url_for('static',filename='totoro.gif')}}">
</body>
</html>
