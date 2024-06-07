import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from _config.config import environments, current_year, current_date
from _config.command_runner import CommandRunner
from _config.aws_handler import AWSHandler

def main():
    command_runner = CommandRunner()
    for env_name, config in environments.items():
        config.set_aws_credentials()  # Set AWS credentials
        aws_handler = AWSHandler(env_name, config)
        # Generate the output file path
        output_file = f"/evidence-artifacts/{current_year}/{env_name}/{current_date}.aws-codecommit-get-branch.json"
        # Define the AWS CLI command with output file path
        aws_command = [
            'aws', 'codecommit', 'get-branch', '--repository-name', 'YourRepositoryName', --branch-name, 'main',  '--output', 'json'
        ]
        # Collect evidence
        aws_handler.collect_evidence(command_runner, aws_command, output_file)
if __name__ == "__main__":
    main()
