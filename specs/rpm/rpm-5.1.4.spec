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
#define	with_python_version	%{nil}
%define	with_perl_subpackage	0%{nil}
%define	with_bzip2		no%{nil}
%define	with_apidocs		0%{nil}

%{!?_usrlibrpm:%global _usrlibrpm /usr/lib/rpm}
%{!?_rpmhome:%global _rpmhome /usr/lib/rpm}

%define	__prefix	%{?_prefix}%{!?_prefix:/usr}
%{?!_lib: %define _lib lib}
%{expand: %%define __share %(if [ -d %{__prefix}/share/man ]; then echo /share ; else echo %%{nil} ; fi)}


Summary: The RPM package management system.
Name: rpm
Version: 5.1.4
Release: 0.1%{?dist}
Group: System Environment/Base
URL: http://rpm5.org
Source0: http://rpm5.org/files/rpm/rpm-5.0/rpm-%{version}.tar.gz
Source1: cpu-os-macros.tar.gz
License: LGPL
Requires: fileutils shadow-utils
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

Requires: autoconf, automake, libtool, gcc-c++, gettext-devel, doxygen, python-devel

# XXX necessary only to drag in /usr/lib/libelf.a, otherwise internal elfutils.
BuildRequires: elfutils-libelf
BuildRequires: elfutils-devel
BuildRequires: zlib-devel

BuildRequires: beecrypt-devel >= 4.1.2
Requires: beecrypt >= 4.1.2

BuildRequires: neon-devel
BuildRequires: sqlite-devel

%if "%{with_bzip2}" == "yes"
BuildRequires: bzip2-devel >= 1.0
%endif
%if "%{with_apidocs}" == "1"
BuildRequires: doxygen graphviz
%endif
%if %{with_python_subpackage}
BuildRequires: python-devel >= %{with_python_version}
%endif
%if %{with_perl_subpackage}
BuildRequires: perl >= 2:5.8.0
%endif

BuildRoot: %{_tmppath}/%{name}-root

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

%package common
Summary: Common RPM paths, scripts, documentation and configuration.
Group: Development/Tools

%description common
The rpm-common package contains paths, scripts, documentation
and configuration common between RPM Package Manager.

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
%setup -q

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

./configure \
        --verbose \
        --prefix=/usr \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--infodir='${prefix}%{__share}/info' \
	--mandir='${prefix}%{__share}/man' \
        --with-db=internal \
        --with-db-tools-integrated \
        --with-zlib=internal \
        --with-file=internal \
        --with-lua=internal \
        --with-sqlite=external \
        --with-beecrypt=external \
        --with-nss=external \
        --with-neon=external \
        --with-xar=internal \
        --with-bzip2=external \
        --with-popt=external \
        --with-keyutils=external \
        --with-libelf \
        --with-selinux \
	$WITH_PYTHON \
	$WITH_PERL \
        --with-db-tools-integrated \
        --with-build-extlibdep \
        --with-build-maxextlibdep \
        --enable-build-pic \
        --enable-build-pie \
        --enable-build-versionscript \
        --enable-build-warnings \
        --enable-build-debug

make -C zlib clean || :
make -C lua clean || :
make -C python clean || :

make %{?_smp_mflags}

%if %{with_apidocs}
make apidocs
%endif

%install
# XXX rpm needs functioning nptl for configure tests
unset LD_ASSUME_KERNEL || :

rm -rf $RPM_BUILD_ROOT

%if %{with_perl_subpackage}
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT$installarchlib
%endif

make DESTDIR="$RPM_BUILD_ROOT" install

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
( cd $RPM_BUILD_ROOT/%{_rpmhome}
  tar xzf %{SOURCE1}
  # XXX assume ix86 platforms for the moment
   rm -rf ./alpha-linux
   rm -rf ./alphaev5-linux
   rm -rf ./alphaev56-linux
   rm -rf ./alphaev6-linux
   rm -rf ./alphaev67-linux
   rm -rf ./alphapca56-linux
   rm -rf ./amd64-linux
   rm -rf ./ia32e-linux
   rm -rf ./ia64-linux
   rm -rf ./ppc-linux
   rm -rf ./ppc64-linux
   rm -rf ./ppc64iseries-linux
   rm -rf ./ppc64pseries-linux
   rm -rf ./ppciseries-linux
   rm -rf ./ppcpseries-linux
   rm -rf ./s390-linux
   rm -rf ./s390x-linux
   rm -rf ./sparc-linux
   rm -rf ./sparc64-linux
   rm -rf ./sparcv9-linux
   rm -rf ./x86_64-linux
)

%find_lang rpm

%if %{with_apidocs}
gzip -9n apidocs/man/man*/* || :
%endif

# Get rid of unpackaged files
{ cd $RPM_BUILD_ROOT
  rm -f .%{_rpmhome}/{Specfile.pm,cpanflute,cpanflute2,rpmdiff,rpmdiff.cgi,sql.prov,sql.req,tcl.req,trpm}
  rm -rf .%{_mandir}/man8/rpmcache.8*
  rm -rf .%{_mandir}/man8/rpmgraph.8*
  rm -rf .%{_mandir}/ja/man8/rpmcache.8*
  rm -rf .%{_mandir}/ja/man8/rpmgraph.8*
  rm -rf .%{_mandir}/pl/man8/rpmcache.8*
  rm -rf .%{_mandir}/pl/man8/rpmgraph.8*
  rm -rf .%{_mandir}/{fr,ko}
  rm -rf .%{_mandir}/man1/xar.1*
  rm -rf .%{_bindir}/xar
  rm -rf .%{_includedir}/xar
  rm -rf .%{_libdir}/libxar*
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

%pre
/usr/sbin/groupadd -g 37 rpm				> /dev/null 2>&1
/usr/sbin/useradd  -r -d /var/lib/rpm -u 37 -g 37 rpm -s /sbin/nologin	> /dev/null 2>&1
exit 0

%post
/sbin/ldconfig

# Establish correct rpmdb ownership.
/bin/chown rpm:rpm /var/lib/rpm/[A-Z]*

exit 0

%postun
/sbin/ldconfig
if [ $1 = 0 ]; then
    /usr/sbin/userdel rpm
    /usr/sbin/groupdel rpm
fi

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%define	rpmattr		%attr(0755, rpm, rpm)
%define	rpmdbattr %attr(0644, rpm, rpm) %verify(not md5 size mtime) %ghost %config(missingok,noreplace)

%files
%pubkey pubkeys/JBJ-GPG-KEY

%rpmattr	%{_bindir}/rpm
%rpmattr	%{_bindir}/rpmconstant

%rpmattr	%{_bindir}/rpmcache
%rpmattr	%{_bindir}/rpmdigest
%rpmattr	%{_bindir}/rpmgrep
%rpmattr	%{_bindir}/rpmmtree
%rpmattr	%{_bindir}/rpmrepo


%attr(0755, rpm, rpm)	%dir %{_rpmhome}
%attr(0644, rpm, rpm)	%{_rpmhome}/macros
%rpmattr	%{_rpmhome}/rpm.*
%rpmattr	%{_rpmhome}/tgpg
%attr(0644, rpm, rpm)	%{_rpmhome}/rpmpopt

%rpmattr	%{_rpmhome}/rpmdb_loadcvt
%rpmattr	%{_rpmhome}/db_*
%rpmattr	%{_rpmhome}/magic
%rpmattr	%{_rpmhome}/magic.mgc
%rpmattr	%{_rpmhome}/magic.mime
%rpmattr	%{_rpmhome}/magic.mime.mgc
%rpmattr	%{_rpmhome}/rpm2cpio
%rpmattr	%{_rpmhome}/vcheck

%files common -f rpm.lang
%doc CHANGES doc/manual/[a-z]*
%rpmattr	%{_bindir}/rpm2cpio
%rpmattr	%{_bindir}/gendiff
%dir			/etc/rpm
%attr(0755, rpm, rpm)	%dir /var/lib/rpm
%rpmdbattr		/var/lib/rpm/*
%attr(0755, rpm, rpm)	%dir /var/spool/repackage

%attr(0755, rpm, rpm)	%dir %{_usrlibrpm}
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

%dir %{__prefix}/src/rpm
%dir %{__prefix}/src/rpm/BUILD
%dir %{__prefix}/src/rpm/SPECS
%dir %{__prefix}/src/rpm/SOURCES
%dir %{__prefix}/src/rpm/SRPMS
%dir %{__prefix}/src/rpm/RPMS
%{__prefix}/src/rpm/RPMS/*

%{_mandir}/man1/rpmgrep.1*
%{_mandir}/man8/rpmmtree.8*

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

%{_mandir}/man1/gendiff.1*
%{_mandir}/man8/rpmbuild.8*
%{_mandir}/man8/rpmconstant.8*
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

%files libs
%{_libdir}/librpm-5.0.so
%{_libdir}/librpmconstant-5.0.so
%{_libdir}/librpmdb-5.0.so
%{_libdir}/librpmio-5.0.so
%{_libdir}/librpmmisc-5.0.so
%{_libdir}/librpmbuild-5.0.so

%files build
%rpmattr	%{_bindir}/rpmbuild
%rpmattr	%{_rpmhome}/brp-*
%rpmattr	%{_rpmhome}/check-files
%rpmattr	%{_rpmhome}/cross-build
%rpmattr	%{_rpmhome}/debugedit
%rpmattr	%{_rpmhome}/find-debuginfo.sh
%rpmattr	%{_rpmhome}/find-lang.sh
%rpmattr	%{_rpmhome}/find-prov.pl
%rpmattr	%{_rpmhome}/find-provides.perl
%rpmattr	%{_rpmhome}/find-req.pl
%rpmattr	%{_rpmhome}/find-requires.perl
%rpmattr	%{_rpmhome}/getpo.sh
%rpmattr	%{_rpmhome}/http.req
%rpmattr	%{_rpmhome}/install-sh
%rpmattr	%{_rpmhome}/javadeps.sh
%rpmattr	%{_rpmhome}/mono-find-provides
%rpmattr	%{_rpmhome}/mono-find-requires
%rpmattr	%{_rpmhome}/mkinstalldirs

%rpmattr	%{_rpmhome}/executabledeps.sh
%rpmattr	%{_rpmhome}/libtooldeps.sh
%rpmattr	%{_rpmhome}/osgideps.pl
%rpmattr	%{_rpmhome}/perldeps.pl
%rpmattr	%{_rpmhome}/perl.prov
%rpmattr	%{_rpmhome}/perl.req
%rpmattr	%{_rpmhome}/php.prov
%rpmattr	%{_rpmhome}/php.req
%rpmattr	%{_rpmhome}/pkgconfigdeps.sh
%rpmattr	%{_rpmhome}/pythondeps.sh
#%rpmattr	%{_rpmhome}/rpmcache
%rpmattr	%{_rpmhome}/rpmcmp
%rpmattr	%{_rpmhome}/rpmdeps
#%rpmattr	%{_rpmhome}/rpmdigest

%rpmattr	%{_rpmhome}/symclash.*
%rpmattr	%{_rpmhome}/u_pkg.sh
%rpmattr	%{_rpmhome}/vpkg-provides.sh
%rpmattr	%{_rpmhome}/vpkg-provides2.sh

%if %{with_python_subpackage}
%files python
%{_libdir}/python%{with_python_version}/site-packages/rpm
%endif

%if %{with_perl_subpackage}
%files perl
%{_libdir}/perl5/site_perl/*/*/auto/RPM
%{_libdir}/perl5/site_perl/5.*/*-linux-*/RPM*
%{_mandir}/man3/RPM*
%endif

%files devel
%if %{with_apidocs}
%doc apidocs
%endif
%{_includedir}/rpm
%{_libdir}/librpm.a
%{_libdir}/librpm.la
%{_libdir}/librpm.so
%{_libdir}/librpmconstant.a
%{_libdir}/librpmconstant.la
%{_libdir}/librpmconstant.so
%{_libdir}/librpmdb.a
%{_libdir}/librpmdb.la
%{_libdir}/librpmdb.so
%{_libdir}/librpmio.a
%{_libdir}/librpmio.la
%{_libdir}/librpmio.so
%{_libdir}/librpmmisc.a
%{_libdir}/librpmmisc.la
%{_libdir}/librpmmisc.so
%{_libdir}/librpmbuild.a
%{_libdir}/librpmbuild.la
%{_libdir}/librpmbuild.so
%{_libdir}/pkgconfig/rpm.pc

%changelog
* Sun Jun 22 2008 Dries Verachtert <dries@ulyssis.org> - 5.1.4-0.1
- Rebuild.

* Tue Jan 22 2008 Jeff Johnson <jbj@rpm5.org> - 5.1-0.1
- resurect rpm.spec.
