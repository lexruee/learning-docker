FROM ruby:2
RUN gem install nokogiri
WORKDIR /src/
COPY printheadlines.rb /src/
USER www-data
CMD ["ruby", "printheadlines.rb"]