# Gym Not Jim - A CLI Fitness Tracker

Gym Not Jim is a command-line interface (CLI) fitness tracker built with Python and SQLAlchemy. It allows users to add, categorize, update, and delete workout routines.

## Features
- Add new users
- Add workouts for users
- List users and their workouts
- Update workout details
- Delete workouts

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/issadiinow/gym_cli.git
   cd gym_cli
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. If you don't have Alembic and Colorama installed, install them manually:
   ```sh
   pip install alembic colorama
   ```

5. Initialize the database:
   ```sh
   python database.py

   ```

## Usage

Run the CLI tool:
```sh
python main.py --help
```

### Commands:

#### Add a User:
```sh
python main.py add-user
```

#### Add a Workout:
```sh
python main.py add-workout
```

#### List Users:
```sh
python main.py list-users
```

#### List Workouts for a User:
```sh
python main.py list-workouts --user_id <USER_ID>
```

#### Update a Workout:
```sh
python main.py update-workout --id <WORKOUT_ID>
```

#### Delete a Workout:
```sh
python main.py delete-workout --id <WORKOUT_ID>
```

## Database Schema

- **Users Table**
  - `id`: Integer (Primary Key)
  - `name`: String

- **Workouts Table**
  - `id`: Integer (Primary Key)
  - `exercise`: String
  - `category`: String
  - `user_id`: Integer (Foreign Key referencing `users.id`)

## License
This project is licensed under the MIT License.

## Author
Issadiinow - [GitHub Profile](https://github.com/issadiinow)

