from client import SupplierDelayedRestockClient
client = SupplierDelayedRestockClient()
print(client.audit_lead_time(5, [2, 4, 3]))