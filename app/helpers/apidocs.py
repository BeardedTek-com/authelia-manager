class apidocs:
    def __init__(self) -> None:
        """
        This is where we document all the api calls.
        """
        self.contents = {
            "API Documentation":{
                "/api"                              : "API Information (THIS PAGE)",
                "/api/initdb"                       : "Init Database",
                "/api/config"                 : "Returns All Config Data",
                "/api/config/current/json"          : "Outputs Authelia's configuration.yml file in JSON format",
                "/api/config/current/yaml"          : "Outputs Authelia's configuration.yml file in YAML format",
                "/api/users/current/json"           : "Outputs Authelia's user_database.yml file in JSON format",
                "/api/users/current/yaml"           : "Outputs Authelia's user_database.yml file in YAML format"
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

    