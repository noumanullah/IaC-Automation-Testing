#!/bin/bash

az deployment group create --resource-group nouman_quality --name deploy-log-quality --template-file deploy_log_quality_analytics_workspace.json