import discord
from jishaku.codeblocks import Codeblock, CodeblockConverter
from discord.ext import commands
import asyncio

class Aliases(commands.Cog):

    def __init__(self, bot, jsk):
        self.bot = bot
        self.jsk = jsk
    
    @commands.command()
    @commands.is_owner()
    async def py(self, ctx, *, argument: CodeblockConverter):
        await ctx.invoke(self.jsk.jsk_python, argument=argument)
    
    @commands.command()
    @commands.is_owner()
    async def sh(self, ctx, *, argument: CodeblockConverter):
        await ctx.invoke(self.jsk.jsk_shell, argument=argument)
    
    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx, service="selfbot"):
        service = service.lower()
        if service=="all": 
            for x in ("milan","satan","murch","selfbot"):
                message = f"service {x} restart"
                arg = Codeblock(None, message)
                await ctx.invoke(self.jsk.jsk_shell, argument=arg)
            return
        message = f"service {service} restart"
        arg = Codeblock(None, message)
        await ctx.invoke(self.jsk.jsk_shell, argument=arg)

    @commands.command()
    @commands.is_owner()
    async def update(self, ctx, *extensions):
        arg = Codeblock(None, "git pull")
        await ctx.invoke(self.jsk.jsk_shell, argument=arg)
        await asyncio.sleep(5)
        if extensions:
            await ctx.invoke(self.load, *extensions)
    
    @commands.command(aliases=["reload"])
    @commands.is_owner()
    async def load(self, ctx, *extensions):
        extensions = [f"cogs.{e}" for e in extensions if not e.startswith("cogs")]
        await ctx.invoke(self.jsk.jsk_load, *extensions)

    
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *extensions):
        extensions = [f"cogs.{e}" for e in extensions if not e.startswith("cogs")]
        await ctx.invoke(self.jsk.jsk_unload, *extensions)
        


    # @commands.command()
    # @commands.is_owner()
    # async def stop(self, ctx, service="selfbot"):
    #     service = service.lower()
    #     if service=="all": 
    #         for x in ("milan","satan","murch","selfbot"):
    #             message = f"service {x} stop"
    #             arg = Codeblock(None, message)
    #             await ctx.invoke(self.jsk.jsk_shell, argument=arg)
    #         return
    #     message = f"service {service} stop"
    #     arg = Codeblock(None, message)
    #     await ctx.invoke(self.jsk.jsk_shell, argument=arg)

    @commands.command()
    @commands.is_owner()
    async def start(self, ctx, service="selfbot"):
        service = service.lower()
        if service=="all": 
            for x in ("milan","satan","murch","selfbot"):
                message = f"service {x} start"
                arg = Codeblock(None, message)
                await ctx.invoke(self.jsk.jsk_shell, argument=arg)
            return
        message = f"service {service} start"
        arg = Codeblock(None, message)
        await ctx.invoke(self.jsk.jsk_shell, argument=arg)