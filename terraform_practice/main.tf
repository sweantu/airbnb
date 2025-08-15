terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.21.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project = var.project
  region  = var.region
}

resource "google_storage_bucket" "terraform-bucket" {
  name          = var.bucket_name
  location      = var.location
  force_destroy = true
}


resource "google_bigquery_dataset" "terraform_dataset" {
  dataset_id = var.dataset_id
}
