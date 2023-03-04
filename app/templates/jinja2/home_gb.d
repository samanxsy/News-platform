{% for news in articles_uk %}
    <p class="authors">{{ news['author'] }}</p>
    <h3>{{ news['title'] }}</h3>
    <a class="links" href="{{ news['url'] }}">Read more on {{ news['author'] }}</a>
    <p class="space"></p>
{% endfor %}
