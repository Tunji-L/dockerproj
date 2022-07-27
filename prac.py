#!usr/bin/env python
import click

@click.command()
@click.option('--count', default=1, help='Number of tmes to count')
@click.option('--name', prompt='your name', help='Name of the person to greet')
def greet(name, count):
    for i in range(count):
        click.echo(f"Hello {name}")
    
if __name__ == "__main__":
    greet()