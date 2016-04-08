echo $PATH

export PATH=/usr/bin:${PATH}

#ctest -V -E 'qgis_openstreetmaptest|qgis_wcsprovidertest|PyQgsServer' -S ./qgis-test-travis.ctest --output-on-failure

cd build
#make -j3 >/dev/null
make -j3 spatialiteprovider
make -j3 wfsprovider
make -j3 python_module_qgis__core
make -j3 pytesting
make -j3 -f python/Makefile
#make -j3 qgistesting

export LD_LIBRARY_PATH=NOTFOUND:$PWD/output/lib:
export PYTHONPATH=$PWD/output/python/:$PWD/output/python/plugins:$PWD/../tests/src/python:
export QGIS_PREFIX_PATH=$PWD/output

for i in $(seq 1 50); do
   echo "Iteration $i";
  /usr/local/bin/python2.7 ../tests/src/python/test_provider_wfs.py -v > log.txt 2>&1 || cat log.txt ;
done

