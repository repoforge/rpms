# $Id$

# Authority: matthias
# Upstream: Tobi Oetiker <oetiker@ee.ethz.ch>

%define phpextdir %(php-config --extension-dir)

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.0.46
Release: 3
License: GPL
Group: Applications/Databases
URL: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/rrdtool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, perl, php-devel >= 4.0, openssl-devel
BuildRequires: libpng-devel, zlib-devel
Requires: perl >= %(rpm -q --qf '%%{epoch}:%%{version}' perl)
Requires: libpng, zlib

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and 
display time-series data (i.e. network bandwidth, machine-room temperature, 
server load average). It stores the data in a very compact way that will not 
expand over time, and it presents useful graphs by processing the data to 
enforce a certain data density. It can be used either via simple wrapper 
scripts (from shell or Perl) or via frontends that poll network devices and 
put a friendly user interface on it.


%package devel
Summary: RRDtool static libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package allow you to use directly this library.


%package -n php-%{name}
Summary: RRDtool module for PHP
Group: Development/Languages
Requires: %{name} = %{version}, php >= 4.0

%description -n php-%{name}
The php-%{name} package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.


%prep
%setup


%build
%configure \
    --enable-shared \
    --enable-local-libpng \
    --enable-local-zlib
%{__make} %{?_smp_mflags}

# Build the php4 module, the tmp install is required
%define rrdtmpdir %{_tmppath}/%{buildsubdir}-tmpinstall
%{__make} install \
	DESTDIR="%{rrdtmpdir}"
pushd contrib/php4
    ./configure \
	--with-rrdtool="%{rrdtmpdir}%{_prefix}"
    %{__make} %{?_smp_mflags}
popd
%{__rm} -rf %{rrdtmpdir}

# Fix @perl@ and @PERL@
find examples/ -type f \
    -exec /usr/bin/perl -pi -e 's|^#! \@perl\@|#!/usr/bin/perl|gi' \{\} \;
find examples/ -name "*.pl" \
    -exec perl -pi -e 's|\015||gi' \{\} \;


%install
rm -rf %{buildroot}
make install \
	DESTDIR="%{buildroot}"

# Install the php4 module
install -m755 -D contrib/php4/modules/rrdtool.so %{buildroot}%{phpextdir}/rrdtool.so
# Clean up the examples for inclusion as docs
rm -rf contrib/php4/examples/CVS

# Put perl files back where they belong
mkdir -p %{buildroot}%{perl_sitearch}/
mv %{buildroot}%{_libdir}/perl/* %{buildroot}%{perl_sitearch}/

# We only want .txt and .html files for the main documentation
mkdir -p doc2/doc
cp -a doc/*.txt doc/*.html doc2/doc/

# Clean up the examples and contrib
rm -f examples/Makefile*
rm -f contrib/Makefile*
# This is so rpm doesn't pick up perl module dependencies automatically
find examples contrib -type f -exec chmod 644 {} \;

# Put man pages back into place...
mkdir -p %{buildroot}%{_mandir}/
mv %{buildroot}%{_prefix}/man/* %{buildroot}%{_mandir}/

# Clean up the buildroot
rm -rf %{buildroot}%{_prefix}/{contrib,doc,examples,html}


%clean
rm -rf %{buildroot}

 
%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS COPYING README TODO doc2/doc
%{_bindir}/*
%{_libdir}/*.so.*
%{perl_sitearch}/*.pm
%{perl_sitearch}/auto/*
%{_mandir}/man1/*


%files devel
%defattr(-, root, root, 0755)
%doc examples
%doc contrib/add_ds contrib/killspike contrib/log2rrd contrib/rrdexplorer
%doc contrib/rrdfetchnames contrib/rrd-file-icon contrib/rrdlastds
%doc contrib/rrdproc contrib/rrdview contrib/snmpstats contrib/trytime
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%files -n php-%{name}
%defattr(-, root, root)
%doc contrib/php4/examples contrib/php4/README
%{phpextdir}/rrdtool.so


%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 1.0.46-2.fr
- Change the strict dependency on perl to fix problem with the recent
  update.

* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 1.0.46-1.fr
- Update to 1.0.46.
- Use system libpng and zlib instead of bundled ones.
- Added php-rrdtool sub-package for the php4 module.

* Fri Dec  5 2003 Matthias Saou <http://freshrpms.net/> 1.0.45-4.fr
- Added epoch to the perl dependency to work with rpm > 4.2.
- Fixed the %% escaping in the perl dep.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.0.45-2.fr
- Rebuild for Fedora Core 1.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.45.

* Wed Apr 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.42.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Mar  5 2003 Matthias Saou <http://freshrpms.net/>
- Added explicit perl version dependency.

* Sun Feb 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.41.

* Fri Jan 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.40.
- Spec file cleanup.

* Fri Jul 05 2002 Henri Gomez <hgomez@users.sourceforge.net>
- 1.0.39

* Mon Jun 03 2002 Henri Gomez <hgomez@users.sourceforge.net>
- 1.0.38

* Fri Apr 19 2002 Henri Gomez <hgomez@users.sourceforge.net>
- 1.0.37

* Tue Mar 12 2002 Henri Gomez <hgomez@users.sourceforge.net>
- 1.0.34
- rrdtools include zlib 1.1.4 which fix vulnerabilities in 1.1.3

