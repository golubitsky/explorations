# Terraform

## How to spin up EC2 instances

Following [this tutorial](https://blog.gruntwork.io/an-introduction-to-terraform-f17df9c6d180):

0. Ensure `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are set.
1. [Install terraform](https://www.terraform.io/downloads.html).
1. Update `main.tf` with a [region-specific desired AMI](https://cloud-images.ubuntu.com/locator/ec2/).

```sh
terraform init # required once
terraform plan
terraform apply # same as plan, but option to apply (confirm yes)
```

Ensure all existing resources are terminated.

```sh
terraform destroy # confirm yes
```

# AWS CLI

To inspect EC2 instances:

```sh
docker pull mesosphere/aws-cli
docker run --rm -t $(tty &>/dev/null && echo "-i") \
    -e AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY \
    -e AWS_DEFAULT_REGION=us-east-1 -v "$(pwd):/project" mesosphere/aws-cli ec2 describe-instances
```
