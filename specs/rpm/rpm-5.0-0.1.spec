# $Id$
# Authority: dries

# Tag: test

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define with_python_version 2.5%{nil}}
%{?el5:%define with_python_version 2.4%{nil}}
%{?el4:%define with_python_version 2.4%{nil}}
%{?el3:%define with_python_version 2.4%{nil}}
%{?fc7:%define with_python_version 2.5%{nil}}
%{?fc6:%define with_python_version 2.4%{nil}}
%{?fc5:%define with_python_version 2.4%{nil}}
%{?fc4:%define with_python_version 2.4%{nil}}
%{?fc3:%define with_python_version 2.4%{nil}}

%define	with_python_subpackage	1%{nil}
#define	with_python_version	2.5%{nil}
%define	with_perl_subpackage	1%{nil}
%define	with_bzip2		1%{nil}
%define	with_apidocs		1%{nil}

%{!?_usrlibrpm:%global _usrlibrpm /usr/lib/rpm}

%define	__prefix	%{?_prefix}%{!?_prefix:/usr}
%{?!_lib: %define _lib lib}
%{expand: %%define __share %(if [ -d %{__prefix}/share/man ]; then echo /share ; else echo %%{nil} ; fi)}

%define rpm_release 0.1

Summary: The RPM package management system.
Name: rpm
Version: 5.0
Release: %{rpm_release}.0%{?dist}
Group: System Environment/Base
URL: http://wraptastic.org
Source: http://rpm5.org/files/rpm/rpm-5.0/rpm-%{version}-%{rpm_release}.tar.gz

# from http://cvs.pld-linux.org/cgi-bin/cvsweb/SOURCES/rpm-arch-x86_64.patch?rev=1.4
Patch: rpm-arch-x86_64.patch

License: LGPL
%ifos linux
Prereq: fileutils shadow-utils
%endif
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

# XXX necessary only to drag in /usr/lib/libelf.a, otherwise internal elfutils.
#dries BuildRequires: rpm >= 4.4.7
BuildRequires: elfutils-libelf
BuildRequires: elfutils-devel
BuildRequires: zlib-devel, autoconf, automake, libtool, gcc-c++, gettext-devel, doxygen, python-devel

BuildRequires: beecrypt-devel >= 4.1.2
Requires: beecrypt >= 4.1.2

BuildRequires: neon-devel
BuildRequires: sqlite-devel

%if %{with_bzip2}
BuildRequires: bzip2-devel >= 0.9.0c-2
%endif
%if %{with_python_subpackage}
#dries BuildRequires: python-devel >= %{with_python_version}
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
Requires: rpm = %{version}-%{release}
Requires: rpm-libs = %{version}-%{release}
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
Requires: rpm = %{version}-%{release}, patch >= 2.5
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

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

%prep
%setup
%patch -p1

%build

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

%ifos linux
# not pretty..
%ifarch x86_64
CFLAGS="$RPM_OPT_FLAGS -fPIC "; export CFLAGS
./configure --with-pic --prefix=%{_prefix} --sysconfdir=/etc \
	--localstatedir=/var --infodir='${prefix}%{__share}/info' \
	--mandir='${prefix}%{__share}/man' \
	$WITH_PYTHON $WITH_PERL --enable-posixmutexes --without-javaglue
echo zlib opnieuw
(cd zlib; make clean; ./configure --with-pic --prefix=%{_prefix})
%else
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
./configure --prefix=%{_prefix} --sysconfdir=/etc \
	--localstatedir=/var --infodir='${prefix}%{__share}/info' \
	--mandir='${prefix}%{__share}/man' \
	$WITH_PYTHON $WITH_PERL --enable-posixmutexes --without-javaglue
%endif

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

make DESTDIR="$RPM_BUILD_ROOT" install

%ifos linux

mkdir -p $RPM_BUILD_ROOT/etc/rpm

mkdir -p $RPM_BUILD_ROOT/var/spool/repackage
mkdir -p $RPM_BUILD_ROOT/var/lib/rpm
for dbi in \
	Basenames Conflictname Dirnames Group Installtid Name Packages \
	Providename Provideversion Requirename Requireversion Triggername \
	Filemd5s Pubkeys Sha1header Sigmd5 \
	__db.001 __db.002 __db.003 __db.004 __db.005
do
    touch $RPM_BUILD_ROOT/var/lib/rpm/$dbi
done

%endif

%find_lang rpm

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

%endif

%files -f rpm.lang
%doc CHANGES GROUPS doc/manual/[a-z]*
%pubkey pubkeys/JBJ-GPG-KEY

%ifos linux
%define	rpmattr		%attr(0755, rpm, rpm)
%define	rpmdbattr %attr(0644, rpm, rpm) %verify(not md5 size mtime) %ghost %config(missingok,noreplace)

%dir				/etc/rpm
%attr(0755, rpm, rpm)	%dir /var/lib/rpm
%attr(0755, rpm, rpm)	%dir /var/spool/repackage

%rpmdbattr	/var/lib/rpm/*
%endif

%rpmattr	%{_bindir}/rpm
%rpmattr	%{_bindir}/rpm2cpio
%rpmattr	%{_bindir}/gendiff

%attr(0755, rpm, rpm)	%dir %{_usrlibrpm}
%attr(0644, rpm, rpm)	%{_usrlibrpm}/macros-5.0
%rpmattr	%{_usrlibrpm}/rpm.*
%rpmattr	%{_usrlibrpm}/tgpg
%attr(0644, rpm, rpm)	%{_usrlibrpm}/rpmpopt-5.0

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
%attr(-, rpm, rpm)		%{_usrlibrpm}/ia32e*
%attr(-, rpm, rpm)		%{_usrlibrpm}/amd64*
%endif
%attr(-, rpm, rpm)		%{_usrlibrpm}/noarch*

%rpmattr	%{_usrlibrpm}/rpmdb_loadcvt
%rpmattr	%{_usrlibrpm}/db_*

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
%{_libdir}/librpm-4.5.so
%{_libdir}/librpmdb-4.5.so
%{_libdir}/librpmio-4.5.so
%{_libdir}/librpmbuild-4.5.so

%files build
%dir %{__prefix}/src/rpm
%dir %{__prefix}/src/rpm/BUILD
%dir %{__prefix}/src/rpm/SPECS
%dir %{__prefix}/src/rpm/SOURCES
%dir %{__prefix}/src/rpm/SRPMS
%dir %{__prefix}/src/rpm/RPMS
%{__prefix}/src/rpm/RPMS/*
%rpmattr	%{_bindir}/rpmbuild
%rpmattr	%{_usrlibrpm}/brp-*
%rpmattr	%{_usrlibrpm}/check-files
%rpmattr	%{_usrlibrpm}/cross-build
%rpmattr	%{_usrlibrpm}/debugedit
%rpmattr	%{_usrlibrpm}/find-debuginfo.sh
%rpmattr	%{_usrlibrpm}/find-lang.sh
%rpmattr	%{_usrlibrpm}/find-prov.pl
%rpmattr	%{_usrlibrpm}/find-provides.perl
%rpmattr	%{_usrlibrpm}/find-req.pl
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

%rpmattr	%{_usrlibrpm}/rpm[bt]
%rpmattr	%{_usrlibrpm}/symclash.*
%rpmattr	%{_usrlibrpm}/u_pkg.sh
%rpmattr	%{_usrlibrpm}/vpkg-provides.sh
%rpmattr	%{_usrlibrpm}/vpkg-provides2.sh

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
%{_libdir}/librpm.a
%{_libdir}/librpm.la
%{_libdir}/librpm.so
%{_libdir}/librpmdb.a
%{_libdir}/librpmdb.la
%{_libdir}/librpmdb.so
%{_libdir}/librpmio.a
%{_libdir}/librpmio.la
%{_libdir}/librpmio.so
%{_libdir}/librpmbuild.a
%{_libdir}/librpmbuild.la
%{_libdir}/librpmbuild.so

%changelog
* Tue Aug 28 2007 Dries Verachtert <dries@ulyssis.org> - 5.0-0.1.0
- Rebuild, small changes.

* Fri Jun 15 2007 Jeff Johnson <jbj@rpm5.org> 5.0-0.1
- rse: provide portability fallbacks for sighold(3), sigrelse(3) and sigpause(3)
- rse: allow RPM to build again even if iconv(3) is not available
- rse: provide --with-db-{largefile,rpc,mutex} options for flexibly building DB
- rse: portability: replace hard-coded -ldl (Linux) for Lua with Autoconf checks
- rse: added devtool/devtool.conf build environment helper
- rse: pruned tree from third-party libraries (except for zlib, db and lua)
- goeran: updated "sv" translation.
- rse: cleaned up the "autogen.sh" scripts.
- jbj: skip packages/headers with unverifiable signatures.
- update README to point to new rpm5.org home.
- upgrade to file-4.21 (CVE-2007-2026, CVE-2007-2799).
- build against rpm5.org cvs,
- fix: swap PART_INSTALL and PART_CLEAN automagic cleanup.
- keys: add Getpass stub vector.
- solaris: add clearenv stub.
- fix: avoid accessing freed memory.
- start rpm-5.0 development.

