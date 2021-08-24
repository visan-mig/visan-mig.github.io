---
title: "VisAn-MIG - Team"
layout: gridlay
excerpt: "VisAn-MIG: Team members"
sitemap: false
permalink: /team/
---

# VisAn-MIG Team Members

{% for member in site.data.team_members %}

<div class="row">

<div class="col clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}</i>
  Role: <b>{{ member.role }}</b>
  <p> {{ member.description }} </p>
</div>

</div>

{% endfor %}
