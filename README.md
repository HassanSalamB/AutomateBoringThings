# AutomateBoringThings
python selenium

az container create --resource-group RG-Sel --name storageseleniumunique --image jenkins/jenkins:lts --restart-policy Never --dns-name-label storageseleniumunique --ports 8080 50000 --azure-file-volume-account-name storageselenium --azure-file-volume-account-key 0ah925hMhMmlYPhAkYVs8iYqCh6uHxmyb6zPMldHnvZUvnPMFFVSgybGaKR21LGuDzpj3/WkQwBhvAZFAHtHuQ== --azure-file-volume-share-name googlefileshare1 --azure-file-volume-mount-path /var/jenkins_home

