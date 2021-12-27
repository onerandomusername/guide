# Creating cogs/extensions

[**Cogs**](disnake:ext/commands/cogs) are analogous to modules that extend the core of the bot - thus adding to its
functions and abilities. They also allow you to break down and organize your bot's collection of commands/listeners
(which is useful when your bot's command list becomes quite extensive).

```{note}
Cogs are typically used alongside with **Extensions**. You can read more about them
[in the documentation](disnake:ext/commands/extensions).
```

## Creating files

What we code here will extend on the code from [**Initial Files**](./101-initial-files.md), and thus we assume that
there already exists a `main.py` file in your directory with initiates a
{py:class}`commands.Bot <disnake.ext.commands.Bot>` instance.

```{code-block} python
:caption: main.py
import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


bot.run("YOUR_BOT_TOKEN")
```

Next, we will create a new Python file either in the same directory as `main.py` or in a subfolder (which is
recommended). For the sake of being organized, we will create the cog file in a separate `cogs` folder, and name the
file `ping.py` just for the "ping" command. If you're strictly following the guide, your file directory should look
something like this:

```
.
├── cogs/
│   └── ping.py
├── main.py
└── secrets.env
```

## Initial code

### Inheriting a class

The first step is to create a class in `ping.py` that inherits from {py:class}`commands.Cog <disnake.ext.commands.Cog>`,
along with a constructor that takes in the bot as its only argument and saves it. This is where we will be putting in
our commands.

```{code-block} py
:caption: ping.py
from disnake.ext import commands


class PingCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
```

:::{tip}

We typehint {py:class}`commands.Bot <disnake.ext.commands.Bot>` here to give the IDE an idea of what the argument type
is. It is not necessary, but can be useful in development when adding certain arguments to your commands.

:::

### Registering commands

Now, to define a command inside the class, we will use the {py:func}`commands.command <disnake.ext.commands.command>`
decorator. It functions the same as {py:meth}`bot.command <disnake.ext.commands.Bot.command>`, but works in cogs as
well.

```{code-block} python
:emphasize-lines: 10
from disnake.ext import commands


class PingCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
```

Note that we're using `self` as the first argument, since the command function is inside a class.

### Adding `setup` function

The last thing that needs to be added to this file is a `setup` function, so that disnake can load the cog when it is
added to `main.py`.

```{code-block} py
:caption: ping.py
:emphasize-lines: 16-
from disnake.ext import commands


class PingCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))
```

This cog file can now be added to the bot via the `bot.load_extension()` method in `main.py`.

```{code-block} python
:caption: main.py
:emphasize-lines: 12

import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


bot.load_extension("cogs.ping")  # Note that we did not mention the .py extension.

bot.run("YOUR_BOT_TOKEN")
```

Note that we've input `"cogs.ping"` here, since the `ping.py` file is inside the `cogs` folder. Therefore, the basic
syntax for loading an extension is `bot.load_extension("<folder_name>.<file_name>")`.

And that concludes the use of cogs with `disnake`! You can now create multiple cogs to group and organize your
commands/events, and load/unload them via your main file. More information on special cog methods and meta options can
be found [in the documentation](disnake:ext/commands/cogs).

## Syntax changes

Cogs represent a fairly drastic change in the way you write commands and bots, so here's a list you can come back to for
the primary syntax used in cogs:

-   Each cog is a Python class that subclasses {py:class}`disnake:disnake.ext.commands.Cog`.
-   Decorators for commands in cogs:
    -   Command - {py:func}`disnake.ext.commands.command`
    -   Slash command - {py:func}`disnake.ext.commands.slash_command`
    -   User command - {py:func}`disnake.ext.commands.user_command`
    -   Message command - {py:func}`disnake.ext.commands.message_command`
-   Every listener is marked with the {py:meth}`disnake.ext.commands.Cog.listener`
-   Cogs are then registered with the {py:meth}`disnake.ext.commands.Bot.add_cog` call, and are subsequently removed
    with the {py:meth}`disnake.ext.commands.Bot.remove_cog`call.

<!-- <sup>Source: [Disnake Documentation]()</sup> -->

Cogs represent a fairly drastic change in the way you write commands and bots. Thus, it is recommended that you get
familiar with this syntax - since the code we use in this section is largely tailored for cogs.
