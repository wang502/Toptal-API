from Toptal import Toptal, Item, Freelencer
import click

@click.command()
@click.option('--newest', help='Find the newest engineering blog posts')
@click.option('--topic', help='Search engineering blog posts by topic (backend, frontend, mobile, design, data science, database...)')
@click.option('--trending', help='Find the trending engineering posts')
@click.option('--search', help='Search engineering blog posts by keyword')
def main(newest, topic, trending, search):
    t = Toptal()
    items = []

    if newest:
        items = t.newest()
        click.secho("Newest engineering posts:", fg="green", bold=True)
        for i in range(1, 1+len(items)):
            click.secho(str(i) + '. ' + str(items[i-1]), bold=True)

    elif search:
        click.secho("Search results based on your keyword(" + search + "):", fg="green", bold=True)
        items = t.search(search, 1, 10)
        for i in range(1, 1+len(items)):
            click.secho(str(i) + '. ' + str(items[i-1]), bold=True)

    elif topic:
        click.secho("Search result based on topic(" + topic + "):", fg="green", bold=True)
        items = t.topic(topic)
        for i in range(1, 1+len(items)):
            click.secho(str(i) + '. ' + str(items[i-1]), bold=True)

    elif trending:
        items = t.trending()
        click.secho("Trending engineering posts: ",fg="green", bold=True)
        for i in range(1, 1+len(items)):
            click.secho(str(i) + '. ' + str(items[i-1]), bold=True)

    else:
        click.echo("Options:\n--newest Find the newest engineering blog posts \n--topic Search engineering blog posts by topic (backend, frontend, mobile, design, data science, database... \n--trending Find the trending engineering posts \n--search Search engineering blog posts by keyword", fg="red", bold=True)
        return

    # prompt to choose item to read
    choice = click.prompt('Choose the item you want to read')
    choice = int(choice)
    if choice > len(items):
        click.secho("Item not exists, please select again", fg="red")
        choice = click.prompt('Choose the item you want to read')
        choice = int(choice)

    item_selected = items[choice-1]
    contents = item_selected.get_content()
    click.secho("Reading starts from here: \n", fg="green", bold=True)
    click.secho("            " + item_selected.title, fg="green", bold=True)
    click.secho(contents, fg="green", bold=True)
