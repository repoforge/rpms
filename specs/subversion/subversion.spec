# $Id: subversion.spec 4608 2006-08-02 15:32:29Z dag $
# Authority: dag

##ExcludeDist: fc3
##Tag: test

%{?dtag: %{expand: %%define %dtag 1}}

%define _without_ruby 1

#{?el3:#define _without_swig 1}
%{?rh9:%define _without_pie 1}
%{?rh9:%define _without_swig 1}
%{?rh7:%define _without_pie 1}
%{?rh7:%define _without_swig 1}
%{?el2:%define _without_pie 1}
%{?el2:%define _without_swig 1}

%define swig_version 1.3.25

# set to zero to avoid running test suite
%define make_check 0

%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')

Summary: Modern Version Control System designed to replace CVS
Name: subversion
Version: 1.5.5
### FC3 comes with release 1.1
Release: 0.1
License: BSD
Group: Development/Tools
URL: http://subversion.tigris.org/

Source0: http://subversion.tigris.org/tarballs/subversion-%{version}.tar.bz2
Source1: subversion.conf
Source3: filter-requires.sh
Source4: http://www.xsteve.at/prg/emacs/psvn.el
Source10: http://dl.sf.net/swig/swig-%{swig_version}.tar.gz
#Patch1: subversion-0.24.2-swig.patch
Patch2: subversion-0.20.1-deplibs.patch
Patch3: subversion-0.31.0-rpath.patch
Patch6: subversion-1.5.0-pie.patch
Patch7: subversion-1.1.3-java.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, libtool, python, python-devel, texinfo, which
BuildRequires: db4-devel >= 4.1.25, expat-devel, docbook-style-xsl, gettext
BuildRequires: apr-util-devel >= 0.9.3-2, openssl-devel
BuildRequires: apr-devel >= 0.9.4
BuildRequires: neon-devel >= 0.24.7-1
#%{!?_without_swig:BuildRequires: swig >= 1.3.21-5}
#%{!?_without_swig:BuildRequires: swig}

Provides: python-subversion = %{version}-%{release}
Provides: subversion-python = %{version}-%{release}

%define __perl_requires %{SOURCE3}

# Put Python bindings in site-packages
%define swigdirs swig_pydir=%{python_sitearch}/libsvn swig_pydir_extra=%{python_sitearch}/svn

%description
Subversion is a concurrent version control system which enables one
or more users to collaborate in developing and maintaining a
hierarchy of files and directories while keeping a history of all
changes.  Subversion only stores the differences between versions,
instead of every complete file.  Subversion is intended to be a
compelling replacement for CVS.

%package devel
Group: Development/Tools
Summary: Development package for Subversion developers.
Requires: subversion = %{version}-%{release}, apr-devel, apr-util-devel

%description devel
The subversion-devel package includes the static libraries and
include files for developers interacting with the subversion
package.

%package -n mod_dav_svn
Group: System Environment/Daemons
Summary: Apache server module for Subversion server.
Requires: httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing)
Requires: subversion = %{version}-%{release}
BuildRequires: httpd-devel >= 2.0.45

%description -n mod_dav_svn
The mod_dav_svn package allows access to a Subversion repository
using HTTP, via the Apache httpd server.

%package perl
Group: Development/Libraries
Summary: Perl bindings to the Subversion libraries
BuildRequires: perl >= 2:5.8.0, perl(ExtUtils::MakeMaker)
Requires: %(eval `perl -V:version`; echo "perl(:MODULE_COMPAT_$version)")
Requires: subversion = %{version}-%{release}

%description perl
This package includes the Perl bindings to the Subversion libraries.

%package javahl
Group: Development/Libraries
Summary: JNI bindings to the Subversion libraries
Requires: subversion = %{version}-%{release}
%{?_with_java:BuildRequires: java-devel}

%description javahl
This package includes the JNI bindings to the Subversion libraries.

%package ruby
Group: Development/Libraries
Summary: Ruby bindings to the Subversion libraries
%{!?_without_ruby:BuildRequires: ruby-devel >= 1.8.2, ruby >= 1.8.2}
Requires: subversion = %{version}-%{release}, ruby-libs >= 1.8.2
Requires: ruby(abi) = 1.8

%description ruby
This package includes the Ruby bindings to the Subversion libraries.

%prep
%setup -a 10
#patch1 -p1 -b .swig
%patch2 -p1 -b .deplibs
%patch3 -p1 -b .rpath
%{!?_without_pie:%patch6 -p1 -b .pie}
%{?_with_java:%patch7 -p1 -b .java}

%{__rm} -rf neon apr apr-util

echo _without_swig: %_without_swig
echo _without_pie: %_without_pie
echo dtag: %dtag

%build
%if %{!?_without_swig:1}0
cd swig-%{swig_version}
[ ! -r configure ] && ./autogen.sh
%configure --prefix="$(pwd)/install" --exec-prefix="$(pwd)/install" --bindir="$(pwd)/install/bin" --datadir="$(pwd)/install/share"
%{__make}
%{__make} install
cd -
%endif

./autogen.sh

# requirement for apr 0.9.7 seems to be bogus
%{__perl} -pi.orig -e 's|\.\[7-9\]|\.\[4-9\]|' configure

# fix shebang lines, #111498
%{__perl} -pi -e 's|/usr/bin/env perl -w|/usr/bin/perl -w|' tools/hook-scripts/*.pl.in

# override weird -shrext from ruby
export svn_cv_ruby_link="%{__cc} -shared"
export svn_cv_ruby_sitedir_libsuffix=""
export svn_cv_ruby_sitedir_archsuffix=""

export CC=gcc CXX=g++
%configure \
    --disable-mod-activation \
    --disable-neon-version-check \
    --disable-static \
    --with-apr="%{_prefix}" \
    --with-apr-util="%{_prefix}" \
    --with-apxs="%{_sbindir}/apxs" \
    --with-expat \
    --with-neon="%{_prefix}" \
    --with-ruby-sitedir="%{ruby_sitearch}" \
    --with-sasl="%{_prefix}" \
    --with-ssl \
%{!?_without_swig:--with-swig="swig-%{swig_version}/install"}
#    --disable-neon-version-check \
# 1.3.0 tarball ships with generated swig sources
#%{__make} extraclean-swig-headers swig-headers
%{__make} %{?_smp_mflags} all

%if %{!?_without_swig:1}0
%{__make} %{?_smp_mflags} swig-py swig-py-lib %{swigdirs}
%{__make} %{?_smp_mflags} swig-pl swig-pl-lib
%{!?_without_ruby:%{__make} %{?_smp_mflags} swig-rb swig-rb-lib}
%endif

%{?_with_java:%{_make} %{?_smp_mflags} javahl-java javahl-javah}
%{?_with_java:%{_make} %{?_smp_mflags} javahl}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%if %{!?_without_swig:1}0
%{__make} install-swig-py %{swigdirs} DESTDIR="%{buildroot}"
%{__make} install-swig-pl-lib DESTDIR="%{buildroot}"
%{!?_without_ruby:%{__make} install-swig-rb DESTDIR="%{buildroot}"}

%{__make} pure_vendor_install -C subversion/bindings/swig/perl/native \
        PERL_INSTALL_ROOT="%{buildroot}"
%endif

%{?_with_java:%{__make} install-javahl install-javahl-lib DESTDIR="%{buildroot}"}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/subversion

# Add subversion.conf configuration file into httpd/conf.d directory.
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/subversion.conf

# Remove unpackaged files
%{__rm} -rf %{buildroot}%{_includedir}/subversion-*/*.txt \
       %{buildroot}%{python_sitearch}/*/*.{a,la}

# remove stuff produced with Perl modules
find %{buildroot} -type f \
    -a \( -name .packlist -o \( -name '*.bs' -a -empty \) \) \
    -print0 | xargs -0 rm -f

# make Perl modules writable so they get stripped
find %{buildroot}%{_libdir}/perl5 -type f -perm 555 -print0 |
        xargs -0 chmod 0755

# unnecessary libraries for swig bindings
%{__rm} -f %{buildroot}%{_libdir}/libsvn_swig_*.{so,la,a}

# Trim what goes in docdir
%{__rm} -rf tools/*/*.in tools/test-scripts \
       doc/book/book/images/images doc/book/book/images/*.ppt

# Install psvn for emacs and xemacs
%{__install} -Dp -m0644 %{SOURCE4} %{buildroot}%{_datadir}/emacs/site-lisp/psvn.el
%{__install} -Dp -m0644 %{SOURCE4} %{buildroot}%{_datadir}/xemacs/site-packages/lisp/psvn.el

# Rename authz_svn INSTALL doc for docdir
ln -f subversion/mod_authz_svn/INSTALL mod_authz_svn-INSTALL

%find_lang %{name}

%if %{make_check}
%check
export LANG=C LC_ALL=C
%{__make} check CLEANUP=yes
%endif

find tools/ -type f -exec %{__chmod} -x {} \;

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post perl -p /sbin/ldconfig
%postun perl -p /sbin/ldconfig
%{!?_without_ruby:%post ruby -p /sbin/ldconfig}
%{!?_without_ruby:%postun ruby -p /sbin/ldconfig}
%{?_with_java:%post javahl -p /sbin/ldconfig}
%{?_with_java:%postun javahl -p /sbin/ldconfig}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COMMITTERS COPYING HACKING INSTALL README
%doc mod_authz_svn-INSTALL contrib/ subversion/LICENSE tools/
%doc %{_mandir}/man1/svn.1*
%doc %{_mandir}/man1/svnadmin.1*
%doc %{_mandir}/man1/svndumpfilter.1*
%doc %{_mandir}/man1/svnlook.1*
%doc %{_mandir}/man1/svnsync.1*
%doc %{_mandir}/man1/svnversion.1*
%doc %{_mandir}/man5/svnserve.conf.5*
%doc %{_mandir}/man8/svnserve.8*
%{_bindir}/svn
%{_bindir}/svnadmin
%{_bindir}/svndumpfilter
%{_bindir}/svnlook
%{_bindir}/svnserve
%{_bindir}/svnsync
%{_bindir}/svnversion
%{_libdir}/libsvn_*.so.*
%{_datadir}/emacs/site-lisp/
%{_datadir}/xemacs/site-packages/lisp/
%{!?_without_swig:%exclude %{_libdir}/libsvn_swig_perl*}
%{!?_without_swig:%exclude %{_mandir}/man3/*::*.3pm*}
%{!?_without_swig:%{python_sitearch}/svn/}
%{!?_without_swig:%{python_sitearch}/libsvn/}
%{!?_without_ruby:%exclude %{_libdir}/libsvn_swig_ruby*}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/subversion-1/
%{_libdir}/libsvn_*.la
%{_libdir}/libsvn_*.so
%{!?_without_swig:%exclude %{_libdir}/libsvn_swig_perl*}

%files -n mod_dav_svn
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/subversion.conf
%{_libdir}/httpd/modules/mod_dav_svn.so
%{_libdir}/httpd/modules/mod_authz_svn.so

%if %{!?_without_swig:1}0
%files perl
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*::*.3pm*
%{perl_vendorarch}/auto/SVN/
%{perl_vendorarch}/SVN/
%{_libdir}/libsvn_swig_perl*
%endif

%if %{!?_without_ruby:1}0
%files ruby
%defattr(-, root, root, 0755)
%{_libdir}/libsvn_swig_ruby*
%{ruby_sitearch}/svn/
%endif

%if %{?_with_java:1}0
%files javahl
%defattr(-, root, root, 0755)
%{_libdir}/libsvnjavahl-1.*
%{_libdir}/svn-javahl/
%endif

%changelog
* Tue Dec 23 2008 Dag Wieers <dag@wieers.com> - 1.5.5-0.1
- Updated to release 1.5.5.

* Sat Oct 25 2008 Dag Wieers <dag@wieers.com> - 1.5.4-0.1
- Updated to release 1.5.4.

* Sat Oct 11 2008 Dag Wieers <dag@wieers.com> - 1.5.3-0.1
- Updated to release 1.5.3.

* Tue Sep 02 2008 Dag Wieers <dag@wieers.com> - 1.5.2-0.1
- Updated to release 1.5.2.

* Thu Jul 31 2008 Dag Wieers <dag@wieers.com> - 1.5.1-0.1
- Updated to release 1.5.1.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.5.0-0.1
- Updated to release 1.5.0.

* Mon Dec 31 2007 Dag Wieers <dag@wieers.com> - 1.4.6-0.1
- Updated to release 1.4.6.

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 1.4.4-0.1
- Updated to release 1.4.4.

* Thu Jan 25 2007 Dag Wieers <dag@wieers.com> - 1.4.3-0.1
- Updated to release 1.4.3.

* Wed Nov 08 2006 Dag Wieers <dag@wieers.com> - 1.4.2-0.1
- Updated to release 1.4.2.

* Tue Aug 01 2006 Dag Wieers <dag@wieers.com> - 1.3.2-0.1
- Updated to release 1.3.2.

* Wed Jul 13 2005 Dag Wieers <dag@wieers.com> - 1.2.1-0.1
- Updated to release 1.2.1.

* Mon Jun 06 2005 Dag Wieers <dag@wieers.com> - 1.2.0-0.2
- Moved perl examples to subversion-perl.

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 1.2.0-0.1
- Updated to release 1.2.0.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 1.1.4-0.1
- Updated to release 1.1.4.

* Sat Jan 15 2005 Dag Wieers <dag@wieers.com> - 1.1.3-0.1
- Updated to release 1.1.3.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 1.1.2-0.1
- Updated to release 1.1.2.

* Sat Dec 04 2004 Dag Wieers <dag@wieers.com> - 1.1.1-0.1
- Updated to release 1.1.1.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 1.0.9-2
- Backported changes from Red Hat's EL3 packages. (Joe Orton)

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 1.0.9-1
- Updated to release 1.0.9.

* Thu Sep 23 2004 Dag Wieers <dag@wieers.com> - 1.0.8-1
- Updated to release 1.0.8.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Updated to release 1.0.7.

* Fri Jun 11 2004 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Sat May 22 2004 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

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
