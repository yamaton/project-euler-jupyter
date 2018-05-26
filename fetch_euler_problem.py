from utils import scrape_project_euler as scraper

from IPython.core import magic_arguments
from IPython.core.magic import Magics, line_magic, magics_class


@magics_class
class EulerProblemMagic(Magics):
    """IPython wrapper to format cell using `https://github.com/ambv/black`."""

    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "problem_id", type=int, help="Problem ID number in Project Euler"
    )
    @line_magic
    def pe(self, line):
        """Magic command to format the IPython cell."""
        args = magic_arguments.parse_argstring(self.pe, line)
        problem_id = args.problem_id
        self.shell.set_next_input(scraper.get_formatted(problem_id), replace=True)


def load_ipython_extension(ipython):
    ipython.register_magics(EulerProblemMagic)
