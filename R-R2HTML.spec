#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R2HTML
Version  : 2.3.3
Release  : 46
URL      : https://cran.r-project.org/src/contrib/R2HTML_2.3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R2HTML_2.3.3.tar.gz
Summary  : HTML Exportation for R Objects
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
file. Thus, making HTML reports is easy. Includes a function
        that allows redirection on the fly, which appears to be very
        useful for teaching purpose, as the student can keep a copy of
        the produced output to keep all that he did during the course.
        Package comes with a vignette describing how to write HTML
        reports for statistical analysis. Finally, a driver for 'Sweave'
        allows to parse HTML flat files containing R code and to
        automatically write the corresponding outputs (tables and
        graphs).

%prep
%setup -q -c -n R2HTML
cd %{_builddir}/R2HTML

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653343199

%install
export SOURCE_DATE_EPOCH=1653343199
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2HTML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2HTML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R2HTML
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc R2HTML || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R2HTML/CITATION
/usr/lib64/R/library/R2HTML/DESCRIPTION
/usr/lib64/R/library/R2HTML/INDEX
/usr/lib64/R/library/R2HTML/Meta/Rd.rds
/usr/lib64/R/library/R2HTML/Meta/demo.rds
/usr/lib64/R/library/R2HTML/Meta/features.rds
/usr/lib64/R/library/R2HTML/Meta/hsearch.rds
/usr/lib64/R/library/R2HTML/Meta/links.rds
/usr/lib64/R/library/R2HTML/Meta/nsInfo.rds
/usr/lib64/R/library/R2HTML/Meta/package.rds
/usr/lib64/R/library/R2HTML/NAMESPACE
/usr/lib64/R/library/R2HTML/NEWS
/usr/lib64/R/library/R2HTML/R/R2HTML
/usr/lib64/R/library/R2HTML/R/R2HTML.rdb
/usr/lib64/R/library/R2HTML/R/R2HTML.rdx
/usr/lib64/R/library/R2HTML/demo/dataframe.R
/usr/lib64/R/library/R2HTML/demo/equations.R
/usr/lib64/R/library/R2HTML/demo/grids.R
/usr/lib64/R/library/R2HTML/doc/R2HTML.css
/usr/lib64/R/library/R2HTML/doc/R2HTML.pdf
/usr/lib64/R/library/R2HTML/doc/dynamic.html
/usr/lib64/R/library/R2HTML/doc/dynamic_main.html
/usr/lib64/R/library/R2HTML/doc/dynamic_menu.html
/usr/lib64/R/library/R2HTML/doc/page1.html
/usr/lib64/R/library/R2HTML/doc/page2.html
/usr/lib64/R/library/R2HTML/doc/page3.html
/usr/lib64/R/library/R2HTML/doc/page4.html
/usr/lib64/R/library/R2HTML/help/AnIndex
/usr/lib64/R/library/R2HTML/help/R2HTML.rdb
/usr/lib64/R/library/R2HTML/help/R2HTML.rdx
/usr/lib64/R/library/R2HTML/help/aliases.rds
/usr/lib64/R/library/R2HTML/help/paths.rds
/usr/lib64/R/library/R2HTML/html/00Index.html
/usr/lib64/R/library/R2HTML/html/R.css
/usr/lib64/R/library/R2HTML/output/ASCIIMathML.js
/usr/lib64/R/library/R2HTML/output/Pastel.css
/usr/lib64/R/library/R2HTML/output/R2HTML.css
/usr/lib64/R/library/R2HTML/output/R2HTMLlogo.gif
/usr/lib64/R/library/R2HTML/output/R2HTMLstuff.zip
/usr/lib64/R/library/R2HTML/output/SciViews.css
/usr/lib64/R/library/R2HTML/output/factor.gif
/usr/lib64/R/library/R2HTML/output/gridR2HTML.css
/usr/lib64/R/library/R2HTML/output/gridR2HTML.js
/usr/lib64/R/library/R2HTML/output/numeric.gif
/usr/lib64/R/library/R2HTML/output/runtime/lib/grid.js
/usr/lib64/R/library/R2HTML/output/runtime/readme.txt
/usr/lib64/R/library/R2HTML/output/runtime/styles/classic/Picasa.ini
/usr/lib64/R/library/R2HTML/output/runtime/styles/classic/Thumbs.db
/usr/lib64/R/library/R2HTML/output/runtime/styles/classic/gecko.xml
/usr/lib64/R/library/R2HTML/output/runtime/styles/classic/grid.css
/usr/lib64/R/library/R2HTML/output/runtime/styles/classic/grid.png
/usr/lib64/R/library/R2HTML/output/runtime/styles/classic/icons.png
/usr/lib64/R/library/R2HTML/output/runtime/styles/classic/loading.gif
/usr/lib64/R/library/R2HTML/output/runtime/styles/flat/Picasa.ini
/usr/lib64/R/library/R2HTML/output/runtime/styles/flat/Thumbs.db
/usr/lib64/R/library/R2HTML/output/runtime/styles/flat/gecko.xml
/usr/lib64/R/library/R2HTML/output/runtime/styles/flat/grid.css
/usr/lib64/R/library/R2HTML/output/runtime/styles/flat/grid.png
/usr/lib64/R/library/R2HTML/output/runtime/styles/flat/icons.png
/usr/lib64/R/library/R2HTML/output/runtime/styles/flat/loading.gif
/usr/lib64/R/library/R2HTML/output/runtime/styles/xp/Picasa.ini
/usr/lib64/R/library/R2HTML/output/runtime/styles/xp/Thumbs.db
/usr/lib64/R/library/R2HTML/output/runtime/styles/xp/gecko.xml
/usr/lib64/R/library/R2HTML/output/runtime/styles/xp/grid.css
/usr/lib64/R/library/R2HTML/output/runtime/styles/xp/grid.png
/usr/lib64/R/library/R2HTML/output/runtime/styles/xp/icons.png
/usr/lib64/R/library/R2HTML/output/runtime/styles/xp/loading.gif
/usr/lib64/R/library/R2HTML/output/tablesort.htc
/usr/lib64/R/library/R2HTML/samples/Pastel.css
/usr/lib64/R/library/R2HTML/samples/R2HTML.css
/usr/lib64/R/library/R2HTML/samples/essai-002.png
/usr/lib64/R/library/R2HTML/samples/essai-004.png
/usr/lib64/R/library/R2HTML/samples/essai-005.png
/usr/lib64/R/library/R2HTML/samples/essai-006.png
/usr/lib64/R/library/R2HTML/samples/example1-002.png
/usr/lib64/R/library/R2HTML/samples/example1.html
/usr/lib64/R/library/R2HTML/samples/example1.snw
/usr/lib64/R/library/R2HTML/samples/example2-004.png
/usr/lib64/R/library/R2HTML/samples/example2-007.png
/usr/lib64/R/library/R2HTML/samples/example2.html
/usr/lib64/R/library/R2HTML/samples/example2.snw
/usr/lib64/R/library/R2HTML/samples/example3-001.png
/usr/lib64/R/library/R2HTML/samples/example3-002.png
/usr/lib64/R/library/R2HTML/samples/example3.html
/usr/lib64/R/library/R2HTML/samples/example3.snw
/usr/lib64/R/library/R2HTML/samples/index.html
/usr/lib64/R/library/R2HTML/samples/toothbig.png
