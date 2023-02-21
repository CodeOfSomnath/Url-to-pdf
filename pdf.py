import pdfkit


def pdf():
  # specify the path of the HTML file
  html_path = 'file.html'

  # specify the path where you want to save the PDF file
  pdf_path = 'file.pdf'

  # configure pdfkit options
  options = {
    'page-size': 'Letter',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm'
  }

  # convert HTML to PDF using pdfkit
  pdfkit.from_file(html_path, pdf_path, options=options)

  # print a message indicating that the PDF has been generated
  print(f'PDF has been generated at {pdf_path}')
