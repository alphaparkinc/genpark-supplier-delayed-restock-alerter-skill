class SupplierDelayedRestockClient:
    def audit_lead_time(self, promised_transit_days: int, historical_delays_days: list[int]) -> dict:
        delay = sum(historical_delays_days) / max(1, len(historical_delays_days))
        return {"estimated_total_delay_days": round(delay, 1), "alert_triggered": delay > 3.0}