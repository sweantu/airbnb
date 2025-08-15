#### Compute
```bash
gcloud compute instances create instance-20250814-112447 --project=airbnb-468005 --zone=us-central1-c --machine-type=e2-medium --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=542332305110-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/trace.append --create-disk=auto-delete=yes,boot=yes,device-name=instance-20250814-112447,image=projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20250805,mode=rw,size=30,type=pd-standard --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any
```

#### Update packages
```bash
sudo apt update
sudo apt upgrade -y
sudo reboot
```

#### Conda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -n py311 python=3.11 -y
conda activate py311
conda install pandas
```

#### Notebook
```bash
conda install notebook
jupyter notebook --ip=0.0.0.0
```

#### Docker and docker compose
```bash
sudo apt remove docker docker-engine docker.io containerd runc
sudo apt update
sudo apt install ca-certificates curl gnupg lsb-release -y
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
sudo usermod -aG docker $USER
docker version
docker compose version
sudo docker run hello-world
```

#### Terraform
```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt-get update && sudo apt-get install -y terraform
terraform -version
```

#### Github
```bash
ssh-keygen -t rsa -b 4096 -C "sweantu@gmail.com"
cat ~/.ssh/id_rsa.pub
ssh -T git@github.com
git config --global user.email "sweantu@gmail.com"
git config --global user.name "Anh Tu"
git clone git@github.com:sweantu/airbnb.git
```
#### Service account
```bash
scp .keys/airbnb-468005-b68cd81995fd.json airbnb:~/
mkdir -p ~/.keys
mv ~/airbnb-468005-b68cd81995fd.json ~/.keys/
chmod 600 ~/.keys/airbnb-468005-b68cd81995fd.json
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.keys/airbnb-468005-b68cd81995fd.json"
```

#### Spark
```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
java -version
wget https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3-scala2.13.tgz
tar xvf spark-3.5.1-bin-hadoop3-scala2.13.tgz
sudo mv spark-3.5.1-bin-hadoop3-scala2.13 /opt/spark
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export PATH=$SPARK_HOME/bin:$PATH' >> ~/.bashrc
echo 'export PYSPARK_PYTHON=python3' >> ~/.bashrc
echo 'export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH' >> ~/.bashrc
echo 'export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH' >> ~/.bashrc
```