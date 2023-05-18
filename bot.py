import hikari
from hikari import PermissionOverwrite, PermissionOverwriteType, Permissions, snowflakes
import lightbulb

token = "BOT TOKEN"
guild_id = SERVER ID

bot = lightbulb.BotApp(
    token=token, default_enabled_guilds=(guild_id), intents=hikari.Intents.ALL
)


@bot.command
@lightbulb.command("create-channel", "Create a channel only for you and select people")
@lightbulb.implements(lightbulb.SlashCommand)
async def creatchannel(ctx: lightbulb.Context):
    channels_view = ctx.app.cache.get_guild_channels_view_for_guild(guild_id)
    channels = channels_view.values()

    guild_category_name = f"{ctx.member.display_name}'s Channels"

    for channel in channels:
        if channel.name == guild_category_name:
            await ctx.respond(f"Catergory <#{channel.id}> already exists!")
            return

    overwrite = PermissionOverwrite(
        id=ctx.member.id,
        type=PermissionOverwriteType.MEMBER,
        allow=(
            Permissions.VIEW_CHANNEL
            | Permissions.READ_MESSAGE_HISTORY
            | Permissions.SEND_MESSAGES
            | Permissions.SPEAK
        ),
        deny=(Permissions.MANAGE_MESSAGES),
    )

    overwrite2 = PermissionOverwrite(
        id=guild_id,
        type=PermissionOverwriteType.ROLE,
        deny=(
            Permissions.VIEW_CHANNEL
            | Permissions.READ_MESSAGE_HISTORY
            | Permissions.SEND_MESSAGES
        ),
    )

    category = await bot.rest.create_guild_category(
        guild=guild_id,
        name=guild_category_name,
        permission_overwrites=(overwrite, overwrite2),
    )
    channel = await bot.rest.create_guild_text_channel(
        guild=guild_id,
        name=f"{ctx.member.display_name}'s Text Channel",
        category=category,
    )
    vc = await bot.rest.create_guild_voice_channel(
        guild=guild_id,
        name=f"{ctx.member.display_name}'s Voice Channel",
        category=category,
    )

    category
    channel
    vc
    await ctx.respond(f"Catergory <#{channel.id}> Created!")


@bot.command()
@lightbulb.option("member", "the specified member", type=hikari.Member)
@lightbulb.command("add-member", "Add a member to your channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context):
    channels_view = ctx.app.cache.get_guild_channels_view_for_guild(guild_id)
    channels = channels_view.values()
    guild_category_name = f"{ctx.member.display_name}'s Channels"
    guild_channel_name = f"{ctx.member.display_name.lower()}s-text-channel"
    guild_vc_name = f"{ctx.member.display_name}'s Voice Channel"

    for channel in channels:
        if channel.name == guild_channel_name:
            overwrite = PermissionOverwrite(
                id=ctx.options.member.id,
                type=PermissionOverwriteType.MEMBER,
                allow=(
                    Permissions.VIEW_CHANNEL
                    | Permissions.READ_MESSAGE_HISTORY
                    | Permissions.SEND_MESSAGES
                    | Permissions.SPEAK
                ),
                deny=(Permissions.MANAGE_MESSAGES),
            )
            original_permission_overwrites = channel.permission_overwrites
            original_permission_overwrites = original_permission_overwrites.values()
            original_permission_overwrites = tuple(original_permission_overwrites)
            new_permission_overwrites = original_permission_overwrites + (
                overwrite,
            )

            await channel.edit(permission_overwrites=new_permission_overwrites)
    for channel in channels:
        if channel.name == guild_vc_name:
            overwrite = PermissionOverwrite(
                id=ctx.options.member.id,
                type=PermissionOverwriteType.MEMBER,
                allow=(
                    Permissions.VIEW_CHANNEL
                    | Permissions.READ_MESSAGE_HISTORY
                    | Permissions.SEND_MESSAGES
                    | Permissions.SPEAK
                ),
                deny=(Permissions.MANAGE_MESSAGES),
            )
            original_permission_overwrites = channel.permission_overwrites
            original_permission_overwrites = original_permission_overwrites.values()
            original_permission_overwrites = tuple(original_permission_overwrites)
            new_permission_overwrites = original_permission_overwrites + (
                overwrite,
            )

            await channel.edit(permission_overwrites=new_permission_overwrites)

    for channel in channels:
        if channel.name == guild_category_name:
            overwrite = PermissionOverwrite(
                id=ctx.options.member.id,
                type=PermissionOverwriteType.MEMBER,
                allow=(
                    Permissions.VIEW_CHANNEL
                    | Permissions.READ_MESSAGE_HISTORY
                    | Permissions.SEND_MESSAGES
                    | Permissions.SPEAK
                ),
                deny=(Permissions.MANAGE_MESSAGES),
            )
            original_permission_overwrites = channel.permission_overwrites
            original_permission_overwrites = original_permission_overwrites.values()
            original_permission_overwrites = tuple(original_permission_overwrites)
            new_permission_overwrites = original_permission_overwrites + (
                overwrite,
            )

            await channel.edit(permission_overwrites=new_permission_overwrites)
            await ctx.respond(
                f"Added {ctx.options.member.display_name} to {channel.name}"
            )
            return
    await ctx.respond("You dont own a channel yet!")


@bot.command()
@lightbulb.option("member", "the specified member", type=hikari.Member)
@lightbulb.command("remove-member", "Remove a member from your channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def removemember(ctx: lightbulb.Context):
    channels_view = ctx.app.cache.get_guild_channels_view_for_guild(guild_id)
    channels = channels_view.values()
    guild_category_name = f"{ctx.member.display_name}'s Channels"
    guild_channel_name = f"{ctx.member.display_name.lower()}s-text-channel"
    guild_vc_name = f"{ctx.member.display_name}'s Voice Channel"

    for channel in channels:
        if channel.name == guild_channel_name:
            overwrite = PermissionOverwrite(
                id=ctx.options.member.id,
                type=PermissionOverwriteType.MEMBER,
                deny=(
                    Permissions.MANAGE_MESSAGES
                    | Permissions.VIEW_CHANNEL
                    | Permissions.READ_MESSAGE_HISTORY
                    | Permissions.SEND_MESSAGES
                    | Permissions.SPEAK
                ),
            )
            original_permission_overwrites = channel.permission_overwrites
            original_permission_overwrites = original_permission_overwrites.values()
            original_permission_overwrites = tuple(original_permission_overwrites)
            new_permission_overwrites = original_permission_overwrites + (
                overwrite,
            )

            await channel.edit(permission_overwrites=new_permission_overwrites)

    for channel in channels:
        if channel.name == guild_vc_name:
            overwrite = PermissionOverwrite(
                id=ctx.options.member.id,
                type=PermissionOverwriteType.MEMBER,
                deny=(
                    Permissions.MANAGE_MESSAGES
                    | Permissions.VIEW_CHANNEL
                    | Permissions.READ_MESSAGE_HISTORY
                    | Permissions.SEND_MESSAGES
                    | Permissions.SPEAK
                ),
            )
            original_permission_overwrites = channel.permission_overwrites
            original_permission_overwrites = original_permission_overwrites.values()
            original_permission_overwrites = tuple(original_permission_overwrites)
            new_permission_overwrites = original_permission_overwrites + (
                overwrite,
            )

            await channel.edit(permission_overwrites=new_permission_overwrites)

    for channel in channels:
        if channel.name == guild_category_name:
            overwrite = PermissionOverwrite(
                id=ctx.options.member.id,
                type=PermissionOverwriteType.MEMBER,
                deny=(
                    Permissions.MANAGE_MESSAGES
                    | Permissions.VIEW_CHANNEL
                    | Permissions.READ_MESSAGE_HISTORY
                    | Permissions.SEND_MESSAGES
                    | Permissions.SPEAK
                ),
            )
            original_permission_overwrites = channel.permission_overwrites
            original_permission_overwrites = original_permission_overwrites.values()
            original_permission_overwrites = tuple(original_permission_overwrites)
            new_permission_overwrites = original_permission_overwrites + (
                overwrite,
            )

            await channel.edit(permission_overwrites=new_permission_overwrites)
            await ctx.respond(
                f"Removed {ctx.options.member.display_name} to {channel.name}"
            )
            return
    await ctx.respond("You dont own a channel yet!")

@bot.command()
@lightbulb.command("remove-channel", "delete your channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def removechannel(ctx: lightbulb.Context):
    channels_view = ctx.app.cache.get_guild_channels_view_for_guild(guild_id)
    channels = channels_view.values()
    guild_vc_name = f"{ctx.member.display_name}'s Voice Channel"
    guild_channel_name = f"{ctx.member.display_name.lower()}s-text-channel"
    guild_category_name = f"{ctx.member.display_name}'s Channels"
    for channel in channels:
        if channel.name == guild_vc_name:
            await bot.rest.delete_channel(channel)
    for channel in channels:
        if channel.name == guild_channel_name:
            await bot.rest.delete_channel(channel)
    for channel in channels:
        if channel.name == guild_category_name:
            await bot.rest.delete_channel(channel)
            await ctx.respond(f"Deleted {channel.name}")
            return
    await ctx.respond("You dont own a channel yet!")
    
@bot.command()
@lightbulb.command("help", "how to use the bot")
async def help(ctx):
    ctx.respond("Use /create-channel to create a category, use /remove-channel to remove the category, use /add-member to add a memberto it and use /remove-member to remove a member\n\n this bot was made using hikari and developed by RavenVR#6650.")

bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="/create-channel",
        type=hikari.ActivityType.WATCHING,
    ),
)
