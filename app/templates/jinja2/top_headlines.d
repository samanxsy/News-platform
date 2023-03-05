{% set count = 0 %}
{% for news in articles %}
    {% if count < 5 %}
        <p class="authors">{{ news['source']['name'] }}</p>
        <h3>{{ news['title'] }}</h3>
        <P class="description">{{ news['description'] }}</P>
        <p class="writer">By {{ news['author'] }}</p>
        <a class="links" href="{{ news['url'] }}">Read more on {{ news['source']['name'] }}</a>
        <p class="space"></p>
        {% set count = count + 1 %}
    {% endif %}
{% endfor %}
