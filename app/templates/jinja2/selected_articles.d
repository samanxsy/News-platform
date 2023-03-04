{% for news in articles %}
    {% set keyword = news['title'].lower().split() %}
    {% for word in keyword %}
        {% if word in interest_list %}
            <p class="authors">{{ news['author'] }}</p>
            <h3>{{ news['title'] }}</h3>
            <a class="links" href="{{ news['url'] }}">Read more on {{ news['author'] }}</a>
            <p class="space"></p>
        {% endif %}
    {% endfor %}
{% endfor %}
