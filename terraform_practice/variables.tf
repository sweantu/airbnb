variable "credentials" {
  description = "The path to the GCP credentials file"
  default = "~/.keys/airbnb-468005-b68cd81995fd.json"
}

variable "project" {
  description = "The project ID to deploy resources to"
  default = "airbnb-468005"
}

variable "region" {
  description = "The region to deploy resources to"
  default = "us-central1"
}

variable "bucket_name" {
  description = "The name of the bucket to deploy resources to"
  default = "airbnb-468005-bucket"
}

variable "location" {
  description = "The location of the bucket to deploy resources to"
  default = "us-central1"
}


variable "dataset_id" {
  description = "The ID of the dataset to deploy resources to"
  default = "airbnb_468005_dataset"
}


