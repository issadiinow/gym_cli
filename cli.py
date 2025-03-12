# import click
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# from models import User, Workout

# @click.group()
# def cli():
#     """Gym Not Jim CLI - Track your workouts"""
#     pass

# @click.command()
# @click.argument('name')
# def add_user(name):
#     """Add a new user"""
#     session = SessionLocal()
#     user = User(name=name)
#     session.add(user)
#     session.commit()
#     session.close()
#     click.echo(f"User {name} added.")

# @click.command()
# @click.argument('user_id', type=int)
# @click.argument('exercise')
# @click.argument('category')
# def add_workout(user_id, exercise, category):
#     """Add a workout for a user"""
#     session = SessionLocal()
#     workout = Workout(user_id=user_id, exercise=exercise, category=category)
#     session.add(workout)
#     session.commit()
#     session.close()
#     click.echo(f"Workout {exercise} added to user {user_id}.")

# @click.command()
# def list_users():
#     """List all users"""
#     session = SessionLocal()
#     users = session.query(User).all()
#     for user in users:
#         click.echo(f"{user.id}: {user.name}")
#     session.close()

# @click.command()
# @click.argument('user_id', type=int)
# def list_workouts(user_id):
#     """List all workouts for a user"""
#     session = SessionLocal()
#     workouts = session.query(Workout).filter(Workout.user_id == user_id).all()
#     for workout in workouts:
#         click.echo(f"{workout.id}: {workout.exercise} - {workout.category}")
#     session.close()

# cli.add_command(add_user)
# cli.add_command(add_workout)
# cli.add_command(list_users)
# cli.add_command(list_workouts)

# if __name__ == "__main__":
#     cli()
