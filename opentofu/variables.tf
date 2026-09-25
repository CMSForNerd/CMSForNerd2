# opentofu/variables.tf
# OpenTofu Variable Definitions

variable "environment" {
  type        = string
  description = "Target infrastructure environment (staging, production, sandbox)"
  default     = "staging"
}

variable "domain_name" {
  type        = string
  description = "Primary domain or host binding for the static site"
  default     = "localhost"
}

variable "server_port" {
  type        = number
  description = "Nginx HTTP service listener port"
  default     = 8080
}

variable "web_root" {
  type        = string
  description = "Physical path for deployed static site assets"
  default     = "/var/www/cmsfornerd2"
}
