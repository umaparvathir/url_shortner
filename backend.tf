terraform {
  backend "s3" {
    bucket = "tfstatefilestorebucket18"
    key    = "tf/terraform.tfstate"
  }
}