source 'https://rubygems.org'

# Use GitHub Pages
gem 'github-pages', group: :jekyll_plugins

group :jekyll_plugins do
  gem 'jekyll-paginate-v2'
  gem 'jekyll-sitemap'
  gem 'jekyll-feed'
end

# Windows and JRuby does not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock http_parser.rb gem to v0.6.x on JRuby builds
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]