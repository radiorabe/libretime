#/bin/bash

#release.sh 1.8.2
#creates a libretime folder with a "1.8.2" suffix
#creates tarballs with a "1.8.2" suffix

#release.sh 1.8.2 RC
#creates a libretime folder with a "1.8.2-RC" suffix
#creates tarballs with a "1.8.2-RC" suffix

#release.sh 1.8.2-RC
#creates a libretime folder with a "1.8.2-RC" suffix
#creates tarballs with a "1.8.2-RC" suffix

if [ $# == 0 ]; then
    echo "Zero arguments"
    exit 1
elif [ $# == 1 ]; then
    suffix=$1
    version=$1
else
    suffix=$1-$2
    version=$1
fi

# Adding dos2unix package
apt update -y -q
apt install dos2unix php composer -y

echo "Creating tarball for LibreTime ${suffix}."

target_file=libretime-${suffix}.tar.gz

echo -n "Running composer install..."
composer install --quiet --no-dev --ignore-platform-reqs
echo " Done"

find libretime-${suffix} -type f -exec dos2unix {} \;
echo -n "Creating tarball..."
tar -czf $target_file \
        --owner=root --group=root \
        --exclude-vcs \
        --exclude .zfproject.xml \
        --exclude .gitignore \
        --exclude .gitattributes \
        --exclude dev_tools \
    libretime-${suffix} 
echo " Done"
