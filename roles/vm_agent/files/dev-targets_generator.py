import json

def generate_file_sd_config(targets, filename="targets.json"):
    """
    Generates a JSON file for Prometheus file-based service discovery.

    Args:
        targets: A list of dictionaries, where each dictionary represents a target group
                 and has 'targets' (list of target addresses) and 'labels' (dictionary).
        filename: The name of the output file (default: targets.json).
    """
    with open(filename, 'w') as f:
        json.dump(targets, f, indent=2)

# Example usage
targets = [
    {
        "targets": ["host1:9100", "host2:9100"],
        "labels": {
            "job": "example",
            "region": "us-east-1"
        }
    },
    {
        "targets": ["host3:9100"],
        "labels": {
            "job": "example",
            "region": "eu-west-1"
        }
    }
]

generate_file_sd_config(targets)

print(f"File targets.json generated successfully.")