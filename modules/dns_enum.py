import dns.resolver

def get_dns_records(domain):
    records = {}

    record_types = ["A", "MX", "NS", "TXT"]

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            records[rtype] = [str(r) for r in answers]
        except:
            records[rtype] = []

    return records