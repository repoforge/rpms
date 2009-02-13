# $Id: rrdtool.spec 3101 2005-04-04 20:13:17Z dag $
# Authority: matthias
# Upstream: Tobi Oetiker <oetiker$ee,ethz,ch>

%{?fc1:%define _without_python 1}
%{?el3:%define _without_python 1}

%{?rh9:%define _without_python 1}
%{?rh9:%define _without_ruby 1}
%{?rh9:%define _without_tcltk_devel 1}

%{?rh7:%define _without_python 1}
%{?rh7:%define _without_ruby 1}
%{?rh7:%define _without_tcltk_devel 1}

%{?el2:%define _without_python 1}
%{?el2:%define _without_ruby 1}
%{?el2:%define _without_tcltk_devel 1}

%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_version %(%{__python} -c 'import string, sys; print string.split(sys.version, " ")[0]')
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
%define ruby_archdir %(ruby -rrbconfig -e "puts Config::CONFIG['archdir']")

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.2.30
Release: 1
License: GPL
Group: Applications/Databases
URL: http://oss.oetiker.ch/rrdtool/

Source0: http://oss.oetiker.ch/rrdtool/pub/rrdtool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, openssl-devel, cgilib-devel, libart_lgpl-devel >= 2.0
BuildRequires: libpng-devel, zlib-devel, freetype-devel
%{!?_without_python:BuildRequires: python-devel >= 2.3}
%{!?_without_ruby:BuildRequires: ruby, ruby-devel}
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
Obsoletes: rrdtool-perl <= %{version}-%{release}
Provides: rrdtool-perl = %{version}-%{release}

%description -n perl-rrdtool
The Perl RRDtool bindings

%package -n tcl-rrdtool
Summary: TCL bindings
Group: Development/Languages
Requires: %{name} = %{version}
Obsoletes: rrdtool-tcl <= %{version}-%{release}
Provides: rrdtool-tcl = %{version}-%{release}

%description -n tcl-rrdtool
The TCL RRDtool bindings

%package -n python-rrdtool
Summary: Python RRDtool bindings
Group: Development/Languages
BuildRequires: python
Requires: python >= %{python_version}
Requires: %{name} = %{version}
Obsoletes: rrdtool-python <= %{version}-%{release}
Provides: rrdtool-python = %{version}-%{release}

%description -n python-rrdtool
Python RRDtool bindings.

%package -n php-rrdtool
Summary: RRDtool module for PHP
Group: Development/Languages
Requires: %{name} = %{version}, php >= 4.0
Obsoletes: rrdtool-php <= %{version}-%{release}
Provides: rrdtool-php = %{version}-%{release}

%description -n php-rrdtool
The php-%{name} package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.

%package -n ruby-rrdtool
Summary: RRDtool module for Ruby
Group: Development/Languages
Requires: %{name} = %{version}, ruby-devel
Obsoletes: rrdtool-ruby <= %{version}-%{release}
Provides: rrdtool-ruby = %{version}-%{release}

%description -n ruby-rrdtool
The ruby-%{name} package includes a library that implements RRDtool bindings
for the Ruby language.

%prep
%setup

### FIXME: Fixes to /usr/lib(64) for x86_64. (Fix upstream)
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure Makefile.in php4/configure php4/ltconfig*

### Fix to find correct python dir on lib64
%{__perl} -pi.orig -e 's|get_python_lib\(0,0,prefix|get_python_lib\(1,0,prefix|g' configure

%build
%configure \
%{?_without_python:--disable-python} \
%{?_without_ruby:--disable-ruby} \
	--disable-static \
%{?_without_tcl:--disable-tcl} \
	--enable-perl-site-install \
%{!?_without_python:--enable-python} \
%{!?_without_ruby:--enable-ruby} \
	--enable-ruby-site-install \
%{!?_without_tcl:--enable-tcl} \
	--enable-tcl-site \
	--with-perl-options='INSTALLDIRS="vendor" DESTDIR="" PREFIX="%{buildroot}%{_prefix}"' \
	--with-pic \
	--with-tcllib="%{_libdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### FIXME: Another dirty hack to install perl modules with old and new perl-ExtUtils-MakeMaker (Fix upstream)
%{__rm} -rf %{buildroot}%{buildroot}
%{__make} -C bindings/perl-piped install INSTALLDIRS="vendor" DESTDIR="" PREFIX="%{buildroot}%{_prefix}"
%{__make} -C bindings/perl-shared install INSTALLDIRS="vendor" DESTDIR="" PREFIX="%{buildroot}%{_prefix}"

### FIXME: Another dirty hack to install ruby files if they're available
if [ -f bindings/ruby/RRD.so ]; then
	%{__install} -Dp -m0755 bindings/ruby/RRD.so %{buildroot}%{ruby_sitearch}/RRD.so
	%{__rm} -rf %{buildroot}%{ruby_archdir}
fi

### We only want .txt and .html files for the main documentation
%{__mkdir_p} rpm-doc/docs/
%{__cp} -ap doc/*.txt doc/*.html rpm-doc/docs/

### Clean up examples dir
%{__rm} -f examples/Makefile* examples/*.in
find examples/ -type f -exec chmod 0644 {} \;
find examples/ -type f -exec %{__perl} -pi -e 's|^#! \@perl\@|#!%{__perl}|gi' {} \;
find examples/ -name "*.pl" -exec %{__perl} -pi -e 's|\015||gi' {} \;

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist
%{__rm} -f %{buildroot}%{perl_vendorarch}/ntmake.pl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS COPYING COPYRIGHT NEWS README THREADS TODO
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
%{_libdir}/librrd.so
%{_libdir}/librrd_th.so
%exclude %{_libdir}/librrd.la
%exclude %{_libdir}/librrd_th.la

%files -n perl-rrdtool
%defattr(-, root, root, 0755)
%doc bindings/perl-shared/MANIFEST bindings/perl-shared/README
%doc %{_mandir}/man3/RRDp.3*
%doc %{_mandir}/man3/RRDs.3*
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/RRDs.pm
%{perl_vendorarch}/auto/RRDs/

%files -n tcl-rrdtool
%defattr(-, root, root, 0755)
%doc bindings/tcl/README
%{_libdir}/tclrrd%{version}.so
%{_libdir}/rrdtool/ifOctets.tcl
%{_libdir}/rrdtool/pkgIndex.tcl

%if %{!?_without_python:1}0
%files -n python-rrdtool
%defattr(-, root, root, 0755)
%doc bindings/python/ACKNOWLEDGEMENT bindings/python/AUTHORS bindings/python/COPYING bindings/python/README
%{python_sitearch}/rrdtoolmodule.so
%endif

%if %{!?_without_ruby:1}0
%files -n ruby-rrdtool
%defattr(-, root, root, 0755)
%doc bindings/ruby/CHANGES bindings/ruby/README
%{ruby_sitearch}/RRD.so
%endif

%changelog
* Fri Feb 13 2009 Christoph Maser <cmr@financial.com> - 1.2.30
- Update to 1.2.30

* Mon Dec 29 2008 Christoph Maser <cmr@financial.com> - 1.2.29-1
- Update to 1.2.29
- Remove fontpath patch as the problem is fixed in this release 

* Fri Dec 12 2008 Christoph Maser <cmr@financial.com> - 1.2.28-2
- Remove unused patches
- Add fontpath patch (http://oss.oetiker.ch/rrdtool-trac/changeset/1653)

* Wed Oct 15 2008 Christoph Maser <cmr@financial.com> - 1.2.28-1
- Updated to release 1.2.28.

* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 1.2.27-1
- Updated to release 1.2.27.

* Wed Jun 06 2007 Dag Wieers <dag@wieers.com> - 1.2.23-1
- Updated to release 1.2.23.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.2.21-1
- Updated to release 1.2.21.

* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 1.2.18-1
- Updated to release 1.2.18.

* Wed Jul 19 2006 Dag Wieers <dag@wieers.com> - 1.2.15-1
- Updated to release 1.2.15.

* Fri May 05 2006 Dag Wieers <dag@wieers.com> - 1.2.13-1
- Updated to release 1.2.13.

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

