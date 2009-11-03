# set to zero to avoid running test suite
%define make_check 1

%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Modern Version Control System designed to replace CVS
Name: subversion
Version: 1.1.1
Release: 1.1%{?dist}
License: BSD
Group: Development/Tools
URL: http://subversion.tigris.org/
Source0: http://subversion.tigris.org/tarballs/subversion-%{version}.tar.gz
Source1: subversion.conf
Source3: filter-requires.sh
Source4: http://www.xsteve.at/prg/emacs/psvn.el
Patch1: subversion-0.24.2-swig.patch
Patch2: subversion-0.20.1-deplibs.patch
Patch3: subversion-0.31.0-rpath.patch
Patch6: subversion-1.0.3-pie.patch
BuildPreReq: autoconf, libtool, python, python-devel, texinfo
BuildPreReq: db4-devel >= 4.1.25, swig >= 1.3.21-5, docbook-style-xsl
BuildPreReq: apr-devel, apr-util-devel, neon-devel >= 0:0.24.7-1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: python-subversion = %{version}-%{release}
Provides: subversion-python = %{version}-%{release}

%define __perl_requires %{SOURCE3}

# Put Python bindings in site-packages
%define pydir %(python -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define swigdirs swig_pydir=%{pydir}/libsvn swig_pydir_extra=%{pydir}/svn

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
BuildRequires: perl >= 2:5.8.0
Requires: %(eval `perl -V:version`; echo "perl(:MODULE_COMPAT_$version)")
Requires: subversion = %{version}-%{release}

%description perl
This package includes the Perl bindings to the Subversion libraries.

%prep
%setup -q
%patch1 -p1 -b .swig
%patch2 -p1 -b .deplibs
%patch3 -p1 -b .rpath
%patch6 -p1 -b .pie

rm -rf neon apr apr-util db4

%build
./autogen.sh

# requirement for apr 0.9.5 seems to be bogus
perl -pi -e 's/\.\[5-9\]/\.\[4-9\]/' configure

# fix shebang lines, #111498
perl -pi -e 's|/usr/bin/env perl -w|/usr/bin/perl -w|' tools/hook-scripts/*.pl.in

export CC=gcc CXX=g++
%configure --with-apr=%{_prefix} --with-apr-util=%{_prefix} \
	--with-swig --with-neon=%{_prefix} \
        --with-apxs=%{_sbindir}/apxs --disable-mod-activation
make %{?_smp_mflags} all swig-py %{swigdirs}
make swig-pl

%install
%{__rm} -rf %{buildroot}
make install install-swig-py install-swig-pl-lib \
        DESTDIR=$RPM_BUILD_ROOT %{swigdirs}

make pure_vendor_install -C subversion/bindings/swig/perl/native \
        PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

# Add subversion.conf configuration file into httpd/conf.d directory.
install -m 755 -d ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/subversion.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d

# Remove unpackaged files
rm -rf ${RPM_BUILD_ROOT}%{_includedir}/subversion-*/*.txt \
       ${RPM_BUILD_ROOT}%{pydir}/*/*.{a,la}

# remove stuff produced with Perl modules
find $RPM_BUILD_ROOT -type f \
    -a \( -name .packlist -o \( -name '*.bs' -a -empty \) \) \
    -print0 | xargs -0 rm -f

# make Perl modules writable so they get stripped
find $RPM_BUILD_ROOT%{_libdir}/perl5 -type f -perm 555 -print0 |
        xargs -0 chmod 755

# unnecessary libraries for swig bindings
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libsvn_swig_*.{so,la,a}

# Trim what goes in docdir
rm -rf tools/*/*.in tools/test-scripts \
       doc/book/book/images/images doc/book/book/images/*.ppt

# Install psvn for emacs and xemacs
for f in emacs/site-lisp xemacs/site-packages/lisp; do
  install -m 755 -d ${RPM_BUILD_ROOT}%{_datadir}/$f
  install -m 644 $RPM_SOURCE_DIR/psvn.el ${RPM_BUILD_ROOT}%{_datadir}/$f
done

# Rename authz_svn INSTALL doc for docdir
ln -f subversion/mod_authz_svn/INSTALL mod_authz_svn-INSTALL

%find_lang %{name}

%if %{make_check}
%check
make check check-swig-pl CLEANUP=yes
%endif

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post perl -p /sbin/ldconfig

%postun perl -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COMMITTERS COPYING HACKING INSTALL README
%doc mod_authz_svn-INSTALL subversion/LICENSE tools
%doc doc/book/book/images doc/book/book/svn-book.html
%doc contrib/client-side/svn_load_dirs{.pl,_*,.README}
%{_bindir}/*
%{_libdir}/libsvn_*.so.*
%{_mandir}/man*/*
%{pydir}/svn
%{pydir}/libsvn
%{_datadir}/emacs/site-lisp
%{_datadir}/xemacs/site-packages/lisp
%exclude %{_libdir}/libsvn_swig_perl*
%exclude %{_mandir}/man*/*::*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/subversion-1
%{_libdir}/libsvn*.a
%{_libdir}/libsvn*.la
%{_libdir}/libsvn*.so
%exclude %{_libdir}/libsvn_swig_perl*

%files -n mod_dav_svn
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/subversion.conf
%{_libdir}/httpd/modules/mod_dav_svn.so
%{_libdir}/httpd/modules/mod_authz_svn.so

%files perl
%defattr(-, root, root, 0755)
%{perl_vendorarch}/auto/SVN
%{perl_vendorarch}/SVN
%{_libdir}/libsvn_swig_perl*
%{_mandir}/man*/*::*

%changelog
* Mon Nov  1 2004 Joe Orton <jorton@redhat.com> 1.1.1-1.1
- rebuild

* Tue Oct 26 2004 Joe Orton <jorton@redhat.com> 1.1.1-1
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
