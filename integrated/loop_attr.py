def gettingNAS(ngapMessage):
    val = None
    def convert_to_bytes(js, par, val):
        if isinstance(js, dict):
            for key, value in js.items():
                if key == 'pDUSessionNAS-PDU':
                    val = value
                val = convert_to_bytes(value, js, val)
        elif isinstance(js, list):
            for i, item in enumerate(js):
                val = convert_to_bytes(item, js, val)
        elif isinstance(js, str):
            if js == 'NAS-PDU':
                val = par[1]
        return val

    return convert_to_bytes(ngapMessage, None, val)
