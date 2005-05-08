# $Id: rrdtool.spec 3101 2005-04-04 20:13:17Z dag $
# Authority: matthias
# Upstream: Tobi Oetiker <oetiker$ee,ethz,ch>

# Tag: test

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Round Robin Database Tool to store and display time-series data
Name: rrdtool
Version: 1.2.2
Release: 1
License: GPL
Group: Applications/Databases
URL: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/

Source: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/rrdtool-%{version}.tar.gz
Patch: rrdtool-1.0.48-php_config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, openssl-devel, libart_lgpl-devel >= 2.0, cgilib-devel
BuildRequires: libpng-devel, zlib-devel, freetype-devel
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
Summary: RRDtool Perl interface
Group: Development/Languages
Requires: %{name} = %{version}
Obsoletes: rrdtool-perl <= %{version}

%description -n perl-rrdtool
The RRDtools Perl modules.

%package -n php-rrdtool
Summary: RRDtool module for PHP
Group: Development/Languages
Requires: %{name} = %{version}, php >= 4.0

%description -n php-rrdtool
The php-%{name} package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.

%prep
%setup

### FIXME: Fixes to /usr/lib(64) for x86_64
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure Makefile.in

%build
%configure \
	--enable-perl-site-install \
	--with-perl-options="PREFIX=\"%{buildroot}%{_prefix}\" INSTALLDIRS=\"vendor\""
#	--with-tcllib="%{_libdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### We only want .txt and .html files for the main documentation
%{__mkdir_p} doc2/doc/
%{__cp} -ap doc/*.txt doc/*.html doc2/doc/

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist
%{__rm} -f %{buildroot}%{perl_vendorarch}/ntmake.pl

%clean
%{__rm} -rf %{buildroot}
 
%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS COPYING COPYRIGHT NEWS README THREADS TODO doc2/doc/
%doc %{_mandir}/man1/*.1*
%{_bindir}/rrdcgi
%{_bindir}/rrdtool
%{_bindir}/rrdupdate
%{_libdir}/librrd.so.*
%{_libdir}/librrd_th.so.*
%{_datadir}/rrdtool/
%exclude %{_prefix}/shared/

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
%exclude %{_prefix}/examples/

%changelog
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

