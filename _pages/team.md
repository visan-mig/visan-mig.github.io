---
title: "VisAn-MIG - Team"
layout: gridlay
excerpt: "VisAn-MIG: Team members"
sitemap: false
permalink: /team/
---

# VisAn-MIG Team Members

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign rem = number_printed | modulo: 2 %}

<div class="row">

<div class="col clearfix">
  {% if rem == 0 %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  {% elsif rem != 0 %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: right" />
  {% endif %}
  <h4>{{ member.name }}</h4>
  <p><i>{{ member.info }}</i></p>
  <p>Role: <b>{{ member.role }}</b></p>
  <p> {{ member.description }} </p>
  <p><a href="{{ site.url }}{{ site.baseurl }}/teampubs#{{ member.short }}">For a list of selected publications of this team member, click here.</a></p>
</div>

{% assign number_printed = number_printed | plus: 1 %}

</div>

{% endfor %}

<br />

<br />

<h4 style="text-align: center">The Social Science Team</h4>

<img src="{{ site.url}}{{ site.baseurl }}/images/teampic/socsci-team.jpg" class="img-responsive" width="65%" style="display: block; margin-left: auto; margin-right: auto" />
