# opentofu/outputs.tf
# OpenTofu Infrastructure Output Exports

output "environment" {
  value       = var.environment
  description = "Target infrastructure environment"
}

output "vhost_config_path" {
  value       = local_file.nginx_vhost_config.filename
  description = "Path to generated Nginx virtual host configuration"
}

output "environment_manifest_path" {
  value       = local_file.environment_manifest.filename
  description = "Path to generated environment manifest JSON"
}

output "web_root_path" {
  value       = var.web_root
  description = "Physical web root directory path"
}
