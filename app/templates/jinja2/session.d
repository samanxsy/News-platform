{% if session['country'] %}
<input type="hidden" name="country" value="{{ session['country'] }}">
{% endif %}