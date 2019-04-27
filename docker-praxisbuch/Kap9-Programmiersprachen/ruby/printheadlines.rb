require 'nokogiri'
require 'open-uri'

Nokogiri::HTML(open("https://heise.de/newsticker/"))
    .search("li.archiv-liste__item .archiv-liste__text--text")
    .each { |item| puts "* #{item.text.strip}" }