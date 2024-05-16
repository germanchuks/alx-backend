#!/usr/bin/env python3

import requests

url = 'https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T090540Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c71d0b75391ce07f7886764979a31a55f9218042d86f164afe0f18c0dd07b940'
response = requests.get(url)

if response.status_code == 200:
    with open('Popular_Baby_Names.csv', 'wb') as file:
        file.write(response.content)

