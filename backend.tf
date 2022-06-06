terraform {
  backend "s3" {
    bucket = "tfstatefilestorebucket11"
    key    = "tf/terraform.tfstate"
  }
}