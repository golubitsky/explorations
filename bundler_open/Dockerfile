FROM ruby:3.0

RUN apt-get update
RUN apt-get install -y vim

COPY Gemfile .

RUN bundle install

COPY . .

ENV EDITOR vi

CMD [ "bash" ]