echo $PATH

export PATH=/usr/bin:${PATH}

#ctest -V -E 'qgis_openstreetmaptest|qgis_wcsprovidertest|PyQgsServer' -S ./qgis-test-travis.ctest --output-on-failure

cd build
make -j3 >/dev/null

export LD_LIBRARY_PATH=NOTFOUND:/Users/travis/build/qgis/QGIS/build/output/lib:
export PYTHONPATH=/Users/travis/build/qgis/QGIS/build/output/python/:/Users/travis/build/qgis/QGIS/build/output/python/plugins:/Users/travis/build/qgis/QGIS/tests/src/python:
export QGIS_PREFIX_PATH=/Users/travis/build/qgis/QGIS/build/output

/usr/local/bin/python2.7 /Users/travis/build/qgis/QGIS/tests/src/python/test_provider_wfs.py -v

for i in $(seq 1 50); do
   echo "Iteration $i";
  /usr/local/bin/python2.7 /Users/travis/build/qgis/QGIS/tests/src/python/test_provider_wfs.py -v;
done

