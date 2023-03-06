{% for news in articles_health %}
    <p class="authors">{{ news['source']['name'] }}</p>
    <h3>{{ news['title'] }}</h3>
    <a class="links" href="{{ news['url'] }}">Read more on {{ news['source']['name'] }}</a>
    <p class="space"></p>
{% endfor %}
