what_can_we_deploy? lower_env=HEAD higher_env=sit
what_can_we_deploy? lower_env=sit higher_env=qa

inputs

- higher env image tag (short git SHA) per service
- lower env image tag (short git SHA) per service
- temp dir
  - clone || pull master of each repo

service a-special (repo a)
service b (repo b)

for service a-special you can deploy commit acddef to prod to release:

1. feature a (these are just commit messages)
2. feature b

would you like to make it so? y/N

# motivations

## the usual

## shared services (antipattern)

# what can we deploy

# better solutions – continuous delivery?
