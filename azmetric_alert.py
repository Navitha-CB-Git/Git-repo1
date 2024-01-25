from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient

def main():
    SUBSCRIPTION_ID = "e0f6e841-294d-4823-943d-38ae39b56dda"
    METRIC_ALERT_NAME = "CPUUsageAlertRule"
    GROUP_NAME = "Navitha-Practice"
    VM_NAME = "VM-Python"
    RESOURCE_URI = f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{GROUP_NAME}/providers/Microsoft.Compute/virtualMachines/{VM_NAME}"


    # Create client
    monitor_client = MonitorManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )

    # Create metric alert
    metric_alert = monitor_client.metric_alerts.create_or_update(
        GROUP_NAME,
        METRIC_ALERT_NAME,
        {
            "location": "global",
            "description": "This is the description of the rule1",
            "severity": 3,
            "enabled": True,
            "scopes": [
                RESOURCE_URI
            ],
            "evaluation_frequency": "PT1M",
            "window_size": "PT15M",
            "target_resource_type": "Microsoft.Compute/virtualMachines",
            "target_resource_region": "South India",
            "criteria": {
                "odata.type": "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria",
                "all_of": [
                    {
                        "criterion_type": "DynamicThresholdCriterion",
                        "name": "High_CPU_80",
                        "metric_name": "Percentage CPU",
                        "metric_namespace": "microsoft.compute/virtualmachines",
                        "operator": "GreaterOrLessThan",
                        "time_aggregation": "Average",
                        "dimensions": [],
                        "alert_sensitivity": "Medium",
                        "failing_periods": {
                            "number_of_evaluation_periods": 4,
                            "min_failing_periods_to_alert": 4
                        },
                    }
                ]
            },
            "auto_mitigate": False,
            "actions": []
        }
    )
    print("Create metric alert:\n{}".format(metric_alert))

    # Get metric alert
    metric_alert = monitor_client.metric_alerts.get(
        GROUP_NAME,
        METRIC_ALERT_NAME
    )
    print("Get metric alert:\n{}".format(metric_alert))

    # Delete metric alert
    monitor_client.metric_alerts.delete(
        GROUP_NAME,
        METRIC_ALERT_NAME
    )
    print("Delete metric alert.")

if __name__ == "__main__":
    main()
