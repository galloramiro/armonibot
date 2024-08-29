# ArmoniBot
The main idea of this repo it's to learn a little bit more about music theory around the harmonica instrument. 
This would also be use as an example on a talk about how to develop an idea from scratch to production.


## How to use this
1. Run `make build` to have a base image
2. Replace all the "armoni-bot" with the correct values.
3. Add dependencies to the `pyproject.toml`
4. Run `make lock-dependencies` to re build the image
5. Yoy can use the `make terminal` to use a terminal inside the container
6. Create your own `.env` using the `.env.example` as a base 


## Testing and lint
- `make test` would run all the test on the tests folder
- `make debug test_dir=tests/{file_name}::{test_name}` would allow you to run specific test or files with test
- `make lint` would run `pylint` to find improvements on your code
- `make black` to run `black` and formate your code
