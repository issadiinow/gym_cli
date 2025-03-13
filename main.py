import click
from colorama import Fore, Style
from database import SessionLocal
from models import User, Workout

# Create a new database session
session = SessionLocal()

@click.group()
def cli():
    """Gym Not Jim - A CLI Fitness Tracker"""
    pass

@click.command()
@click.option('--name', prompt="Enter your name", help="User's name")
def add_user(name):
    """Add a new user to the fitness tracker."""
    user = User(name=name)
    session.add(user)
    session.commit()
    click.echo(Fore.GREEN + f"User '{name}' added successfully!" + Style.RESET_ALL)

@click.command()
@click.option('--user_id', type=int, prompt="Enter User ID", help="User ID")
@click.option('--title', prompt="Workout Title", help="Workout title")
@click.option('--category', prompt="Workout Category (e.g., Chest, Back, Legs)", help="Workout category")
def add_workout(user_id, title, category):
    """Add a workout for a user."""
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        click.echo(Fore.RED + "Error: User not found!" + Style.RESET_ALL)
        return

    workout = Workout(exercise=title, category=category, user_id=user_id)  # ✅ Fixed
    session.add(workout)
    session.commit()
    click.echo(Fore.GREEN + f"Workout '{title}' added for user {user.name}!" + Style.RESET_ALL)

@click.command()
def list_users():
    """List all users."""
    users = session.query(User).all()
    if not users:
        click.echo(Fore.YELLOW + "No users found." + Style.RESET_ALL)
        return

    click.echo(Fore.CYAN + "Users:" + Style.RESET_ALL)
    for user in users:
        click.echo(f"- ID: {user.id}, Name: {user.name}")

@click.command()
@click.option('--user_id', type=int, prompt="Enter User ID", help="User ID")
def list_workouts(user_id):
    """List workouts for a specific user."""
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        click.echo(Fore.RED + "Error: User not found!" + Style.RESET_ALL)
        return

    workouts = session.query(Workout).filter_by(user_id=user_id).all()
    if not workouts:
        click.echo(Fore.YELLOW + "No workouts found for this user." + Style.RESET_ALL)
        return

    click.echo(Fore.CYAN + f"Workouts for {user.name}:" + Style.RESET_ALL)
    for workout in workouts:
        click.echo(f"- ID: {workout.id}, Exercise: {workout.exercise}, Category: {workout.category}")

@click.command()
@click.option('--id', type=int, prompt="Enter Workout ID", help="Workout ID")
@click.option('--title', prompt="New Workout Title", help="New workout title")
@click.option('--category', prompt="New Workout Category", help="New workout category")
def update_workout(id, title, category):
    """Update a workout."""
    workout = session.query(Workout).filter_by(id=id).first()
    if not workout:
        click.echo(Fore.RED + "Error: Workout not found!" + Style.RESET_ALL)
        return

    workout.exercise = title  # ✅ Fixed attribute
    workout.category = category
    session.commit()
    click.echo(Fore.GREEN + f"Workout '{title}' updated successfully!" + Style.RESET_ALL)

@click.command()
@click.option('--id', type=int, prompt="Enter Workout ID", help="Workout ID")
def delete_workout(id):
    """Delete a workout."""
    workout = session.query(Workout).filter_by(id=id).first()
    if not workout:
        click.echo(Fore.RED + "Error: Workout not found!" + Style.RESET_ALL)
        return

    session.delete(workout)
    session.commit()
    click.echo(Fore.GREEN + f"Workout ID {id} deleted successfully!" + Style.RESET_ALL)

# Add all commands to the CLI group
cli.add_command(add_user)
cli.add_command(add_workout)
cli.add_command(list_users)
cli.add_command(list_workouts)
cli.add_command(update_workout)
cli.add_command(delete_workout)

if __name__ == "__main__":
    cli()
