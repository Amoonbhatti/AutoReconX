def generate_html_report(target, results, output_path):
    html = f"""
    <html>
    <head>
        <title>AutoReconX Report - {target}</title>
        <style>
            body {{
                font-family: Arial;
                background: #0f172a;
                color: white;
                padding: 20px;
            }}
            h1 {{ color: #38bdf8; }}
            h2 {{ color: #facc15; }}
            pre {{
                background: #1e293b;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }}
            .finding {{
                color: #ef4444;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>

    <h1>AutoReconX Report</h1>
    <h2>Target: {target}</h2>
    <hr>
    """

    for key, value in results.items():
        html += f"<h2>{key.upper()}</h2>"

        if key == "findings":
            for f in value:
                html += f'<p class="finding">{f}</p>'
        else:
            html += f"<pre>{value}</pre>"

    html += """
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path