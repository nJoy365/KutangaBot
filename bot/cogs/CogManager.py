from discord.ext import commands
import os


class CogManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def load_cogs(self):
        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                if f[:-3] not in self.bot.cogs:
                    if not f[:-3].startswith("_") and f[:-3].endswith("Cog"):
                        await self.bot.load_extension(f"cogs.{f[:-3]}")
                        await self.bot.logger.info(message=f"Loaded cog {f[:-3]}")

    @commands.Cog.listener()
    async def on_cog_load(self, cog: commands.Cog):
        await self.bot.logger.info(message=f"{cog.qualified_name} cog loaded")

    @commands.Cog.listener()
    async def on_cog_unload(self, cog: commands.Cog):
        await self.bot.logger.info(message=f"{cog.qualified_name} cog unloaded")

    @commands.group(name="cog", invoke_without_command=True)
    async def cog(self, ctx: commands.Context):
        """Cog management commands"""
        await ctx.send_help(self.cog)

    @cog.command("load", description="Load a cog")
    async def load_cog(self, ctx: commands.Context, *, cog_name: str):
        await self.bot.load_extension(f"cogs.{cog_name}")
        await self.bot.logger.log(ctx=ctx, message=f"Loaded {cog_name}")

    @cog.command("unload", description="Unload a cog")
    async def unload_cog(self, ctx: commands.Context, *, cog_name: str):
        await self.bot.unload_extension(f"cogs.{cog_name}")
        await self.bot.logger.log(ctx=ctx, message=f"Unloaded {cog_name}")

    @cog.command("reload", description="Reload a cog")
    async def reload_cog(self, ctx: commands.Context, *, cog_name: str):
        if cog_name.lower() == "all":
            cogs = [key for key in self.bot.cogs.keys()]
            done = []
            for cog in cogs:
                if cog not in done and cog != "CogManager":
                    await self.bot.reload_extension(f"cogs.{cog}")
                    done.append(cog)
            await self.bot.logger.log(
                ctx=ctx, message=f"Reloaded cogs: {', '.join(done)}"
            )
        else:
            await self.bot.reload_extension(f"cogs.{cog_name}")
            await self.bot.logger.log(ctx=ctx, message=f"Reloaded {cog_name}")

    @cog.command("list", description="List all cogs")
    async def list_cogs(self, ctx: commands.Context):
        await ctx.send(f"Cogs: {', '.join(self.bot.cogs)}")


async def setup(bot):
    await bot.add_cog(CogManager(bot))
    await bot.cogs["CogManager"].load_cogs()
