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
            click.secho(str(i) + '. ' + items[i-1].title, fg="yellow", bold=True)
            click.secho(items[i-1].url + "\n", fg="green", bold=True)

    elif search:
        click.secho("Search results based on your keyword \"" + search + "\": \n", fg="green", bold=True)
        items = t.search(search, 1, 10)
        if len(items) == 0:
            click.secho("*No result returned. Please try another keyword*", fg="red", bold=True)
            return
        for i in range(1, 1+len(items)):
            #click.secho(str(i) + '. ' + str(items[i-1]), bold=True)
            click.secho(str(i) + '. ' + items[i-1].title, fg="yellow", bold=True)
            click.secho(items[i-1].url + "\n", fg="green", bold=True)

    elif topic:
        click.secho("Search result based on topic(" + topic + "):", fg="green", bold=True)
        items = t.topic(topic)
        try:
            for i in range(1, 1+len(items)):
                click.secho(str(i) + '. ' + items[i-1].title, fg="yellow", bold=True)
                click.secho(items[i-1].url + "\n", fg="green", bold=True)
        except:
            click.secho("Option: --topic Search engineering blog posts by topic (backend, frontend, mobile, design, data science, database) \n", fg="red", bold=True)
            return

    elif trending:
        items = t.trending()
        click.secho("Trending engineering posts: ",fg="green", bold=True)
        for i in range(1, 1+len(items)):
            click.secho(str(i) + '. ' + items[i-1].title, fg="yellow", bold=True)
            click.secho(items[i-1].url + "\n", fg="green", bold=True)

    else:
        click.secho("Options:\n--newest=true Find the newest engineering blog posts \n--topic=TEXT Search engineering blog posts by topic (backend, frontend, mobile, design, data science, database... \n--trending=true Find the trending engineering posts \n--search=TEXT Search engineering blog posts by keyword", fg="red", bold=True)
        return

    # prompt to choose item to read
    choice = click.prompt('Choose the item you want to read')
    choice = int(choice)
    if choice > len(items):
        click.secho("Item not exists, please select again", fg="red")
        choice = click.prompt('Choose the item you want to read\n', fg="blue")
        choice = int(choice)

    item_selected = items[choice-1]
    contents = item_selected.get_content()
    click.secho("Article chosen: ", fg="green")
    click.secho(item_selected.title + "\n", fg="green", bold=True)
    click.secho(contents)
