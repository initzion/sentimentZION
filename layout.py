html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                            <link rel="stylesheet" href="assets/main.css">
                        </head>
                        <body class="dash-template" >
                            <header>
                             <nav id="nav">
        	<b><li><img src="/assets/img/circlelogo.png" class='logo' /></li>
            <li><a href="/" style = "position:absolute; left:50px; top:0px;" >SentimentZION</a></li></b>
            <ul class="container">
<c>

      <li><a href="https://utkarshbrajnil.github.io/">About Us</a></li>
</c>
            </ul>


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
