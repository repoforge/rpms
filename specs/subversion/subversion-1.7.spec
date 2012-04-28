# $Id$
# Authority: dag
# Upstream: CollabNet <dev$subversion,apache,org>

%{?dtag: %{expand: %%global %dtag 1}}

%global _default_patch_fuzz 2

# Default included settings
#    Requires bash 4.x
%global with_bash_completion 1
#    Requires gnome and recent dbus
%global with_gnome_keyring 1
#    Requires contemporary java
%global with_java 1
#    Requires KDE 4
%global with_kwallet 1
#    Requires emacs-21.3 or later
%global with_psvn 1
#    Requires ruby 3.8.2 or later
%global with_ruby 1

# Use system versions where feasible, included tarballs when not
%global with_system_neon 1
%global with_system_python 1
%global with_system_sqlite 1

# Define as 1 to run test suite,
# fails on older OS's, takes an extra hour to run
#%global make_check 1
%global make_check 0

### EL6 ships with subversion-1.6.11
%{?el6:# Tag: rfx}
### EL5 ships with subversion-1.6.11
%{?el5:# Tag: rfx}
# Fails on a few tests
%{?el5: %global make_check 0}
%{?el5: %global with_bash_completion 0}
%{?el5: %global with_kwallet 0}
%{?el5: %global with_psvn 0}

%{?el5: %global with_system_sqlite 0}
### EL4 ships with subversion-1.1.4
%{?el4:# Tag: rfx}
# Fails on a few tests
%{?el4: %global make_check 0}
%{?el4: %global with_bash_completion 0}
%{?el4: %global with_gnome_keyring 0}
%{?el4: %global with_java 0}
%{?el4: %global with_kwallet 0}
%{?el4: %global with_psvn 0}
%{?el4: %global with_ruby 0}

%{?el4: %global with_system_neon 0}
%{?el4: %global with_system_python 0}
%{?el4: %global with_system_sqlite 0}

# Local tarballs used only when system components are too old
%global neon_version 0.28.4
%global python_version 2.4.6
%global sqlite_amalgamation_version 3.6.22

# set JDK path to build javahl; default for JPackage
%global jdk_path /usr/lib/jvm/java

%global perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%if %{with_ruby}
# Define this just like __perl and __python
%{?!__ruby: %global __ruby %{_bindir}/ruby}

%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}
%endif

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: A Modern Concurrent Version Control System
Name: subversion
Version: 1.7.4
Release: 0.3%{?dist}
License: ASL 2.0
Group: Development/Tools
URL: http://subversion.apache.org/
Source0: http://www.apache.org/dist/subversion/subversion-%{version}.tar.bz2
Source1: subversion.conf
Source2: http://sqlite.org/sqlite-amalgamation-%{sqlite_amalgamation_version}.tar.gz
Source3: filter-requires.sh
Source4: http://www.xsteve.at/prg/emacs/psvn.el
Source5: psvn-init.el
Source6: svnserve.init

# The following are needed to build on el4
Source10: http://www.python.org/ftp/python/%{python_version}/Python-%{python_version}.tar.bz2
Source11: http://www.webdav.org/neon/neon-%{neon_version}.tar.gz

Patch1: subversion-1.7.0-rpath.patch
Patch2: subversion-1.7.0-pie.patch
Patch3: subversion-1.7.0-kwallet.patch
Patch4: subversion-1.7.2-ruby19.patch
Patch11: subversion-1.7.4-apr.patch
BuildRequires: apr-devel >= 0.9.4
BuildRequires: apr-util-devel >= 0.9.4
BuildRequires: autoconf
BuildRequires: cyrus-sasl-devel
BuildRequires: db4-devel >= 4.1.25
# More general requirement, file-devel is in file in some releases
#BuildRequires: file-devel
BuildRequires: /usr/include/magic.h
BuildRequires: gettext
%if %{with_gnome_keyring}
# Only used for gnome-keyring
BuildRequires: dbus-devel
BuildRequires: gnome-keyring-devel
%endif
%if %{with_kwallet}
# kde4-config forces correct kde4 packages for RHEL 6
BuildRequires: /usr/bin/kde4-config
BuildRequires: kdelibs-devel >= 4.0.0
%endif
BuildRequires: libtool
%if %{with_system_neon}
BuildRequires: neon-devel >= 0:0.24.7-1
%endif
BuildRequires: python
BuildRequires: python-devel
%if %{with_ruby}
BuildRequires: ruby
BuildRequires: ruby-devel
%endif
%if %{with_system_sqlite}
BuildRequires: sqlite-devel >= 3.4.0
%endif
BuildRequires: swig >= 1.3.21-5
BuildRequires: texinfo
BuildRequires: which
BuildRequires: zlib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: svn = %{version}-%{release}
Requires: subversion-libs%{?_isa} = %{version}-%{release}
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service

%global __perl_requires %{SOURCE3}

# Put Python bindings in site-packages
%global swigdirs swig_pydir=%{python_sitearch}/libsvn swig_pydir_extra=%{python_sitearch}/svn

%description
Subversion is a concurrent version control system which enables one
or more users to collaborate in developing and maintaining a
hierarchy of files and directories while keeping a history of all
changes.  Subversion only stores the differences between versions,
instead of every complete file.  Subversion is intended to be a
compelling replacement for CVS.

%package libs
Group: Development/Tools
Summary: Libraries for Subversion Version Control system
# APR 1.3.x interfaces are required
Conflicts: apr%{?_isa} < 1.3.0

%description libs
The subversion-libs package includes the essential shared libraries
used by the Subversion version control tools.

%package python
Group: Development/Libraries
Summary: Python bindings for Subversion Version Control system

%description python
The subversion-python package includes the Python bindings to the
Subversion libraries.

%package devel
Group: Development/Tools
Summary: Development package for the Subversion libraries
Requires: subversion%{?_isa} = %{version}-%{release}
Requires: apr-devel%{?_isa}, apr-util-devel%{?_isa}

%description devel
The subversion-devel package includes the libraries and include files
for developers interacting with the subversion package.

%if %{with_gnome_keyring}
%package gnome
Group: Development/Tools
Summary: GNOME Keyring support for Subversion
Requires: subversion%{?_isa} = %{version}-%{release}

%description gnome
The subversion-gnome package adds support for storing Subversion
passwords in the GNOME Keyring.
%endif

%package kde
Group: Development/Tools
Summary: KDE Wallet support for Subversion
Requires: subversion%{?_isa} = %{version}-%{release}

%description kde
The subversion-kde package adds support for storing Subversion
passwords in the KDE Wallet.

%if %{with_kwallet}
Kwallet for %{name} is not currently supported on this operating system
This package is a placeholder until KDE4 is available.
%endif

%package -n mod_dav_svn
Group: System Environment/Daemons
Summary: Apache httpd module for Subversion server
Requires: subversion-libs%{?_isa} = %{version}-%{release}
BuildRequires: httpd-devel >= 2.0.45

%description -n mod_dav_svn
The mod_dav_svn package allows access to a Subversion repository
using HTTP, via the Apache httpd server.

%package perl
Group: Development/Libraries
Summary: Perl bindings to the Subversion libraries
# Disabled for RHEL 5
#BuildRequires: perl-devel >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::Embed)
Requires: %(eval `perl -V:version`; echo "perl(:MODULE_COMPAT_$version)")
Requires: subversion%{?_isa} = %{version}-%{release}

%description perl
This package includes the Perl bindings to the Subversion libraries.

%if %{with_java}
%package javahl
Group: Development/Libraries
Summary: JNI bindings to the Subversion libraries
Requires: subversion%{?_isa} = %{version}-%{release}
BuildRequires: java-devel-openjdk
# JAR repacking requires both zip and unzip in the buildroot
BuildRequires: zip, unzip
# For the tests
BuildRequires: junit

%description javahl
This package includes the JNI bindings to the Subversion libraries.
%endif

%if %{with_ruby}
%package ruby
Group: Development/Libraries
Summary: Ruby bindings to the Subversion libraries
BuildRequires: ruby-devel >= 1.8.2
BuildRequires: ruby >= 1.8.2
Requires: subversion%{?_isa} = %{version}-%{release}
Conflicts: ruby-libs%{?_isa} < 1.8.2
Requires: ruby(abi) = 1.8

%description ruby
This package includes the Ruby bindings to the Subversion libraries.
%endif

%prep
%setup

%if !%{with_system_sqlite}
echo "Setting up included %{SOURCE2}"
%setup -T -D -a 2
%{__mv} sqlite-%{sqlite_amalgamation_version} sqlite-amalgamation
%endif

%if !%{with_system_python}
echo "Setting up included %{SOURCE10}"
%setup -T -D -a 10
%endif

# Old Subversion releases had traces of these
%{__rm} -rf neon apr apr-util

%if !%{with_system_neon}
echo "Setting up included %{SOURCE11}"
%setup -T -D -a 11
%{__mv} neon-%{neon_version} neon
%endif

%patch1 -p1 -b .rpath
%patch2 -p1 -b .pie
%patch3 -p1 -b .kwallet
%patch4 -p1 -b .ruby
%patch11 -p1 -b .apr

%build
%if !%{with_system_python}
# build python 2.4 and use it if target is too old
pushd Python-%{python_version}
%configure
%{__make}
export PYTHON=${PWD}/python
popd
%endif

# Regenerate the buildsystem, so that:
#  1) patches applied to configure.in take effect
#  2) the swig bindings are regenerated using the system swig
# (2) is not ideal since typically upstream test with a different
# swig version
./autogen.sh --release

# fix shebang lines, #111498
%{__perl} -pi -e 's|/usr/bin/env perl -w|/usr/bin/perl -w|' tools/hook-scripts/*.pl.in

# override weird -shrext from ruby
export svn_cv_ruby_link="%{__cc} -shared"
export svn_cv_ruby_sitedir_libsuffix=""
export svn_cv_ruby_sitedir_archsuffix=""

%ifarch sparc64
%{__sed} -i 's/-fpie/-fPIE/' Makefile.in
%endif

export CC=gcc CXX=g++ JAVA_HOME=%{jdk_path} CFLAGS="$RPM_OPT_FLAGS"
%configure \
	--disable-mod-activation \
	--disable-neon-version-check \
	--with-apr=%{_prefix} \
	--with-apr-util=%{_prefix} \
	--with-apxs=%{_sbindir}/apxs \
	--with-berkeley-db \
%if %{with_system_neon}
	--with-neon=%{_prefix} \
%endif
%if %{with_ruby}
	--with-ruby-sitedir=%{ruby_sitearch} \
%endif
%if %{with_gnome_keyring}
	--with-gnome-keyring \
%endif
%if %{with_java}
	--enable-javahl \
	--with-junit=%{_prefix}/share/java/junit.jar \
%endif
%if %{with_kwallet}
	--with-kwallet \
%else
	--without-kwallet \
%endif
	--with-sasl=%{_prefix} \
	--with-swig \
	--with-editor={_bindir}/vi

# Seems to cause RHEL 5 compilation issues
#	--disable-static \


%{__make} %{?_smp_mflags} all
%{__make} swig-py swig-py-lib %{swigdirs}
%{__make} swig-pl swig-pl-lib
%if %{with_ruby}
%{__make} swig-rb swig-rb-lib
%endif
%if %{with_java}
# javahl-javah does not parallel-make with javahl
%{__make} javahl-java javahl-javah
%{__make} %{?_smp_mflags} javahl
%endif

%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__make} install install-swig-py install-swig-pl-lib \
     DESTDIR=$RPM_BUILD_ROOT %{swigdirs}
%if %{with_ruby}
%{__make} install-swig-rb DESTDIR=$RPM_BUILD_ROOT %{swigdirs}
%endif
%if %{with_java}
%{__make} install-javahl-java install-javahl-lib javahl_javadir=%{_javadir} DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} pure_vendor_install -C subversion/bindings/swig/perl/native \
        PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{__install} -m 755 -d ${RPM_BUILD_ROOT}%{_sysconfdir}/subversion

# Add subversion.conf configuration file into httpd/conf.d directory.
%{__install} -m 755 -d ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
%{__install} -m 644 $RPM_SOURCE_DIR/subversion.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d

# Install SysV init script
%{__mkdir_p} $RPM_BUILD_ROOT/etc/rc.d/init.d
%{__install} -p -m 755 $RPM_SOURCE_DIR/svnserve.init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/svnserve

# Remove unpackaged files
%{__rm} -rf ${RPM_BUILD_ROOT}%{_includedir}/subversion-*/*.txt \
       ${RPM_BUILD_ROOT}%{python_sitearch}/*/*.{a,la}

# The SVN build system is broken w.r.t. DSO support; it treats
# normal libraries as DSOs and puts them in $libdir, whereas they
# should go in some subdir somewhere, and be linked using -module,
# etc.  So, forcibly nuke the .so's for libsvn_auth_{gnome,kde},
# since nothing should ever link against them directly.
%{__rm} -f ${RPM_BUILD_ROOT}%{_libdir}/libsvn_auth_*.so

# remove stuff produced with Perl modules
find $RPM_BUILD_ROOT -type f \
    -a \( -name .packlist -o \( -name '*.bs' -a -empty \) \) \
    -print0 | xargs -0 rm -f

# make Perl modules writable so they get stripped
find $RPM_BUILD_ROOT%{_libdir}/perl5 -type f -perm 555 -print0 |
        xargs -0 chmod 755

# unnecessary libraries for swig bindings
{__rm} -f ${RPM_BUILD_ROOT}%{_libdir}/libsvn_swig_*.{so,la,a}

%if %{with_ruby}
# Remove unnecessary ruby libraries
%{__rm} -f ${RPM_BUILD_ROOT}%{ruby_sitearch}/svn/ext/*.*a
%endif

# Trim what goes in docdir
%{__rm} -rf tools/*/*.in tools/test-scripts tools/buildbot tools/dist

%if %{with_psvn}
# Install psvn for emacs and xemacs
%{__install} -Dp -m0644 %{SOURCE4} %{buildroot}%{_datadir}/emacs/site-lisp/psvn.el
%{__install} -Dp -m0644 %{SOURCE4} %{buildroot}%{_datadir}/xemacs/site-packages/lisp/psvn.el
%endif

# Rename authz_svn INSTALL doc for docdir
ln -f subversion/mod_authz_svn/INSTALL mod_authz_svn-INSTALL

# Trim exported dependencies to APR libraries only:
%{__sed} -i "/^dependency_libs/{
     s, -l[^ ']*, ,g;
     s, -L[^ ']*, ,g;
     s,%{_libdir}/lib[^a][^p][^r][^ ']*.la, ,g;
     }"  $RPM_BUILD_ROOT%{_libdir}/*.la

%if %{with_bash_completion}
# Install bash completion
%{__install} -Dpm 644 tools/client-side/bash_completion \
        $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}
%endif

%find_lang %{name}

%if %{make_check}
%check
export LANG=C LC_ALL=C
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
export MALLOC_PERTURB_=171 MALLOC_CHECK_=3
export LIBC_FATAL_STDERR_=1
%{__make} check check-swig-pl check-swig-py CLEANUP=yes
# check-swig-rb omitted: it runs svnserve
%if %{with_java}
%{__make} check-javahl
%endif
%endif

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%post
# Register the snvserve service
/sbin/chkconfig --add svnserve

%preun
if [ $1 = 0 ]; then
	/sbin/service svnserve stop > /dev/null 2>&1
	/sbin/chkconfig --del svnserve
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post perl -p /sbin/ldconfig
%postun perl -p /sbin/ldconfig

%if %{with_ruby}
%post ruby -p /sbin/ldconfig
%postun ruby -p /sbin/ldconfig
%endif

%if %{with_java}
%post javahl -p /sbin/ldconfig
%postun javahl -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc BUGS CHANGES COMMITTERS INSTALL LICENSE NOTICE README
%doc tools mod_authz_svn-INSTALL
%{_bindir}/*
%{_mandir}/man*/*
%{_sysconfdir}/rc.d/init.d/svnserve
%if %{with_psvn}
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/xemacs/site-packages/lisp/*.el
%endif
%if %{with_bash_completion}
%{_sysconfdir}/bash_completion.d
%endif
%dir %{_sysconfdir}/subversion
%exclude %{_mandir}/man*/*::*

%files libs
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/libsvn_*.so.*
%exclude %{_libdir}/libsvn_swig_perl*
%if %{with_ruby}
%exclude %{_libdir}/libsvn_swig_ruby*
%endif
%if %{with_kwallet}
%exclude %{_libdir}/libsvn_auth_kwallet*
%endif
%if %{with_gnome_keyring}
%exclude %{_libdir}/libsvn_auth_gnome*
%endif

%files python
%defattr(-,root,root)
%{python_sitearch}/svn
%{python_sitearch}/libsvn

%if %{with_gnome_keyring}
%files gnome
%defattr(-,root,root)
%{_libdir}/libsvn_auth_gnome_keyring-*.so.*
%endif

%files kde
%defattr(-,root,root)
%if %{with_kwallet}
%{_libdir}/libsvn_auth_kwallet-*.so.*
%endif

%files devel
%defattr(-,root,root)
%{_includedir}/subversion-1
%{_libdir}/libsvn*.*a
%{_libdir}/libsvn*.so
%exclude %{_libdir}/libsvn_swig_perl*
%if %{with_java}
%exclude %{_libdir}/libsvnjavahl-1.*
%endif

%files -n mod_dav_svn
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/subversion.conf
%{_libdir}/httpd/modules/mod_dav_svn.so
%{_libdir}/httpd/modules/mod_authz_svn.so
%{_libdir}/httpd/modules/mod_dontdothat.so
%doc tools/server-side/mod_dontdothat/README

%files perl
%defattr(-,root,root,-)
%{perl_vendorarch}/auto/SVN
%{perl_vendorarch}/SVN
%{_libdir}/libsvn_swig_perl*
%{_mandir}/man*/*::*

%if %{with_ruby}
%files ruby
%defattr(-,root,root,-)
%{_libdir}/libsvn_swig_ruby*
%{ruby_sitearch}/svn
%endif

%if %{with_java}
%files javahl
%defattr(-,root,root,-)
%{_libdir}/libsvnjavahl-1.*
%{_javadir}/svn-javahl.jar
%endif

%changelog
* Tue Apr 24 2012  Nico Kadel-Garcia <nkadel@gmail.com> - 1.7.4-0.3
- Lots of "_with_" arguments, defined and undefiled to use "with_" syntax
  defined as 0 or 1
- Synchronize numerous layout bits between 1.6.18 and 1.7.4 .spec files
- Update psvn.el, and synchronize filter-requires.sh
- Incorporate subversion.conf from Fedora 17, but with modules
  not enabled by default

* Mon Apr 09 2012 Nico Kadel-Garcia <nkadel@gmail.com> - 1.7.4-0.2
- Synchronize filter-requires.sh with 1.6.17 SRPM.

* Thu Mar 08 2012 Nico Kadel-Garcia <nkadel@gmail.com> - 1.7.4-0.1
- Update to 1.7.4 from Repoforge package.

* Mon Feb 13 2012 Nico Kadel-Garcia <nkadel@gmail.com> - 1.7.3-0.2
- Update to 1.7.3 from Fedora 1.7.2 package
- Integrate Repoforge hooks to compile for RHEL 5 and RHEL 6,
  especially kwallet module and sqlite-amalgamation for RHEL 5.
- Simplify bash_completion installation (avoid re-arranging source directory).
- Add mod_dontdothat to mod_dav_svn package.
- Add tools/server-side/mod_dontdothat/README to mod_dav_svn docs.
- Add BuildRequires for ruby and ruby-devel to handle ruby_sitearch
  in .spec file.
- Eliminate noarch build processing, documentation is now built as
  subversion-api-docs package.
- Update subversion.conf to point to safer and more consistent /var/www/svn

* Thu Feb  9 2012 Joe Orton <jorton@redhat.com> - 1.7.2-1
- update to 1.7.2
- add Vincent Batts' Ruby 1.9 fixes from dev@

* Sun Feb  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.1-3
- fix gnome-keyring build deps 

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Joe Orton <jorton@redhat.com> - 1.7.1-1
- update to 1.7.1
- (temporarily) disable failing kwallet support

* Sun Nov 27 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.0-3
- Build with libmagic support.

* Sat Oct 15 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.0-2
- Fix apr Conflicts syntax in -libs.
- Fix obsolete chown syntax in subversion.conf.
- Fix use of spaces vs tabs in specfile.

* Wed Oct 12 2011 Joe Orton <jorton@redhat.com> - 1.7.0-1
- update to 1.7.0
- drop svn2cl (no longer shipped in upstream tarball)

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.6.17-5
- Perl mass rebuild

* Wed Jul 20 2011 Joe Orton <jorton@redhat.com> - 1.6.17-4
- run javahl tests (Blair Zajac, #723338)

* Wed Jul 20 2011 Joe Orton <jorton@redhat.com> - 1.6.17-3
- split out python subpackage

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6.17-2
- Perl mass rebuild
- change cflags in Makefile.PL to work with Perl 5.14.1

* Thu Jun  2 2011 Joe Orton <jorton@redhat.com> - 1.6.17-1
- update to 1.6.17 (#709952)

* Fri Mar  4 2011 Joe Orton <jorton@redhat.com> - 1.6.16-1
- update to 1.6.16 (#682203)
- tweak arch-specific requires

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Joe Orton <jorton@redhat.com> - 1.6.15-1
- update to 1.6.15

* Sun Oct 17 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.6.13-3
- Make name based dependencies arch qualified where appropriate (#643714).

* Tue Oct 12 2010 Joe Orton <jorton@redhat.com> - 1.6.13-2
- trim tools/buildbot, tools/dist from docdir

* Tue Oct  5 2010 Joe Orton <jorton@redhat.com> - 1.6.13-1
- update to 1.6.13

* Tue Sep  7 2010 Joe Orton <jorton@redhat.com> - 1.6.12-5
- add svnserve init script
- split out -libs subpackage

* Fri Sep  3 2010 Joe Orton <jorton@redhat.com> - 1.6.12-4
- restore PIE support

* Sat Jul 24 2010 David Malcolm <dmalcolm@redhat.com> - 1.6.12-3
- for now, disable python cases that fail against python 2.7 (patch 9)

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul  7 2010 Joe Orton <jorton@redhat.com> - 1.6.12-1
- update to 1.6.12 (#586629)
- fix comments in subversion.conf (#551484)

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.6.11-2
- Mass rebuild with perl-5.12.0

* Sat Apr 17 2010 Joe Orton <jorton@redhat.com> - 1.6.11-1
- update to 1.6.11

* Sat Feb 13 2010 Joe Orton <jorton@redhat.com> - 1.6.9-2
- fix detection of libkdecore

* Mon Feb  8 2010 Joe Orton <jorton@redhat.com> - 1.6.9-1
- update to 1.6.9 (#561810)
- fix comments in subversion.conf (#551484)
- update to psvn.el r40299

* Mon Jan 25 2010 Ville Skyttä <ville.skytta@iki.fi> - 1.6.6-5
- Include svn2cl and its man page only in the -svn2cl subpackage (#558598).
- Do not include bash completion in docs, it's installed.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.6.6-4
- rebuild against perl 5.10.1

* Thu Nov 26 2009 Joe Orton <jorton@redhat.com> - 1.6.6-3
- rebuild for new db4
- trim libsvn_* from dependency_libs in *.la

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.6.6-2
- rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Sun Nov  8 2009 Joe Orton <jorton@redhat.com> - 1.6.6-1
- update to 1.6.6

* Mon Nov  2 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.5-3
- Apply svn2cl upstream patch to fix newline issues with libxml2 2.7.4+,
  see http://bugs.debian.org/546990 for details.

* Sat Sep 19 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.5-2
- Ship svn2cl and bash completion (#496456).
- Add %%defattr to -gnome and -kde.

* Sun Aug 23 2009 Joe Orton <jorton@redhat.com> 1.6.5-1
- update to 1.6.5

* Tue Aug 18 2009 Joe Orton <jorton@redhat.com> 1.6.4-4
- rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.4-3
- Use bzipped upstream tarball.

* Fri Aug  7 2009 Joe Orton <jorton@redhat.com> 1.6.4-2
- update to 1.6.4

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Joe Orton <jorton@redhat.com> 1.6.3-2
- remove -devel dependency on -gnome, -kde (#513313)

* Tue Jun 23 2009 Joe Orton <jorton@redhat.com> 1.6.3-1
- update to 1.6.3

* Sun Jun 14 2009 Joe Orton <jorton@redhat.com> 1.6.2-3
- add -gnome, -kde subpackages

* Mon Jun  1 2009 Joe Orton <jorton@redhat.com> 1.6.2-2
- enable KWallet, gnome-keyring support

* Fri May 15 2009 Joe Orton <jorton@redhat.com> 1.6.2-1
- update to 1.6.2

* Wed Apr 15 2009 Joe Orton <jorton@redhat.com> 1.6.1-4
- really disable PIE

* Tue Apr 14 2009 Joe Orton <jorton@redhat.com> 1.6.1-3
- update to 1.6.1; disable PIE patch for the time being

* Tue Mar 31 2009 Joe Orton <jorton@redhat.com> 1.6.0-3
- BR sqlite-devel

* Tue Mar 31 2009 Joe Orton <jorton@redhat.com> 1.6.0-1
- update to 1.6.0

* Thu Mar 12 2009 Dennis Gilmore <dennis@ausil.us> - 1.5.6-4
- use -fPIE on sparc64

* Mon Mar  9 2009 Joe Orton <jorton@redhat.com> 1.5.6-3
- update to 1.5.6
- autoload psvn (#238491, Tom Tromey)
- regenerate swig bindings (#480503)
- fix build with libtool 2.2 (#469524)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Joe Orton <jorton@redhat.com> 1.5.5-5
- update to 1.5.5

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.5.4-4
- Rebuild for Python 2.6

* Mon Oct 27 2008 Joe Orton <jorton@redhat.com> 1.5.4-3
- update to 1.5.4

* Mon Oct 13 2008 Joe Orton <jorton@redhat.com> 1.5.3-3
- fix build

* Mon Oct 13 2008 Joe Orton <jorton@redhat.com> 1.5.3-2
- update to 1.5.3 (#466674)
- update psvn.el to r33557

* Tue Sep 30 2008 Joe Orton <jorton@redhat.com> 1.5.2-3
- enable SASL support (#464267)

* Fri Sep 12 2008 Joe Orton <jorton@redhat.com> 1.5.2-2
- update to 1.5.2

* Mon Jul 28 2008 Joe Orton <jorton@redhat.com> 1.5.1-2
- update to 1.5.1
- require suitable APR

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5.0-8
- rebuild against new db4-4.7

* Thu Jul  3 2008 Joe Orton <jorton@redhat.com> 1.5.0-7
- add svnmerge and wcgrep to docdir (Edward Rudd, #451932)
- drop neon version overrides

* Wed Jul  2 2008 Joe Orton <jorton@redhat.com> 1.5.0-6
- build with OpenJDK

* Wed Jul  2 2008 Joe Orton <jorton@redhat.com> 1.5.0-5
- fix files list

* Wed Jul  2 2008 Joe Orton <jorton@redhat.com> 1.5.0-4
- swig-perl test suite fix for Perl 5.10 (upstream r31546)

* Tue Jul  1 2008 Joe Orton <jorton@redhat.com> 1.5.0-3
- attempt build without java bits

* Thu Jun 26 2008 Joe Orton <jorton@redhat.com> 1.5.0-2
- update to 1.5.0

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4.6-7
- tests are randomly failing, unrelated to new perl, disabled tests

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4.6-6
- rebuild for new perl (again)

* Thu Feb 21 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.4.6-5
- Correct install location of java stuff (#433295)

* Wed Feb  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4.6-4
- BR perl(ExtUtils::Embed)

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4.6-3
- rebuild for new perl

* Fri Dec 21 2007 Joe Orton <jorton@redhat.com> 1.4.6-2
- update to 1.4.6

* Mon Dec 10 2007 Warren Togami <wtogami@redhat.com> 1.4.4-11
- temporarily disable test suite

* Thu Dec  6 2007 Joe Orton <jorton@redhat.com> 1.4.4-10
- fix build with swig 1.3.33 (patch by Torsten Landschoff)

* Wed Dec  5 2007 Joe Orton <jorton@redhat.com> 1.4.4-9
- rebuild for OpenLDAP soname bump

* Tue Sep  4 2007 Joe Orton <jorton@redhat.com> 1.4.4-8
- update to psvn.el r26383 from upstream

* Sun Sep  2 2007 Joe Orton <jorton@redhat.com> 1.4.4-7
- rebuild for fixed 32-bit APR 

* Thu Aug 30 2007 Joe Orton <jorton@redhat.com> 1.4.4-6
- clarify License tag; re-enable test suite

* Thu Aug 23 2007 Joe Orton <jorton@redhat.com> 1.4.4-5
- rebuild for neon 0.27

* Wed Aug 22 2007 Joe Orton <jorton@redhat.com> 1.4.4-4
- trim dependencies from .la files
- detabify spec file
- test suite disabled to ease stress on builders

* Wed Aug  8 2007 Joe Orton <jorton@redhat.com> 1.4.4-3
- fix build with new glibc open()-as-macro
- build all swig code in %%build, not %%install
- BuildRequire perl(Test::More), perl(ExtUtils::MakeMaker)

* Tue Jul  3 2007 Joe Orton <jorton@redhat.com> 1.4.4-2
- update to 1.4.4
- add Provides: svn (#245087)
- fix without-java build (Lennert Buytenhek, #245467)

* Wed Apr 11 2007 Joe Orton <jorton@redhat.com> 1.4.3-5
- fix version of apr/apr-util in BR (#216181)

* Thu Mar 29 2007 Joe Orton <jorton@redhat.com> 1.4.3-4
- fix javahl compile failure

* Mon Jan 29 2007 Joe Orton <jorton@redhat.com> 1.4.3-3
- update to 1.4.3 (#228691)
- remove trailing dot from Summary
- use current preferred standard BuildRoot
- add post/postun ldconfig scriptlets for -ruby and -javahl

* Fri Dec  8 2006 Joe Orton <jorton@redhat.com> 1.4.2-5
- fix use of python_sitearch

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.4.2-4
- rebuild against python 2.5
- follow python packaging guidelines

* Wed Nov  8 2006 Joe Orton <jorton@redhat.com> 1.4.2-3
- update to 1.4.2

* Mon Sep 11 2006 Joe Orton <jorton@redhat.com> 1.4.0-2
- update to 1.4.0

* Thu Jul 13 2006 Joe Orton <jorton@redhat.com> 1.3.2-6
- fix ruby packaging (#191611)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.3.2-5.1
- rebuild

* Wed Jun  7 2006 Joe Orton <jorton@redhat.com> 1.3.2-5
- disable test suite

* Wed Jun  7 2006 Joe Orton <jorton@redhat.com> 1.3.2-4
- BR gettext

* Fri Jun  2 2006 Joe Orton <jorton@redhat.com> 1.3.2-3
- re-enable test suite

* Fri Jun  2 2006 Joe Orton <jorton@redhat.com> 1.3.2-2
- update to 1.3.2
- fix Ruby sitelibdir (Garrick Staples, #191611)
- own /etc/subversion (#189071)
- update to psvn.el r19857

* Thu Apr  6 2006 Joe Orton <jorton@redhat.com> 1.3.1-4
- move libsvn_swig_ruby* back to subversion-ruby

* Tue Apr  4 2006 Joe Orton <jorton@redhat.com> 1.3.1-3
- update to 1.3.1
- update to psvn.el r19138 (Stefan Reichoer)
- build -java on s390 again

* Thu Feb 16 2006 Florian La Roche <laroche@redhat.com> - 1.3.0-5
- do not package libs within subversion-ruby, these are already
  available via the main package

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.3.0-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.3.0-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 1.3.0-4
- run check-swig-py in %%check (#178448)
- relax JDK requirement (Kenneth Porter, #177367)

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 1.3.0-3
- rebuild for neon 0.25

* Wed Jan  4 2006 Joe Orton <jorton@redhat.com> 1.3.0-2
- update to 1.3.0 (#176833)
- update to psvn.el r17921 Stefan Reichoer

* Mon Dec 12 2005 Joe Orton <jorton@redhat.com> 1.2.3-6
- fix ownership of libsvnjavahl.* (#175289)
- try building javahl on ia64/ppc64 again

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec  2 2005 Joe Orton <jorton@redhat.com> 1.2.3-5
- rebuild for httpd-2.2/apr-1.2/apr-util-1.2

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 1.2.3-4
- rebuilt against new openssl

* Thu Sep  8 2005 Joe Orton <jorton@redhat.com> 1.2.3-3
- update to 1.2.3
- update to psvn.el r16070 from Stefan Reichoer
- merge subversion.conf changes from RHEL4
- merge filter-requires.sh changes from FC4 updates

* Mon Aug  8 2005 Joe Orton <jorton@redhat.com> 1.2.1-4
- add BR for which (#161015)

* Fri Jul 22 2005 Joe Orton <jorton@redhat.com> 1.2.0-3
- update to 1.2.1
- fix BuildRequires for ruby and apr-util (#163126)
- drop static library archives

* Wed May 25 2005 Joe Orton <jorton@redhat.com> 1.2.0-2
- disable java on all but x86, x86_64, ppc (#158719)

* Tue May 24 2005 Joe Orton <jorton@redhat.com> 1.2.0-1
- update to 1.2.0; add ruby subpackage

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 1.1.4-3
- enable java subpackage again
- tweak subversion.conf comments

* Sun Apr  3 2005 Joe Orton <jorton@redhat.com> 1.1.4-2
- update to 1.1.4

* Tue Mar 22 2005 Joe Orton <jorton@redhat.com> 1.1.3-8
- further swig bindings fix (upstream via Max Bowsher, #151798)
- fix perl File::Path dependency in filter-requires.sh

* Tue Mar 22 2005 Joe Orton <jorton@redhat.com> 1.1.3-7
- restore swig bindings support (from upstream via Max Bowsher, #141343)
- tweak SELinux commentary in default subversion.conf

* Wed Mar  9 2005 Joe Orton <jorton@redhat.com> 1.1.3-6
- fix svn_load_dirs File::Path version requirement

* Tue Mar  8 2005 Joe Orton <jorton@redhat.com> 1.1.3-5
- add -java subpackage for javahl libraries (Anthony Green, #116202)

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 1.1.3-4
- rebuild

* Tue Feb 15 2005 Joe Orton <jorton@redhat.com> 1.1.3-3
- run test suite in C locale (#146125)
- adjust -pie patch for build.conf naming upstream

* Wed Jan 19 2005 Joe Orton <jorton@redhat.com> 1.1.3-2
- rebuild to pick up db-4.3 properly; don't ignore test failures

* Sun Jan 16 2005 Joe Orton <jorton@redhat.com> 1.1.3-1
- update to 1.1.3 (#145236)
- fix python bindings location on x86_64 (#143522)

* Mon Jan 10 2005 Joe Orton <jorton@redhat.com> 1.1.2-3
- update to 1.1.2
- disable swig bindings due to incompatible swig version

* Wed Nov 24 2004 Joe Orton <jorton@redhat.com> 1.1.1-5
- update subversion.conf examples to be SELinux-friendly

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 1.1.1-4
- rebuild against db-4.3.21.
- x86_64: don't fail "make check" while diagnosing db-4.3.21 upgrade.

* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 1.1.1-3
- rebuild against python 2.4

* Mon Oct 25 2004 Joe Orton <jorton@redhat.com> 1.1.1-2
- update to 1.1.1
- update -pie patch to address #134786

* Mon Oct  4 2004 Joe Orton <jorton@redhat.com> 1.1.0-5
- use pure_vendor_install to fix Perl modules
- use %%find_lang to package translations (Axel Thimm)

* Thu Sep 30 2004 Joe Orton <jorton@redhat.com> 1.1.0-4
- don't use parallel make for swig-py

* Thu Sep 30 2004 Joe Orton <jorton@redhat.com> 1.1.0-3
- BuildRequire newest swig for "swig -ldflags" fix

* Thu Sep 30 2004 Joe Orton <jorton@redhat.com> 1.1.0-2
- fix swig bindings build on x86_64

* Thu Sep 30 2004 Joe Orton <jorton@redhat.com> 1.1.0-1
- update to 1.1.0

* Thu Sep 23 2004 Joe Orton <jorton@redhat.com> 1.0.8-2
- update to 1.0.8
- remove -neonver patch
- update psvn.el to 11062

* Mon Aug 23 2004 Joe Orton <jorton@redhat.com> 1.0.6-3
- add svn_load_dirs.pl to docdir (#128338)
- add psvn.el (#128356)

* Thu Jul 22 2004 Joe Orton <jorton@redhat.com> 1.0.6-2
- rebuild

* Tue Jul 20 2004 Joe Orton <jorton@redhat.com> 1.0.6-1
- update to 1.0.6
- allow build against neon 0.24.*

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 10 2004 Joe Orton <jorton@redhat.com> 1.0.5-1
- update to 1.0.5

* Mon Jun  7 2004 Joe Orton <jorton@redhat.com> 1.0.4-2
- add ra_svn security fix for CVE CAN-2004-0413 (Ben Reser)

* Fri May 28 2004 Joe Orton <jorton@redhat.com> 1.0.4-1.1
- rebuild for new swig

* Sat May 22 2004 Joe Orton <jorton@redhat.com> 1.0.4-1
- update to 1.0.4

* Fri May 21 2004 Joe Orton <jorton@redhat.com> 1.0.3-2
- build /usr/bin/* as PIEs
- add fix for libsvn_client symbol namespace violation (r9608)

* Wed May 19 2004 Joe Orton <jorton@redhat.com> 1.0.3-1
- update to 1.0.3

* Sun May 16 2004 Joe Orton <jorton@redhat.com> 1.0.2-3
- add ldconfig invocations for -perl post/postun (Ville Skyttä)

* Tue May  4 2004 Joe Orton <jorton@redhat.com> 1.0.2-2
- add perl MODULE_COMPAT requirement for -perl subpackage
- move perl man pages into -perl subpackage
- clean up -perl installation and dependencies (Ville Skyttä, #123045)

* Mon Apr 19 2004 Joe Orton <jorton@redhat.com> 1.0.2-1
- update to 1.0.2

* Fri Mar 12 2004 Joe Orton <jorton@redhat.com> 1.0.1-1
- update to 1.0.1; cvs2svn no longer included

* Fri Mar 12 2004 Joe Orton <jorton@redhat.com> 1.0.0-3
- add -perl subpackage for Perl bindings (steve@silug.org)
- include mod_authz_svn INSTALL file

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com> 1.0.0-2.1
- rebuilt

* Wed Feb 25 2004 Joe Orton <jorton@redhat.com> 1.0.0-2
- add fix for lack of apr_dir_read ordering guarantee (Philip Martin)
- enable compression in ra_dav by default (Tobias Ringström)

* Mon Feb 23 2004 Joe Orton <jorton@redhat.com> 1.0.0-1
- update to one-dot-oh

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 0.37.0-2
- rebuilt

* Sat Jan 24 2004 Joe Orton <jorton@redhat.com> 0.37.0-1
- update to 0.37.0

* Tue Jan 13 2004 Joe Orton <jorton@redhat.com> 0.36.0-1
- update to 0.36.0

* Thu Jan  8 2004 Joe Orton <jorton@redhat.com> 0.35.1-1
- update to 0.35.1
- fix shebang lines in hook scripts (#111498)

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 0.34.0-3
- rebuild against db-4.2.52.

* Thu Dec  4 2003 Joe Orton <jorton@redhat.com> 0.34.0-2
- package all man pages

* Thu Dec 04 2003 Joe Orton <jorton@redhat.com> 0.34.0-1
- update to 0.34.0

* Thu Nov 13 2003 Joe Orton <jorton@redhat.com> 0.32.1-3
- remove workarounds for #109268 and #109267

* Thu Nov  6 2003 Joe Orton <jorton@redhat.com> 0.32.1-2
- rebuild for Python 2.3.2
- remove libtool workaround
- add workarounds for #109268 and #109267

* Fri Oct 24 2003 Joe Orton <jorton@redhat.com> 0.32.1-1
- update to 0.31.2
- work around libtool/ppc64/db4 confusion

* Mon Oct 13 2003 Jeff Johnson <jbj@jbj.org> 0.31.0-2.1
- rebuild against db-4.2.42.

* Fri Oct 10 2003 Joe Orton <jorton@redhat.com> 0.31.0-2
- include The Book
- don't add an RPATH for libdir to executables

* Thu Oct  9 2003 Joe Orton <jorton@redhat.com> 0.31.0-1
- update to 0.31.0

* Wed Sep 24 2003 Joe Orton <jorton@redhat.com> 0.30.0-1
- update to 0.30.0

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 0.29.0-1
- update to 0.29.0

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.25-2
- rebuild

* Tue Jul 15 2003 Joe Orton <jorton@redhat.com> 0.25-1
- update to 0.25

* Mon Jul 14 2003 Joe Orton <jorton@redhat.com> 0.24.2-4
- rebuild

* Tue Jun 24 2003 Joe Orton <jorton@redhat.com> 0.24.2-3
- rebuild

* Tue Jun 24 2003 Joe Orton <jorton@redhat.com> 0.24.2-2
- don't use any LDFLAGS when building swig, fix for libdir=lib64

* Tue Jun 24 2003 Joe Orton <jorton@redhat.com> 0.24.2-1
- update to 0.24.2; fix Python bindings

* Tue Jun 17 2003 Joe Orton <jorton@redhat.com> 0.24.1-1
- update to 0.24.1; include mod_authz_svn
- force use of CC=gcc CXX=g++

* Mon Jun  9 2003 Joe Orton <jorton@redhat.com> 0.23.0-2
- add cvs2svn man page

* Mon Jun  9 2003 Joe Orton <jorton@redhat.com> 0.23.0-1
- update to 0.23.0

* Sun Jun  8 2003 Joe Orton <jorton@redhat.com> 0.22.2-7
- package cvs2svn to be usable outside docdir
- remove unnecessary files

* Thu Jun  5 2003 Joe Orton <jorton@redhat.com> 0.22.2-6
- add fix for unhandled deadlock errors in libsvn_fs
- don't package the out-of-date info pages

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com> 0.22.2-5
- rebuilt

* Tue Jun  3 2003 Joe Orton <jorton@redhat.com> 0.22.2-4
- cleanups

* Mon Jun  2 2003 Elliot Lee <sopwith@redhat.com> 0.22.2-3
- Add back in s390x, excludearch bad.

* Tue May 20 2003 Jeff Johnson <jbj@redhat.com> 0.22.2-2
- use external neon-0.23.9-2 (i.e. with neon-config), drop internal neon.
- use db-4.1.25, not db-4.0.14.
- do "make check" (but ignore failure for now).
- s390x knows not of httpd >= 2.0.45.

* Thu May  8 2003 Joe Orton <jorton@redhat.com> 0.22.2-1
- update to 0.22.2; add mod_dav_svn subpackage
- include Python bindings
- neon: force use of expat, enable SSL
- drop check for specific apr version added in -3

* Thu May  1 2003 Joe Orton <jorton@redhat.com> 0.20.1-6
- filter out perl(Config::IniFiles) requirement

* Thu May  1 2003 Joe Orton <jorton@redhat.com> 0.20.1-5
- fail early if apr-config is not 0.9.3

* Wed Apr 30 2003 Joe Orton <jorton@redhat.com> 0.20.1-4
- fix workaround for non-lib64 platforms

* Wed Apr 30 2003 Joe Orton <jorton@redhat.com> 0.20.1-3
- add workaround for libtool problem

* Tue Apr 29 2003 Joe Orton <jorton@redhat.com> 0.20.1-2
- require and use system apr, apr-util libraries
- use License not Copyright

* Fri Apr 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 0.20.1

* Wed Jan 22 2003 Jeff Johnson <jbj@redhat.com> 0.17.1-4503.0
- upgrade to 0.17.1.

* Wed Dec 11 2002 Jeff Johnson <jbj@redhat.com> 0.16-3987.1
- upgrade to 0.16.

* Wed Nov 13 2002 Jeff Johnson <jbj@redhat.com> 0.15-3687.2
- don't mess with the info handbook install yet.

* Sun Nov 10 2002 Jeff Johnson <jbj@redhat.com> 0.15-3687.1
- use libdir, build on x86_64 too.
- avoid "perl(Config::IniFiles) >= 2.27" dependency.

* Sat Nov  9 2002 Jeff Johnson <jbj@redhat.com> 0.15-3687.0
- first build from adapted spec file, only client and libraries for now.
- internal apr/apr-utils/neon until incompatibilities sort themselves out.
- avoid libdir issues on x86_64 for the moment.
