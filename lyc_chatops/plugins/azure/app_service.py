from errbot import BotPlugin, botcmd


class AppService(BotPlugin):
    @botcmd
    def health(self, msg, args):
        """
        a command callable with !health
        """

        return "It *works*!"

    @botcmd
    def unhealth(self, msg, args):
        """
        a command callable with !health
        """

        return "It NOTad 22 *works*!"
