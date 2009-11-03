# $Id$
# Authority: dries
# Upstream: Jeff Johnson <n3npq$mac,com>

# Tag: test


%define	with_python_subpackage	1%{nil}
# python version 2.5 => 2.4 for fc6 (dries)
%define	with_python_version	2.4%{nil}
%define	with_perl_subpackage	1%{nil}
%define	with_bzip2		1%{nil}
%define	with_apidocs		1%{nil}
%define rpm_version		4.5

%{!?_usrlibrpm:%define _usrlibrpm /usr/lib/rpm5}

# Autogenerate shell script dependencies.
#%%define __executable_requires	%{_usrlibrpm}/executabledeps.sh --requires

# XXX legacy requires './' payload prefix to be omitted from rpm packages.
%define	_noPayloadPrefix	1

%define	__prefix	%{?_prefix}%{!?_prefix:/usr}
%{?!_lib: %define _lib lib}
%{expand: %%define __share %(if [ -d %{__prefix}/share/man ]; then echo /share ; else echo %%{nil} ; fi)}


Summary: The RPM package management system.
Name: rpm5
Version: %{rpm_version}
Release: 0.3%{?dist}
Group: System Environment/Base
URL: http://wraptastic.org
Source: http://rpm5.org/files/rpm/rpm-4.5/rpm-%{version}.tar.gz
Patch: rpm5-add-5-suffix.patch
License: LGPL
%ifos linux
Prereq: fileutils shadow-utils
%endif
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

# XXX necessary only to drag in /usr/lib/libelf.a, otherwise internal elfutils.
#not available in fc6 (dries) - BuildRequires: rpm >= 4.4.7
BuildRequires: elfutils-libelf
BuildRequires: elfutils-devel
BuildRequires: zlib-devel, autoconf, automake, libtool, gcc-c++, gettext-devel, doxygen

BuildRequires: beecrypt-devel >= 4.1.2
Requires: beecrypt >= 4.1.2

BuildRequires: neon-devel
BuildRequires: sqlite-devel

%if %{with_bzip2}
BuildRequires: bzip2-devel >= 0.9.0c-2
%endif
%if %{with_python_subpackage}
BuildRequires: python-devel >= %{with_python_version}
%endif
%if %{with_perl_subpackage}
BuildRequires: perl >= 2:5.8.0
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package conflicts
Summary: Files which conflict with other rpm packages
Group: System Environment/Base

%description conflicts
Files which conflict with other rpm packages.

%package libs
Summary:  Libraries for manipulating RPM packages.
Group: Development/Libraries
# XXX this Provides: is bogus, but getconf(...) needs to be bootstrapped.
Provides: getconf(GNU_LIBPTHREAD_VERSION) = NPTL
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

%description libs
This package contains the RPM shared libraries.

%package devel
Summary:  Development files for manipulating RPM packages.
Group: Development/Libraries
Requires: rpm5 = %{version}-%{release}
Requires: rpm5-libs = %{version}-%{release}
Requires: beecrypt >= 4.1.2
Requires: neon-devel
Requires: sqlite-devel
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%package build
Summary: Scripts and executable programs used to build packages.
Group: Development/Tools
Requires: rpm5 = %{version}-%{release}, patch >= 2.5
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

%package build-conflicts
Summary: Conflicting files of the rpm5-build package
Group: Development/Tools
Requires: rpm5 = %{version}-%{release}, patch >= 2.5

%description build-conflicts
Conflicting files of the rpm5-build package.

%if %{with_python_subpackage}
%package python
Summary: Python bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
Requires: rpm = %{version}-%{release}
Requires: rpm-libs = %{version}-%{release}
Requires: python >= %{with_python_version}

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python
programs that will manipulate RPM packages and databases.
%endif

%if %{with_perl_subpackage}
%package perl
Summary: Perl bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.17
Requires: rpm = %{version}-%{release}
Requires: rpm-libs = %{version}-%{release}
Obsoletes: perl-RPM, perl-RPM2
Conflicts: perl-RPM, perl-RPM2

%description perl
The rpm-perl package contains a module that permits applications
written in the Perl programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Perl
programs that will manipulate RPM packages and databases.

(Note: rpm-perl is forked from perl-RPM2-0.66, and will obsolete existing perl-RPM packages)
%endif

%package -n popt5
Summary: A C library for parsing command line parameters.
Group: Development/Libraries
Version: 1.11

%description -n popt5
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion. Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%package -n popt5-devel
Summary: Header files, libraries and development documentation for popt5.
Group: Development/Libraries
Requires: popt5

%description -n popt5-devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using popt5,
you will need to install popt5-devel.

%package  -n popt5-devel-conflicts
Summary: Conflicting files for popt5-devel.
Group: Development/Libraries
Requires: popt5-devel

%description -n popt5-devel-conflicts
This package contains the conflicting files of popt5-devel.


%prep
%setup -q -n rpm-%{rpm_version}
%patch -p1
%{__cp} gendiff gendiff5
%{__cp} scripts/rpm2cpio scripts/rpm2cpio5
# {__perl} -pi -e "s|@localedir@|/usr/share/locale|g;" po/Makefile* */Makefile*

%build
bash ./autogen.sh
# XXX rpm needs functioning nptl for configure tests
unset LD_ASSUME_KERNEL || :

%if %{with_python_subpackage}
WITH_PYTHON="--with-python=%{with_python_version}"
%else
WITH_PYTHON="--without-python"
%endif

%if %{with_perl_subpackage}
WITH_PERL="--with-perl"
%else
WITH_PERL="--without-perl"
%endif
bash ./autogen.sh
%ifos linux
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
localedir=%{_prefix}/share/locale ./configure --prefix=%{_prefix} --sysconfdir=/etc \
	--localstatedir=/var --infodir='${prefix}%{__share}/info' \
	--mandir='${prefix}%{__share}/man' \
	$WITH_PYTHON $WITH_PERL --enable-posixmutexes --without-javaglue \
	
%else
export CPPFLAGS=-I%{_prefix}/include 
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} $WITH_PYTHON $WITH_PERL \
	--without-javaglue
%endif

make -C zlib || :

make %{?_smp_mflags}

%install
# XXX rpm needs functioning nptl for configure tests
unset LD_ASSUME_KERNEL || :

rm -rf $RPM_BUILD_ROOT

%if %{with_perl_subpackage}
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT$installarchlib
%endif

make DESTDIR="$RPM_BUILD_ROOT" localedir=/usr/share/locale install

%ifos linux

# Save list of packages through cron
mkdir -p ${RPM_BUILD_ROOT}/etc/cron.daily
install -m 755 scripts/rpm.daily ${RPM_BUILD_ROOT}/etc/cron.daily/rpm

mkdir -p ${RPM_BUILD_ROOT}/etc/logrotate.d
install -m 644 scripts/rpm.log ${RPM_BUILD_ROOT}/etc/logrotate.d/rpm

mkdir -p $RPM_BUILD_ROOT/etc/rpm

mkdir -p $RPM_BUILD_ROOT/var/spool/repackage
mkdir -p $RPM_BUILD_ROOT/var/lib/rpm
for dbi in \
	Basenames Conflictname Dirnames Group Installtid Name Packages \
	Providename Provideversion Requirename Requireversion Triggername \
	Filemd5s Pubkeys Sha1header Sigmd5 \
	__db.001 __db.002 __db.003 __db.004 __db.005 __db.006 __db.007 \
	__db.008 __db.009
do
    touch $RPM_BUILD_ROOT/var/lib/rpm/$dbi
done

%endif

%if %{with_apidocs}
gzip -9n apidocs/man/man*/* || :
%endif

# Get rid of unpackaged files
{ cd $RPM_BUILD_ROOT
  rm -f .%{_usrlibrpm}/{Specfile.pm,cpanflute,cpanflute2,rpmdiff,rpmdiff.cgi,sql.prov,sql.req,tcl.req,trpm}
  rm -rf .%{_mandir}/man8/rpmcache.8*
  rm -rf .%{_mandir}/man8/rpmgraph.8*
  rm -rf .%{_mandir}/ja/man8/rpmcache.8*
  rm -rf .%{_mandir}/ja/man8/rpmgraph.8*
  rm -rf .%{_mandir}/pl/man8/rpmcache.8*
  rm -rf .%{_mandir}/pl/man8/rpmgraph.8*
  rm -rf .%{_mandir}/{fr,ko}
  rm -f .%{_bindir}/rpm{e,i,u}
  rm -f .%{_bindir}/rpm
%if %{with_python_subpackage}
  rm -f .%{_libdir}/python%{with_python_version}/site-packages/*.{a,la}
  rm -f .%{_libdir}/python%{with_python_version}/site-packages/rpm/*.{a,la}
%endif
%if %{with_perl_subpackage}
  find .%{_libdir}/perl5 -type f -a \( -name perllocal.pod -o -name .packlist \
    -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
  find .%{_libdir}/perl5 -type d -depth -exec rmdir {} 2>/dev/null ';'
%endif
}

%clean
rm -rf $RPM_BUILD_ROOT

%ifos linux
%pre
/usr/sbin/groupadd -g 37 rpm				> /dev/null 2>&1
/usr/sbin/useradd  -r -d /var/lib/rpm -u 37 -g 37 rpm -s /sbin/nologin	> /dev/null 2>&1
exit 0
%endif

%post
%ifos linux
/sbin/ldconfig

# Establish correct rpmdb ownership.
/bin/chown rpm:rpm /var/lib/rpm/[A-Z]*

%endif
exit 0

%ifos linux
%postun
/sbin/ldconfig
if [ $1 = 0 ]; then
    /usr/sbin/userdel rpm
    /usr/sbin/groupdel rpm
fi
exit 0

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%post -n popt5 -p /sbin/ldconfig
%postun -n popt5 -p /sbin/ldconfig
%endif

%define	rpmattr		%attr(0755, rpm, rpm)

%files
%doc CHANGES GROUPS doc/manual/[a-z]*
%pubkey wdj/JBJ-GPG-KEY
%attr(0755, rpm, rpm)	/bin/rpm5

%ifos linux
#%config(noreplace,missingok)	/etc/cron.daily/rpm
#%config(noreplace,missingok)	/etc/logrotate.d/rpm
%dir				/etc/rpm
#%config(noreplace,missingok)	/etc/rpm/macros.*
%attr(0755, rpm, rpm)	%dir /var/lib/rpm
%attr(0755, rpm, rpm)	%dir /var/spool/repackage

%define	rpmdbattr %attr(0644, rpm, rpm) %verify(not md5 size mtime) %ghost %config(missingok,noreplace)
%rpmdbattr	/var/lib/rpm/*
%endif

%rpmattr	%{_bindir}/rpm2cpio5
%rpmattr	%{_bindir}/gendiff5
%rpmattr	%{_bindir}/rpmdb5
#%rpmattr	%{_bindir}/rpmdigest5
#%rpmattr	%{_bindir}/rpm[eiu]5
%rpmattr	%{_bindir}/rpmsign5
%rpmattr	%{_bindir}/rpmquery5
%rpmattr	%{_bindir}/rpmverify5

%attr(0755, rpm, rpm)	%dir %{_usrlibrpm}
%rpmattr	%{_usrlibrpm}/config.guess
%rpmattr	%{_usrlibrpm}/config.sub
%attr(0644, rpm, rpm)	%{_usrlibrpm}/macros
%rpmattr	%{_usrlibrpm}/mkinstalldirs
%rpmattr	%{_usrlibrpm}/rpm.*
%rpmattr	%{_usrlibrpm}/rpm[deiukqv]5
%rpmattr	%{_usrlibrpm}/rpm[deiukqv]
%rpmattr	%{_usrlibrpm}/tgpg
%attr(0644, rpm, rpm)	%{_usrlibrpm}/rpmpopt*
%attr(0644, rpm, rpm)	%{_usrlibrpm}/rpmrc


%ifarch i386 i486 i586 i686 athlon pentium3 pentium4
%attr(-, rpm, rpm)		%{_usrlibrpm}/i[3456]86*
%attr(-, rpm, rpm)		%{_usrlibrpm}/athlon*
%attr(-, rpm, rpm)		%{_usrlibrpm}/pentium*
%endif
%ifarch alpha alphaev5 alphaev56 alphapca56 alphaev6 alphaev67
%attr(-, rpm, rpm)		%{_usrlibrpm}/alpha*
%endif
%ifarch sparc sparcv8 sparcv9 sparc64
%attr(-, rpm, rpm)		%{_usrlibrpm}/sparc*
%endif
%ifarch ia64
%attr(-, rpm, rpm)		%{_usrlibrpm}/ia64*
%endif
%ifarch powerpc ppc ppciseries ppcpseries ppcmac ppc64
%attr(-, rpm, rpm)		%{_usrlibrpm}/ppc*
%endif
%ifarch s390 s390x
%attr(-, rpm, rpm)		%{_usrlibrpm}/s390*
%endif
%ifarch armv3l armv4b armv4l
%attr(-, rpm, rpm)		%{_usrlibrpm}/armv[34][lb]*
%endif
%ifarch armv5teb armv5tel
%attr(-, rpm, rpm)		%{_usrlibrpm}/armv[345]*
%endif
%ifarch mips mipsel
%attr(-, rpm, rpm)		%{_usrlibrpm}/mips*
%endif
%ifarch x86_64
%attr(-, rpm, rpm)		%{_usrlibrpm}/x86_64*
%endif
%attr(-, rpm, rpm)		%{_usrlibrpm}/noarch*

%rpmattr	%{_usrlibrpm}/rpmdb_*
#%rpmattr	%{_usrlibrpm}/rpmfile

%lang(cs)	%{__prefix}/*/locale/cs/LC_MESSAGES/rpm.mo
%lang(da)	%{__prefix}/*/locale/da/LC_MESSAGES/rpm.mo
%lang(de)	%{__prefix}/*/locale/de/LC_MESSAGES/rpm.mo
%lang(fi)	%{__prefix}/*/locale/fi/LC_MESSAGES/rpm.mo
%lang(fr)	%{__prefix}/*/locale/fr/LC_MESSAGES/rpm.mo
%lang(gl)	%{__prefix}/*/locale/gl/LC_MESSAGES/rpm.mo
%lang(is)	%{__prefix}/*/locale/is/LC_MESSAGES/rpm.mo
%lang(ja)	%{__prefix}/*/locale/ja/LC_MESSAGES/rpm.mo
%lang(ko)	%{__prefix}/*/locale/ko/LC_MESSAGES/rpm.mo
%lang(no)	%{__prefix}/*/locale/no/LC_MESSAGES/rpm.mo
%lang(pl)	%{__prefix}/*/locale/pl/LC_MESSAGES/rpm.mo
%lang(pt)	%{__prefix}/*/locale/pt/LC_MESSAGES/rpm.mo
%lang(pt_BR)	%{__prefix}/*/locale/pt_BR/LC_MESSAGES/rpm.mo
%lang(ro)	%{__prefix}/*/locale/ro/LC_MESSAGES/rpm.mo
%lang(ru)	%{__prefix}/*/locale/ru/LC_MESSAGES/rpm.mo
%lang(sk)	%{__prefix}/*/locale/sk/LC_MESSAGES/rpm.mo
%lang(sl)	%{__prefix}/*/locale/sl/LC_MESSAGES/rpm.mo
%lang(sr)	%{__prefix}/*/locale/sr/LC_MESSAGES/rpm.mo
%lang(sv)	%{__prefix}/*/locale/sv/LC_MESSAGES/rpm.mo
%lang(tr)	%{__prefix}/*/locale/tr/LC_MESSAGES/rpm.mo
%lang(uk)	%{__prefix}/*/locale/uk/LC_MESSAGES/rpm.mo


%files conflicts
%ifos linux
%config(noreplace,missingok)	/etc/cron.daily/rpm
%config(noreplace,missingok)	/etc/logrotate.d/rpm
%endif

%{_mandir}/man8/rpm.8*
%{_mandir}/man8/rpm2cpio.8*
%lang(ja)	%{_mandir}/ja/man8/rpm.8*
%lang(ja)	%{_mandir}/ja/man8/rpm2cpio.8*
#%lang(ko)	%{_mandir}/ko/man8/rpm.8*
#%lang(ko)	%{_mandir}/ko/man8/rpm2cpio.8*
%lang(pl)	%{_mandir}/pl/man8/rpm.8*
%lang(pl)	%{_mandir}/pl/man8/rpm2cpio.8*
%lang(ru)	%{_mandir}/ru/man8/rpm.8*
%lang(ru)	%{_mandir}/ru/man8/rpm2cpio.8*
%lang(sk)	%{_mandir}/sk/man8/rpm.8*

%files libs
%{_libdir}/librpm5-4.4.so
%{_libdir}/librpmdb5-4.4.so
%{_libdir}/librpmio5-4.4.so
%{_libdir}/librpmbuild5-4.4.so

%files build
%dir %{__prefix}/src/rpm
%dir %{__prefix}/src/rpm/BUILD
%dir %{__prefix}/src/rpm/SPECS
%dir %{__prefix}/src/rpm/SOURCES
%dir %{__prefix}/src/rpm/SRPMS
%dir %{__prefix}/src/rpm/RPMS
%{__prefix}/src/rpm/RPMS/*
%rpmattr	%{_bindir}/rpmbuild5
%rpmattr	%{_usrlibrpm}/brp-*
%rpmattr	%{_usrlibrpm}/check-files
%rpmattr	%{_usrlibrpm}/config.site
%rpmattr	%{_usrlibrpm}/cross-build
%rpmattr	%{_usrlibrpm}/debugedit
%rpmattr	%{_usrlibrpm}/find-debuginfo.sh
%rpmattr	%{_usrlibrpm}/find-lang.sh
%rpmattr	%{_usrlibrpm}/find-prov.pl
%rpmattr	%{_usrlibrpm}/find-provides
%rpmattr	%{_usrlibrpm}/find-provides.perl
%rpmattr	%{_usrlibrpm}/find-req.pl
%rpmattr	%{_usrlibrpm}/find-requires
%rpmattr	%{_usrlibrpm}/find-requires.perl
%rpmattr	%{_usrlibrpm}/getpo.sh
%rpmattr	%{_usrlibrpm}/http.req
%rpmattr	%{_usrlibrpm}/javadeps.sh
%rpmattr	%{_usrlibrpm}/magic
%rpmattr	%{_usrlibrpm}/magic.mgc
%rpmattr	%{_usrlibrpm}/magic.mime
%rpmattr	%{_usrlibrpm}/magic.mime.mgc

%rpmattr	%{_usrlibrpm}/executabledeps.sh
%rpmattr	%{_usrlibrpm}/libtooldeps.sh
%rpmattr	%{_usrlibrpm}/perldeps.pl
%rpmattr	%{_usrlibrpm}/perl.prov
%rpmattr	%{_usrlibrpm}/perl.req
%rpmattr	%{_usrlibrpm}/php.prov
%rpmattr	%{_usrlibrpm}/php.req
%rpmattr	%{_usrlibrpm}/pkgconfigdeps.sh
%rpmattr	%{_usrlibrpm}/pythondeps.sh
%rpmattr	%{_usrlibrpm}/rpmdeps

%rpmattr	%{_usrlibrpm}/rpm[bt]5
%rpmattr	%{_usrlibrpm}/rpm[bt]
%rpmattr	%{_usrlibrpm}/symclash.*
%rpmattr	%{_usrlibrpm}/u_pkg.sh
%rpmattr	%{_usrlibrpm}/vpkg-provides.sh
%rpmattr	%{_usrlibrpm}/vpkg-provides2.sh

%files build-conflicts
%{_mandir}/man1/gendiff.1*
%{_mandir}/man8/rpmbuild.8*
%{_mandir}/man8/rpmdeps.8*

#%lang(ja)	%{_mandir}/ja/man1/gendiff.1*
%lang(ja)	%{_mandir}/ja/man8/rpmbuild.8*
#%lang(ja)	%{_mandir}/ja/man8/rpmdeps.8*
#%lang(ko)	%{_mandir}/ko/man1/gendiff.1*
#%lang(ko)	%{_mandir}/ko/man8/rpmbuild.8*
#%lang(ko)	%{_mandir}/ko/man8/rpmdeps.8*
%lang(pl)	%{_mandir}/pl/man1/gendiff.1*
%lang(pl)	%{_mandir}/pl/man8/rpmbuild.8*
%lang(pl)	%{_mandir}/pl/man8/rpmdeps.8*
#%lang(ru)	%{_mandir}/ru/man1/gendiff.1*
#%lang(ru)	%{_mandir}/ru/man8/rpmbuild.8*
#%lang(ru)	%{_mandir}/ru/man8/rpmdeps.8*
#%lang(sk)	%{_mandir}/sk/man1/gendiff.1*
#%lang(sk)	%{_mandir}/sk/man8/rpmbuild.8*
#%lang(sk)	%{_mandir}/sk/man8/rpmdeps.8*


%if %{with_python_subpackage}
%files python
%{_libdir}/python%{with_python_version}/site-packages/rpm
%endif

%if %{with_perl_subpackage}
%files perl
%{_libdir}/perl5/site_perl/*/*/auto/RPM
%{_libdir}/perl5/site_perl/*/*/RPM.*
%{_mandir}/man3/RPM.*
%endif


%files devel
%if %{with_apidocs}
%doc apidocs
%endif
%{_includedir}/rpm
%{_libdir}/librpm5.a
%{_libdir}/librpm5.la
%{_libdir}/librpm5.so
%{_libdir}/librpmdb5.a
%{_libdir}/librpmdb5.la
%{_libdir}/librpmdb5.so
%{_libdir}/librpmio5.a
%{_libdir}/librpmio5.la
%{_libdir}/librpmio5.so
%{_libdir}/librpmbuild5.a
%{_libdir}/librpmbuild5.la
%{_libdir}/librpmbuild5.so

%files -n popt5
%{_libdir}/libpopt5.so.*
%{_mandir}/man3/popt.3*
%lang(cs)	%{__prefix}/*/locale/cs/LC_MESSAGES/popt.mo
%lang(da)	%{__prefix}/*/locale/da/LC_MESSAGES/popt.mo
%lang(de)	%{__prefix}/*/locale/de/LC_MESSAGES/popt.mo
%lang(es)	%{__prefix}/*/locale/es/LC_MESSAGES/popt.mo
%lang(eu_ES)	%{__prefix}/*/locale/eu_ES/LC_MESSAGES/popt.mo
%lang(fi)	%{__prefix}/*/locale/fi/LC_MESSAGES/popt.mo
%lang(fr)	%{__prefix}/*/locale/fr/LC_MESSAGES/popt.mo
%lang(gl)	%{__prefix}/*/locale/gl/LC_MESSAGES/popt.mo
%lang(hu)	%{__prefix}/*/locale/hu/LC_MESSAGES/popt.mo
%lang(id)	%{__prefix}/*/locale/id/LC_MESSAGES/popt.mo
%lang(is)	%{__prefix}/*/locale/is/LC_MESSAGES/popt.mo
%lang(it)	%{__prefix}/*/locale/it/LC_MESSAGES/popt.mo
%lang(ja)	%{__prefix}/*/locale/ja/LC_MESSAGES/popt.mo
%lang(ko)	%{__prefix}/*/locale/ko/LC_MESSAGES/popt.mo
%lang(no)	%{__prefix}/*/locale/no/LC_MESSAGES/popt.mo
%lang(pl)	%{__prefix}/*/locale/pl/LC_MESSAGES/popt.mo
%lang(pt)	%{__prefix}/*/locale/pt/LC_MESSAGES/popt.mo
%lang(pt_BR)	%{__prefix}/*/locale/pt_BR/LC_MESSAGES/popt.mo
%lang(ro)	%{__prefix}/*/locale/ro/LC_MESSAGES/popt.mo
%lang(ru)	%{__prefix}/*/locale/ru/LC_MESSAGES/popt.mo
%lang(sk)	%{__prefix}/*/locale/sk/LC_MESSAGES/popt.mo
%lang(sl)	%{__prefix}/*/locale/sl/LC_MESSAGES/popt.mo
%lang(sr)	%{__prefix}/*/locale/sr/LC_MESSAGES/popt.mo
%lang(sv)	%{__prefix}/*/locale/sv/LC_MESSAGES/popt.mo
%lang(tr)	%{__prefix}/*/locale/tr/LC_MESSAGES/popt.mo
%lang(uk)	%{__prefix}/*/locale/uk/LC_MESSAGES/popt.mo
%lang(wa)	%{__prefix}/*/locale/wa/LC_MESSAGES/popt.mo
%lang(zh)	%{__prefix}/*/locale/zh/LC_MESSAGES/popt.mo
%lang(zh_CN)	%{__prefix}/*/locale/zh_CN/LC_MESSAGES/popt.mo
%lang(zh_TW)	%{__prefix}/*/locale/zh_TW/LC_MESSAGES/popt.mo

%files -n popt5-devel
%{_libdir}/libpopt5.a
%{_libdir}/libpopt5.la
%{_libdir}/libpopt5.so
%files -n popt5-devel-conflicts
%{_includedir}/popt.h

%changelog
* Thu May 31 2007 Dries Verachtert <dries@ulyssis.org> - 4.5-0.3.1
- Requires python 2.4 instead of 2.5 so it compiles on fc6: TODO problem?
- Renamed to rpm5
- Added a patch so quite a lot of files are built and installed with suffix '5'
- todo: gettext-devel, aclocal, autoconf, automake
- todo: touch compile
- todo in prep: gendiff -> gendiff5 moven
- USRLIBRPM set to /usr/lib/rpm5

* Fri May 25 2007 Jeff Johnson <jbj@jbj.org> 4.5-0.3
- solaris: add clearenv stub.
- keys: add Getpass stub vector.
- fix: swap PART_INSTALL and PART_CLEAN automagic cleanup.
- build against rpm5.org cvs,

* Tue May 22 2007 Jeff Johnson <jbj@jbj.org> 4.5-0.2
- fix: avoid accessing freed memory.

* Mon May 21 2007 Jeff Johnson <jbj@jbj.org> 4.5-0.1
- start rpm-4.5 development.
