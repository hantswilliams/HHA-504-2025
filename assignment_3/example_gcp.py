import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with 'systolic' and 'diastolic' (or query params as fallback).
    Returns a JSON classification of blood pressure.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    systolic = data.get("systolic", args.get("systolic"))
    diastolic = data.get("diastolic", args.get("diastolic"))

    # Presence check
    if systolic is None or diastolic is None:
        return (
            json.dumps({"error": "Both 'systolic' and 'diastolic' are required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        sys_val = float(systolic)
        dia_val = float(diastolic)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'systolic' and 'diastolic' must be numbers."}),
            400,
            {"Content-Type": "application/json"},
        )

    status = "normal" if (sys_val < 120 and dia_val < 80) else "abnormal"
    category = "Normal (<120/<80)" if status == "normal" else "Elevated/Hypertensive (simplified)"

    payload = {
        "systolic": sys_val,
        "diastolic": dia_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
