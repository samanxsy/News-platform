{% for country in countries %}
    <option value="{{ country.code }}" 
        {% if session['country'] == country.code %}selected{% endif %}>{{ country.name }}</option>
{% endfor %}