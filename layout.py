html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                            <link rel="stylesheet" href="assets/main.css">
                        </head>
                        <body class="dash-template">
                            <header>
                             <nav id="nav">
        	<b><a href="home">SentimentZION</a></b>

			</nav>
                            </div>
                            </header>
                            <div class='container'>
                            {%app_entry%}
                            </div>
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''
