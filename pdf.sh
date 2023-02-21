curl \
    -u 'api:aed0baa864334a0182ccef7de9834451' \
    -H 'Content-Type: application/json' \
    -d '{"source":$1,"landscape":false,"use_print":false}' \
    https://api.pdfshift.io/v3/convert/pdf/ \
    -o timeline-near-future.pdf

echo $1