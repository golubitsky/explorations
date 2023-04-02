Following https://www.linkedin.com/pulse/coding-challenge-3-john-crickett

### Run tests

```
bundle install

# watch for changes and run when needed; press Enter to run all tests
bundle exec guard --clear

# run all tests once
bundle exec rspec
```

### Run program

#### Encode/compress file

```
ruby compression.rb --encode spec/data/135-0.txt
```

#### Decode file

```
ruby compression.rb --decode spec/data/135-0.txt-encoded spec/data/135-0.txt-table
```

### How much compression is achieved?

```
$ ruby compression.rb --encode spec/data/135-0.txt
encoded spec/data/135-0.txt to spec/data/135-0.txt-encoded
stored decoding table at spec/data/135-0.txt-table

$ ruby compression.rb --decode spec/data/135-0.txt-encoded spec/data/135-0.txt-table
decoded spec/data/135-0.txt-encoded to spec/data/135-0.txt-encoded-decoded

# no diff between decoded and original files
$ diff spec/data/135-0.txt-encoded-decoded spec/data/135-0.txt

# about 43% reduction in file size of Les Miserables test input
$ ls -l spec/data
total 16928
-rw-r--r--  1 mgolubitsky  staff  3369045 Jul 20  2021 135-0.txt
-rw-r--r--  1 mgolubitsky  staff  1919764 Apr  2 18:37 135-0.txt-encoded
-rw-r--r--  1 mgolubitsky  staff  3369045 Apr  2 18:38 135-0.txt-encoded-decoded
-rw-r--r--  1 mgolubitsky  staff     2583 Apr  2 18:37 135-0.txt-table
```
