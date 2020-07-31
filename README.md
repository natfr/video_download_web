
### 
Pytube3 was used to work with youtube. I had an issue with cipher and 
used "https://github.com/nficano/pytube/issues/642" to handle it (fixed this issue by changing 
a few lines in extract.py)

changed

cipher_url = [
                parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
            ]
to

cipher_url = [
                parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
            ]
