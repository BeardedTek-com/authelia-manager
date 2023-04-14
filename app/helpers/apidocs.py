class apidocs:
    def __init__(self) -> None:
        """
        This is where we document all the api calls.
        """
        self.contents = {
            "API Documentation":{
                "/"                                 : "[GET]  Informational page",
                "/ui"                               : "[GET]  UI entrypoint",
                "/ui/login"                         : "[GET]  User login form",
                "/api"                              : "[GET]  API information",
                "/api/docs"                         : "[GET]  Main documentation (This may change to ui)",
                "/api/initdb"                       : "[GET]  Initialize database",
                "/api/config"                       : "[GET]  Returns config data in JSON",
                "/api/config/post"                  : "[POST] Processes updated config data",
                "/api/user"                         : "[GET]  Returns user data in JSON",
                "/api/user/post"                    : "[POST] Processes updated user data",
                "/api/group"                        : "[GET]  Returns Group Data in JSON",
                "/api/group/post"                   : "[POST] Processes updated group data",
                "/api/config/current/json"          : "[GET]  Displays Authelia's current configuration.yml file in JSON format",
                "/api/config/current/yaml"          : "[GET]  Displays Authelia's current configuration.yml file in YAML format",
                "/api/users/current/json"           : "[GET]  Displays Authelia's current user_database.yml file in JSON format",
                "/api/users/current/yaml"           : "[GET]  Displays Authelia's current user_database.yml file in YAML format",
                "/api/randpw"                       : "[GET]  Generates Random Password (DEPRICATED)",
                "/api/account"                      : "[POST] Processes changes to user account",
                "/api/settings"                     : "[POST] Processes changes to user settings",
                "/api/login"                        : "[POST] Processes Log in",
                "/api/logout"                       : "[POST] Processes Log out"
            }
        }
        self.markdown =     "API Documentation\n"
    def md(self) -> str:
        for url in self.contents:
            """
            I'm sure there's a better way to do this, but it functions...
            """
            self.markdown += f"<pre class='text-xl bg-zinc-400 dark:bg-zinc-400 p-1 text-slate-800 dark:text-slate-800'>"
            self.markdown += f"<code class='cursor-pointer' onClick=parent.location='{url}'>"
            self.markdown += f"  {url}  \r"
            self.markdown += "</code>"
            self.markdown += "<code>"
            self.markdown += f"    {self.contents[url]}"
            self.markdown += f"</code>"
            self.markdown += f"</pre>"
        return self.contents

    