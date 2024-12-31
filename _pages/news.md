---
title: "VisAn-MIG - News"
layout: gridlay
excerpt: "VisAn-MIG -- News."
sitemap: false
permalink: /news/
pagination:
  enabled: true
  collection: news_items
  per_page: 10
  sort_field: date
  sort_reverse: true
---

<div class="col-sm-12">
<h1>News</h1>
</div>

<div class="row">
<div class="col-sm-12 clearfix">
{% for post in paginator.collections.news_items %}
<div class="well">
  <h4>{{ post.date | date: "%-d %B %Y" }}</h4>
  <pubtit>{{ post.title }}</pubtit>
  <p><em>{{ post.source }}: "{{ post.headline }}"</em></p>
  {{ post.content }}
</div>
{% endfor %}

<!-- Pagination links -->
<div class="pagination text-center">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" class="previous">&laquo; Previous</a>
  {% endif %}
  
  <span class="page_number">
    Page {{ paginator.page }} of {{ paginator.total_pages }}
  </span>

  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" class="next">Next &raquo;</a>
  {% endif %}
</div>
</div>
</div>