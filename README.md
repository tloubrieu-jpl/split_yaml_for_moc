

Create files to update the Massive Cloud Computing Kubernetes cluster through a Pull Request

## Install

Clone the repostory, then

    cd split_yaml_for_moc
    pip install -r requirements.txt

TODO: have a proper python package

## Usage

For example:

Get helm charts templates, here for spark operator:

    $ helm template spark-operator/spark-operator --generate-name --set sparkJobNamespace=sdap --include-crds > ~/Documents/sdap/HLS/spark-operator-giant.yaml
    
    
Fork the cluster repository https://github.com/operate-first/apps/

Clone the fork (here https://github.com/tloubrieu-jpl/apps) locally.

    $ cd /Users/loubrieu/Documents/sdap/HLS/moc/
    $ git clone https://github.com/tloubrieu-jpl/apps.git
    
Generate the spark-operator resources and add them to the forked repository:

    python split_yaml/split_yaml.py --input-file /Users/loubrieu/Documents/sdap/HLS/charts/spark-operator-giant.yaml  --output-dir /Users/loubrieu/Documents/sdap/HLS/moc/apps/cluster-scope/base


Same for sdap templates:

    git clone https://github.com/apache/incubator-sdap-nexus.git
    cd incubator-sdap-nexus
    helm template nexus helm -n sdap -f values-moc.yaml --include-crds > ~/Documents/sdap/HLS/charts/sdap-template.yaml    
    python split_yaml/split_yaml.py --input-file /Users/loubrieu/Documents/sdap/HLS/charts/sdap-template.yaml  --output-dir /Users/loubrieu/Documents/sdap/HLS/moc/apps/cluster-scope/base
    
    
    

     

    
