with open("pdf.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

html_code = "<html><head><style>table {border-collapse: collapse;} td {border: 1px solid black; padding: 8px;}</style></head><body><table>"
for line in lines:
    fields = line.strip().split("\t")
    html_code += "<tr>"
    for field in fields:
        html_code += f"<td>{field}</td>"
    html_code += "</tr>"
html_code += "</table></body></html>"

with open("pdfb2.html", "w", encoding="utf-8") as output_file:
    output_file.write(html_code)
