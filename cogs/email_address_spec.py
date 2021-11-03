"""
    This file contains several methods to manage configured email address.
    User can configure, update, view, and delete email address whenever required.
    The configured email address is used to mail attachments and remainders.
"""
import os
import re
import json

from discord.ext import commands


class EmailAddressCRUD(commands.Cog):
    """
        EmailAddressCRUD class provides various CRUD methods to manage email addresses of users.
    """

    def __init__(self, bot):
        """
            initialize
        """
        self.bot = bot
        self.email_list = None
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(cur_dir)
        with open("data/email/emails.json", "r", encoding='utf-8') as file:
            self.email_list = json.load(file)

    # ----------------------------------------------------------------------------------------------
    #    Function: add_email_address(self, ctx, email_address: str)
    #    Description: Configures the specified email address to json.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - email_address: email address specified by the author
    #    Outputs: returns either an error stating a reason for failure or returns a success message
    #          indicating that the specified email address has been added
    # ----------------------------------------------------------------------------------------------
    @commands.command(name="add_email",
                      help="add email address to receive notifications and files,"
                           " ex. $add_email no-reply@example.com")
    async def add_email_address(self, ctx, email_address: str):
        """
            Configures the specified email address to json.

            Parameters:
                ctx: used to access the values passed through the current context
                email_address: email address specified by the author

            Returns:
                returns either an error stating a reason for failure or returns a success message
                indicating that the specified email address has been added.

        """
        author = ctx.message.author

        if not EmailAddressCRUD.validate_email_address(email_address):
            await ctx.send("Enter a valid Email Address..!")
            return

        if not self.email_list:
            with open("data/email/emails.json", "r", encoding='utf-8') as file:
                self.email_list = json.load(file)

        if str(author.id) in self.email_list.keys():
            await ctx.send(
                "There is already an email address configured, "
                "Please use update command to update it..!")
            return
        else:
            self.email_list[str(author.id)] = email_address
            with open("data/email/emails.json", "w", encoding='utf-8') as file:
                json.dump(self.email_list, file)
            await ctx.send("Email address has been configured successfully..!")

    @add_email_address.error
    async def add_email_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the add_email command, do: $add_email email_address'
                '\n ( For example: $add_email no-reply@example.com)')

    # ----------------------------------------------------------------------------------------------
    #    Function: view_email_address(self, ctx)
    #    Description: displays the configured email address of user.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    Outputs: returns either an error stating a reason for failure or returns a configured email
    #    address.
    # ----------------------------------------------------------------------------------------------
    @commands.command(name="view_email",
                      help="displays the configured email address of an user, ex. "
                           "$view_email no-reply@example.com")
    async def view_email_address(self, ctx):
        """
            Displays the configured email address of user.

            Parameters:
                ctx: used to access the values passed through the current context

            Returns:
                returns either an error stating a reason for failure or returns a configured email
                address.

        """
        author = ctx.message.author

        if not self.email_list:
            with open("data/email/emails.json", "r", encoding='utf-8') as file:
                self.email_list = json.load(file)

        if str(author.id) in self.email_list:
            await ctx.send(
                "currently configured email address:{}".format(self.email_list[str(author.id)]))
        else:
            await ctx.send("There is no email address configured..!")
            return

    # ----------------------------------------------------------------------------------------------
    #    Function: update_email_address(self, ctx, email_address: str)
    #    Description: Updates the configured email address in json with the specified one.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor.
    #    - ctx: used to access the values passed through the current context.
    #    - email_address: email address specified by the author.
    #    Outputs: returns either an error stating a reason for failure or returns a success message
    #          indicating that the specified email address has been updated.
    # ----------------------------------------------------------------------------------------------
    @commands.command(name="update_email",
                      help="update email address of an user,ex. $update_email no-reply@example.com")
    async def update_email_address(self, ctx, email_address: str):
        """
            Updates the configured email address in json with the specified one.

            Parameters:
                ctx: used to access the values passed through the current context
                email_address: email address specified by the author

            Returns:
                returns either an error stating a reason for failure or returns a success message
                indicating that the specified email address has been added.

        """
        author = ctx.message.author

        if not EmailAddressCRUD.validate_email_address(email_address):
            await ctx.send("Enter a valid Email Address..!")
            return

        if not self.email_list:
            with open("data/email/emails.json", "r", encoding='utf-8') as file:
                self.email_list = json.load(file)

        if str(author.id) in self.email_list:
            self.email_list[str(author.id)] = email_address
            with open("data/email/emails.json", "w", encoding='utf-8') as file:
                json.dump(self.email_list, file)
            await ctx.send("Email address has been updated successfully..!")
        else:
            await ctx.send("There is no email address configured, "
                           "Please use add command to add one..!")
            return

    @update_email_address.error
    async def update_email_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the update_email command, do: $update_email email_address'
                '\n ( For example: $update_email no-reply@example.com)')

    # ----------------------------------------------------------------------------------------------
    #    Function: delete_email_address(self, ctx)
    #    Description: Deletes the configured email address in json.
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor.
    #    - ctx: used to access the values passed through the current context.
    #    Outputs: returns either an error stating a reason for failure or returns a success message
    #          indicating that the specified email address has been deleted.
    # ----------------------------------------------------------------------------------------------
    @commands.command(name="delete_email",
                      help="delete email address of an user,ex. $delete_email no-reply@example.com")
    async def delete_email_address(self, ctx):
        """
            Deletes the configured email address in json.

            Parameters:
                ctx: used to access the values passed through the current context

            Returns:
                returns either an error stating a reason for failure or returns a success message
                indicating that the specified email address has been deleted.

        """
        author = ctx.message.author

        if not self.email_list:
            with open("data/email/emails.json", "r", encoding='utf-8') as file:
                self.email_list = json.load(file)

        if str(author.id) in self.email_list:
            del self.email_list[str(author.id)]
            with open("data/email/emails.json", "w", encoding='utf-8') as file:
                json.dump(self.email_list, file)
            await ctx.send("Email address has been deleted successfully..!")
        else:
            await ctx.send("There is no email address configured..!")
            return

    # ----------------------------------------------------------------------------------------------
    #    Function: validate_email_address(self, ctx)
    #    Description: validates the given email address.
    #    Inputs:
    #    - email_address: email_address provided as input.
    #    Outputs: returns true if given email address is valid, false otherwise
    # ----------------------------------------------------------------------------------------------
    @staticmethod
    def validate_email_address(email_address: str):
        """
           validates the given email address.

            Parameters:
                email_address: email_address provided as input.

            Returns:
                returns true if given email address is valid, false otherwise.
        """
        email_regex = "^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$"
        if re.search(email_regex, email_address):
            return True
        return False


# -----------------------------------------------------------
# add the file to the bots' cog system
# -----------------------------------------------------------
def setup(bot):
    """
       add the file to the bots' cog system.
    """
    bot.add_cog(EmailAddressCRUD(bot))
