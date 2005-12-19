# $Id: rrdtool.spec 3101 2005-04-04 20:13:17Z dag $
# Authority: matthias
# Upstream: Tobi Oetiker <oetiker$ee,ethz,ch>

# Tag: test

%{?fc1:%define _without_python 1}
%{?el3:%define _without_python 1}

%{?rh9:%define _without_python 1}
%{?rh9:%define _without_tcltk_devel 1}

%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_version %(%{__python} -c 'import string, sys; print string.split(sys.version, " ")[0]')

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.2.12
Release: 1
License: GPL
Group: Applications/Databases
URL: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/

Source: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/rrdtool-%{version}.tar.gz
Patch: rrdtool-1.2.12-tclrrd.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, openssl-devel, libart_lgpl-devel >= 2.0, cgilib-devel
BuildRequires: libpng-devel, zlib-devel, freetype-devel
%{!?_without_python:BuildRequires: python-devel >= 2.3}
%{!?_without_tcltk_devel:BuildRequires: tcl-devel, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl, tk}
Requires: perl >= %(rpm -q --qf '%%{epoch}:%%{version}' perl)

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

%description -n perl-rrdtool
The Perl RRDtool bindings

%package -n tcl-rrdtool
Summary: TCL bindings
Group: Development/Languages
Requires: %{name} = %{version}
Obsoletes: rrdtool-tcl <= %{version}

%description -n tcl-rrdtool
The TCL RRDtool bindings

%package -n python-rrdtool
Summary: Python RRDtool bindings
Group: Development/Languages
BuildRequires: python
Requires: python >= %{python_version}
Requires: %{name} = %{version}

%description -n python-rrdtool
Python RRDtool bindings.

%package -n php-rrdtool
Summary: RRDtool module for PHP
Group: Development/Languages
Requires: %{name} = %{version}, php >= 4.0

%description -n php-rrdtool
The php-%{name} package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.

%prep
%setup
%patch0 -p0

### FIXME: Fixes to /usr/lib(64) for x86_64. (Fix upstream)
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure Makefile.in

%build
%configure \
	--enable-perl-site-install \
	--with-perl-options='INSTALLDIRS="vendor" DESTDIR="" PREFIX="%{buildroot}%{_prefix}"'
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
	pkglibdir="%{_datadir}/tclrrd1.2.11" \
	pythondir="%{python_sitearch}"
### FIXME: pkglibdir ends up being "/usr/lib /usr/share/tclrrd1.2.11" on EL4 (Fix upstream)
### FIXME: pythondir is /usr/lib on 64bit too, should be /usr/lib64 (Fix upstream)

### FIXME: Another dirty hack to install perl modules with old and new perl-ExtUtils-MakeMaker (Fix upstream)
%{__rm} -rf %{buildroot}%{buildroot}
%{__make} -C bindings/perl-piped install INSTALLDIRS="vendor" DESTDIR="" PREFIX="%{buildroot}%{_prefix}"
%{__make} -C bindings/perl-shared install INSTALLDIRS="vendor" DESTDIR="" PREFIX="%{buildroot}%{_prefix}"

### We only want .txt and .html files for the main documentation
%{__mkdir_p} rpm-doc/docs/
%{__cp} -ap doc/*.txt doc/*.html rpm-doc/docs/

%{__rm} -f examples/Makefile* examples/*.in

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist
%{__rm} -f %{buildroot}%{perl_vendorarch}/ntmake.pl

%clean
%{__rm} -rf %{buildroot}
 
%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS COPYING COPYRIGHT NEWS README THREADS TODO
### FIXME: examples/ includes scripts that require perl-rrdtool (circular dependency)
%doc examples/ rpm-doc/docs/
%doc %{_mandir}/man1/*.1*
%{_bindir}/rrdcgi
%{_bindir}/rrdtool
%{_bindir}/rrdupdate
%{_libdir}/librrd.so.*
%{_libdir}/librrd_th.so.*
%{_datadir}/rrdtool/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/rrd.h
%{_libdir}/librrd.a
%{_libdir}/librrd_th.a
%exclude %{_libdir}/librrd.la
%exclude %{_libdir}/librrd_th.la
%{_libdir}/librrd.so
%{_libdir}/librrd_th.so

%files -n perl-rrdtool
%defattr(-, root, root, 0755)
%doc examples/
%doc %{_mandir}/man3/RRDp.3*
%doc %{_mandir}/man3/RRDs.3*
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%{perl_vendorarch}/auto/RRDs/

%files -n tcl-rrdtool
%defattr(-, root, root, 0755)
%{_libdir}/tclrrd%{version}.so
#%{_datadir}/tclrrd%{version}/ifOctets.tcl
#%{_datadir}/tclrrd%{version}/pkgIndex.tcl
%{_datadir}/tclrrd1.2.11/ifOctets.tcl
%{_datadir}/tclrrd1.2.11/pkgIndex.tcl

%if %{!?_without_python:1}0
%files -n python-rrdtool
%defattr(-, root, root, 0755)
%{python_sitearch}/rrdtoolmodule.so
%endif

%changelog
* Mon Dec 19 2005 Dag Wieers <dag@wieers.com> - 1.2.12-1
- Updated to release 1.2.12.

* Wed Jul 27 2005 Dag Wieers <dag@wieers.com> - 1.2.11-1
- Updated to release 1.2.11.
- Fixes for x86_64 and perl/tcl/python bindings.

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 1.2.9-1
- Updated to release 1.2.9.

* Wed May 18 2005 Dag Wieers <dag@wieers.com> - 1.2.8-1
- Updated to release 1.2.8.

* Tue May 10 2005 Dag Wieers <dag@wieers.com> - 1.2.6-1
- Updated to release 1.2.6.

* Sat May 07 2005 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Sat May 07 2005 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

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

