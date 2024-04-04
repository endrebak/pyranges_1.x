class PyRangesOptions:
    """Class to manage PyRanges options. Instantiated in pyranges_main."""

    def __init__(self) -> None:
        self.options_in_use = {
            "max_rows_to_show": (8, "the max number of rows to show in PyRanges repr"),
            "max_column_names_to_show": (
                3,
                "how many columns listed in PyRanges repr when not all fit the screen width",
            ),
        }
        self.options_default = self.options_in_use.copy()

    def set_option(self, name: str, value: int) -> None:
        """Set an option to a new value.

        Set one or more options.

        Run pyranges.options.display_options() to see available options and their current values.

        Parameters
        ----------
        name : str
            The name of the option to set.

        value : int
            The value to set the option to.

        Examples
        --------
        >>> import pyranges as pr
        >>> pr.options.set_option('max_rows_to_show', 10)


        """
        if name in self.options_in_use:
            self.options_in_use[name] = (value, self.options_in_use[name][1])
        else:
            msg = f"Option {name} not recognized."
            raise ValueError(msg)

    def get_option(self, name: str) -> int:
        """Get the value of an option.

        Parameters
        ----------
        name : str
            The name of the option to get.

        Returns
        -------
        int
            The value of the option.

        Examples
        --------
        >>> import pyranges as pr
        >>> pr.options.get_option("max_rows_to_show")
        8

        """
        if name not in self.options_in_use:
            msg = f"Option {name} not recognized."
            raise ValueError(msg)
        return self.options_in_use[name][0]

    def reset_options(self) -> None:
        """Reset all options to their default values.

        Examples
        --------
        >>> import pyranges as pr
        >>> pr.options.get_option('max_rows_to_show')
        8

        >>> pr.options.set_option('max_rows_to_show', 10)
        >>> pr.options.get_option('max_rows_to_show')
        10

        >>> pr.options.reset_options()
        >>> pr.options.get_option('max_rows_to_show')
        8

        """
        self.options_in_use = self.options_default.copy()

    def display_options(self) -> str:
        """Return a representation of the current options and their values.

        Examples
        --------
        >>> import pyranges as pr
        >>> print(pr.options.display_options())
        max_rows_to_show         : 8 (the max number of rows to show in PyRanges repr)
        max_column_names_to_show : 3 (how many columns listed in PyRanges repr when not all fit the screen width)

        """
        max_len_k = max(len(k) for k in self.options_in_use)
        max_len_v = max(len(str(v[0])) for v in self.options_in_use.values())

        return "\n".join(f"{k:<{max_len_k}} : {v[0]:>{max_len_v}} ({v[1]})" for k, v in self.options_in_use.items())

    def __repr__(self) -> str:
        return self.display_options()


options = PyRangesOptions()
