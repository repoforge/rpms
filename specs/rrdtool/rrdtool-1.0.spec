# $Id$
# Authority: matthias
# Upstream: Tobi Oetiker <oetiker$ee,ethz,ch>

%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define phpextdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.0.50
Release: 3
License: GPL
Group: Applications/Databases
URL: http://oss.oetiker.ch/rrdtool/
Source: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/rrdtool-1.0.x/rrdtool-%{version}.tar.gz
Patch0: rrdtool-1.0.48-php_config.patch
Patch1: rrdtool-1.0.50-configure.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, perl, php-devel >= 4.0, openssl-devel
BuildRequires: libpng-devel, zlib-devel

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


%package -n perl-rrdtool
Summary: Perl RRDtool bindings
Group: Development/Languages
Requires: %{name} = %{version}
Obsoletes: rrdtool-perl <= %{version}
Requires: perl >= %(rpm -q --qf '%{RPMTAG_EPOCH}:%{RPMTAG_VERSION}' perl | tail -1)

%description -n perl-rrdtool
The Perl RRDtool bindings


%package -n php-rrdtool
Summary: RRDtool module for PHP
Group: Development/Languages
Requires: %{name} = %{version}, php >= 4.0

%description -n php-rrdtool
The php-%{name} package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.


%prep
%setup
%patch0 -b .phpfix
%patch1 -b .config64

### FIXME: Fixes to /usr/lib(64) for x86_64
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure contrib/php4/configure Makefile.in
%{__perl} -pi.orig -e 's|#include <config.h>|#include <config.h>\n#include "../config.h"|g;' src/rrd_tool.h

%build
%configure \
    --program-prefix="%{?_program_prefix}" \
    --enable-shared \
    --with-perl-options='INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"' \
    --enable-local-libpng \
    --enable-local-zlib \
    --with-pic
# make sure the shared libraries have a .so extension
%{__perl} -pi -e 's|shared_ext|shrext|g;' libtool
%{__perl} -pi -e 's|\\\${shrext}|.so|g;' libtool
%{__make} %{?_smp_mflags}

# Build the php4 module, the tmp install is required
%define rrdtmpdir %{_tmppath}/%{buildsubdir}-tmpinstall
%{__make} install DESTDIR="%{rrdtmpdir}"
pushd contrib/php4
    ./configure \
	--with-rrdtool="%{rrdtmpdir}%{_prefix}"
    %{__make} %{?_smp_mflags}
popd
%{__rm} -rf %{rrdtmpdir}

# Fix @perl@ and @PERL@
find examples/ -type f \
    -exec %{__perl} -pi -e 's|^#! \@perl\@|#!%{__perl}|gi' {} \;
find examples/ -name "*.pl" \
    -exec %{__perl} -pi -e 's|\015||gi' {} \;


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} site-perl-install

# Install the php4 module
%{__install} -Dp -m0755 contrib/php4/modules/rrdtool.so \
    %{buildroot}%{phpextdir}/rrdtool.so
# Clean up the examples for inclusion as docs
%{__rm} -rf contrib/php4/examples/CVS
# Put the php config bit into place
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/rrdtool.ini << EOF
; Enable rrdtool extension module
extension=rrdtool.so
EOF

# We only want .txt and .html files for the main documentation
%{__mkdir_p} rpm-doc/docs/
%{__cp} -ap doc/*.txt doc/*.html rpm-doc/docs/

# Clean up the examples and contrib
%{__rm} -f examples/Makefile* contrib/Makefile*

# This is so rpm doesn't pick up perl module dependencies automatically
find examples/ contrib/ -type f -exec chmod 0644 {} \;
# And this, to clean up what will be included
find examples/ contrib/ -type d -name CVS -o -name .libs | xargs %{__rm} -rf

# Clean up the buildroot
%{__rm} -rf %{buildroot}%{_prefix}/{contrib,doc,examples,html}/
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist
%{__rm} -f %{buildroot}%{perl_vendorarch}/ntmake.pl

# remove the empty dir
%{__rm} -Rf %{buildroot}%{_libdir}/perl

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS COPYING COPYRIGHT README TODO
%doc rpm-doc/docs/
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*


%files devel
%defattr(-, root, root, 0755)
%doc contrib/add_ds contrib/killspike contrib/log2rrd contrib/rrdexplorer
%doc contrib/rrd-file-icon contrib/rrdfetchnames contrib/rrdlastds
%doc contrib/rrdproc contrib/rrdview contrib/snmpstats contrib/trytime
%{_includedir}/rrd.h
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%files -n perl-rrdtool
%defattr(-, root, root, 0755)
%doc examples/
%doc %{_mandir}/man3/RRDp.3*
%doc %{_mandir}/man3/RRDs.3*
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%{perl_vendorarch}/auto/RRDs/


%files -n php-rrdtool
%defattr(-, root, root, 0755)
%doc contrib/php4/examples contrib/php4/README
%config(noreplace) %{_sysconfdir}/php.d/rrdtool.ini
%{phpextdir}/rrdtool.so


%changelog
* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 1.0.50-3
- Moved perl dependency to perl-rrdtool.
- Fixed perl dependency-problem on EL4/i386 caused by duplicate package.

* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 1.0.50-2
- Fixed libpng problem on x86_64 because of missing architecture in configure. (Andrey Brindeev)

* Sat Jul 30 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.50-1
- Some fixes for FC4.

* Wed May 18 2005 Dag Wieers <dag@wieers.com> - 1.0.50-1
- Updated to release 1.0.50.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 1.0.49-2
- Fix for the php-rrdtool patch. (Joe Pruett)

* Thu Aug 25 2004 Dag Wieers <dag@wieers.com> - 1.0.49-1
- Updated to release 1.0.49.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 1.0.48-3
- Fixes for x86_64. (Garrick Staples)

* Fri Jul  2 2004 Matthias Saou <http://freshrpms.net/> 1.0.48-3
- Actually apply the patch for fixing the php module, doh!

* Thu May 27 2004 Matthias Saou <http://freshrpms.net/> 1.0.48-2
- Added php.d config entry to load the module once installed.

* Thu May 13 2004 Dag Wieers <dag@wieers.com> - 1.0.48-1
- Updated to release 1.0.48.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 1.0.47-1
- Updated to release 1.0.47.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 1.0.46-2
- Change the strict dependency on perl to fix problem with the recent
  update.

* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 1.0.46-1
- Update to 1.0.46.
- Use system libpng and zlib instead of bundled ones.
- Added php-rrdtool sub-package for the php4 module.

* Fri Dec  5 2003 Matthias Saou <http://freshrpms.net/> 1.0.45-4
- Added epoch to the perl dependency to work with rpm > 4.2.
- Fixed the %% escaping in the perl dep.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.0.45-2
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

