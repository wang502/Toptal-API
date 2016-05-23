from Toptal import Toptal, Item, Freelencer

@click.command()
@click.option('--newest', default=1, prompt='Find the newest engineering blog posts')
@click.option('--search', prompt='Search engineering blog posts by keyword')
@click.option('--topic', prompt='Search engineering blog posts by topic (backend, frontend, mobile, design, data science, database...)')
@click.option('--trending', default=1, prompt='Find the trending engineering posts')
def main(newest, search, topic, trending):
    t = Toptal()
    if newest:
        items = t.newest()
        for i in range(1, 1+len(items)):
            click.echo(str(i) + '. ' + items[i-1])
    elif search:
        items = t.search(search, 1, 10)
        for i in range(1, 1+len(items)):
            click.echo(str(i) + '. ' + items[i-1])
    elif topic:
        items = t.topic(topic)
        for i in range(1, 1+len(items)):
            click.echo(str(i) + '. ' + items[i-1])
    elif trending:
        items = t.trending()
        for i in range(1, 1+len(items)):
            click.echo(str(i) + '. ' + items[i-1])
    else:
        click.echo()
