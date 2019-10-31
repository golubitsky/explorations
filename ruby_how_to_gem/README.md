Execute all commands below in directory of this file.

# Goals

## Spin up a local gem server

- https://hub.docker.com/r/spoonest/geminabox

```sh
# Each of the below commands will spin this up automatically. But here's a command to spin it up:
docker-compose run --rm --service-ports server
open http://localhost:9292/
```

It stores all uploaded gems in a Docker volume.

## Package a gem

Output of this step used in next step.

```sh
docker-compose run --rm build-gem
```

### Research

- https://guides.rubygems.org/make-your-own-gem/
- `gem build hola.gemspec`
  - Outputs `.gem` file in same dir.

## Upload the gem to the gem server

```sh
docker-compose run --rm upload
```

## Consume the gem in an application

```sh
docker-compose run --rm app
```
