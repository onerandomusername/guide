# What are interactions?

An **Interaction** is the message that your bot receives when a user initiates an application command or a message
component.

## Interactions and Bot Users

We're all used to the way that Discord bots have worked for a long time. You make an application in
[Developer Portal](https://discord.com/developers/applications), make a new bot user, and copy the token. Interactions
bring something entirely new - the ability to interact with an application _without needing a bot user in the guild_.
Responding to the interaction doesn't require a bot token.

`disnake` is primarily focused on using the gateway events, so you still need a bot user. Check out
[`hikari-py`](https://github.com/hikari-py/hikari) with their REST-API part for this purpose.

Welcome to the new world.

## Responding to interactions

You have only 3 seconds to respond to the interaction. If do not have time to do it, Discord will shown "This
interaction failed" error.

In fact, there are 3 types of interactions:

-   {py:class}`disnake.ApplicationCommandInteraction` (for [application commands](./202-application-commands))
-   {py:class}`disnake.MessageInteraction` (for [message components](./203-message-components))
-   {py:class}`disnake.Interaction` (a base class, usually not used)

But responding is the same for both interactions types.

### `interaction.response`

{py:attr}`disnake.Interaction.response` attribute returns a {py:class}`disnake.InteractionResponse` instance that has 4
useable methods. A response can **only be done once**. If you want to send secondary messages, consider using
{py:attr}`disnake.Interaction.followup` webhook instead.

1. {py:meth}`disnake.InteractionResponse.send_message` - Sends response message
2. {py:meth}`disnake.InteractionResponse.edit_message` - Edits original message, you're unable to use this in
   application command because there are no message while you responding
3. {py:meth}`disnake.InteractionResponse.defer` - Defers the interaction
4. {py:meth}`disnake.InteractionResponse.is_done` - Indicates whether an interaction response has been done before

```{note}

{py:meth}`disnake.InteractionResponse.defer`  works differently depending on the type of interaction.
It creates *"Bot is thinking..."* message for application commands and
doesn't throw *"This interaction failed"* if you're not going to respond to message components.
```

```{note}

If you're going to run long processes (more than 3 seconds) while responding, you must first defer the interaction.
Then when your response is ready you can edit the message using {py:meth}`disnake.InteractionResponse.edit_message` method
```

```python title="example.py"
@bot.slash_command()
async def ping(inter: ApplicationCommandInteraction):
    await inter.response.send_message("Pong!")


@bot.slash_command()
async def defer(inter: ApplicationCommandInteraction):
    await inter.response.defer()
    await asyncio.sleep(10)
    await inter.edit_original_message("The wait is over, my comrades!")
```

### `interaction.followup`

Often used when you need to send secondary messages after responding.
