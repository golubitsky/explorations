FROM node:10

RUN yarn global add elm@0.19.0-bugfix6
RUN yarn global add elm-test@0.19.0-beta11
RUN yarn global add elm elm-live

RUN mkdir /src
WORKDIR /src
COPY entrypoint.sh .

ENTRYPOINT [ "./entrypoint.sh" ]