# Creating commands

```{note}

This page is a follow-up, and the base code used is from the previous page ([Initial files](./101-initial-files.md)). The code can be found on the GitHub repository [here](https:/github.com/DisnakeDev/guide/tree/main/docs/extra-code-samples/code-intial-files).
```

Discord also allows developers to register {disdocs}`slash commands </interactions/application-commands>`, which
provides users a first-class way of interacting directly with your application. These slash commands shall be covered by
the guide [here](../200-interactions/202-application-commands.md), in the **Interactions** section.

## A note on prefix commands

Bot commands that are initiated when a keyword is used along with a specified prefix (such as `!` or `$`) are known as
**prefix commands** (are also often referred to as **text commands**).

```{warning} Message Intent - Privileged

It is to be noted that handling prefix commands require the **message intent**, which allows the bot to get content and data of messages sent by users. This intent has recently been privileged, i.e., it needs to be manually enabled for the bot application, and its requirement will eventually be reviewed if your bot is in over 100 servers.

You can read more about the message intent [here][message-intent-article].
```

Therefore, to minimize the permissions your bot has to use, we will be covering prefix commands under the **Popular
Topics** section, and advancing with the basics of slash commands in this article; more advanced topics of the same will
be covered in the [**Interactions**](../200-interactions/202-application-commands.md) section.

## Registering commands

This section covers the bare minimum to get you started with registering slash commands. Once again, you can refer to
[this page](../200-interactions/202-application-commands.md) for an in-depth coverage of topics, including guild
commands, global commands, options, option types, autocomplete and choices.

Now, we shall continue with the base code used in the previous section.

```python linenums="1" title="main.py"
import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


bot.run("YOUR_BOT_TOKEN")
```

The first step is to use the {py:meth}`@bot.slash_command <disnake.ext.commands.Bot.slash_command>` coroutine, along
with an async function in order to define the code for your slash command. Below is a script demonstrating the same
(focus on the use of `inter`, which is short for `interaction`).

```python linenums="1" title="main.py" hl_lines="12-14"
import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command()
async def ping(inter):
    ...


bot.run("YOUR_BOT_TOKEN")
```

The `inter` passed into the function is analogous to context, or `ctx` used in prefix commands - it passes through all
information relative to the interaction - data regarding the user who initiated the command, as an example. It is also
necessary for replying to the use of the command.

<!-- prettier-ignore -->
:::{admonition} Using `ctx` vs. `inter`
If you have experience with coding bots with {dpydocs}`discord.py </>`, you would be familiar with using `ctx` as an
abbreviation for passing context into the function. This guide will primarily be using `inter`, as it is short for
`interaction` and refers to {py:class}`disnake.ApplicationCommandInteraction`. Of course, you're open to using your
preferred abbreviation in code.
:::

### Registering commands in specific guilds

Note that servers are referred to as "guilds" in the Discord API and disnake library. On running the above code, the
slash command will be registered globally, and will be accessible on all servers the bot is in. The caveat being that
global registration of slash commands can take up to 1 hour (refer to
{disdocs}`Discord's documentation </interactions/application-commands#create-global-application-command>`.

When you're trying to test your changes to code in real time, it can be immensely useful to have the command's function
update with your code changes right away. Thus, you can use the `guild_ids` argument for the command to be
instantaneously registered in a list of specified servers. (We recommend including your separate development server in
this list.)

```python linenums="1" title="main.py" hl_lines="12-14"
import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command(guild_ids=[1234, 5678])  # Your server IDs go here.
async def ping(inter):
    ...


bot.run("YOUR_BOT_TOKEN")
```

<!-- prettier-ignore -->
:::{admonition} Using `test_guilds` in `commands.Bot()`

When you have multiple commands registered under the same test guilds, it is convenient to only have your `guild_ids`
defined once. Therefore, you can use the `test_guilds` argument in the `commands.Bot()` instance instead of passing
`guild_ids` to every single command -

```python
bot = commands.Bot(test_guilds=[1234, 5678])
```

:::

Now that you're all set with registering the slash command, you can proceed with responding to the initiated command.

## Responding to commands

You can respond to a slash command initiated by the user, using `inter.response.send_message()`. It is analogous to
using `ctx.send()`, in that you can respond to the interaction with embeds, files, buttons/select menus or just plain
text.

```python linenums="1" title="main.py" hl_lines="14"
import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command(guild_ids=[1234, 5678])
async def ping(inter):
    await inter.response.send_message("Pong!")


bot.run("YOUR_BOT_TOKEN")
```

```{image} /assets/img-creating-commands/001.png
:width: 60%
```

### Server info command

`inter.guild` refers to the guild the interaction was sent in (a {py:class}`disnake.Guild`), which exposes properties
such as `.name` or `.member_count`.

```python linenums="1" title="main.py" hl_lines="12-16"
import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command()
async def server(inter):
    await inter.response.send_message(
        f"Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}"
    )


bot.run("YOUR_BOT_TOKEN")
```

```{image} /assets/img-creating-commands/002.png
:width: 60%
```

```{tip}
Refer to the {py:class}`disnake.Guild` documentation for a list of all the available properties and methods.
```

You could also display the date the server was created, or the server's verification level. You would do those in the
same manner - use `inter.guild.created_at` or `inter.guild.verification_level`, respectively.

### User info command

A "user" refers to a Discord user. `inter.author` refers to the user the interaction was sent by (a
{py:class}`disnake.User` in DM contexts, or a {py:class}`disnake.Member`) in server contexts), which exposes properties
such as `.name` or `.id`. (Using just `inter.author` will give the user's full tag.)

```python linenums="1" title="main.py" hl_lines="12-14"
import disnake
from disnake.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command()
async def user(inter):
    await inter.response.send_message(f"Your tag: {inter.author}\nYour ID: {inter.author.id}")


bot.run("YOUR_BOT_TOKEN")
```

```{image} /assets/img-creating-commands/003.png
:width: 60%
```

```{tip}
Refer to the {py:class}`disnake.User` and {py:class}`disnake.Member` documentation for a list of all the available properties and methods.
```

And there you have it!

## Resulting Code

If you want to compare your code to the code we've constructed so far, you can review it over on the GitHub repository
[here](https:/github.com/DisnakeDev/guide/tree/main/docs/extra-code-samples/code-creating-commands).

[message-intent-article]: https://support-dev.discord.com/hc/en-us/articles/4404772028055
