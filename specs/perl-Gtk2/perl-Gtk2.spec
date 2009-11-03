# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2

Summary: Perl interface to the 2.x series of the Gimp Toolkit library
Name: perl-Gtk2
Version: 1.221
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0.0
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Cairo)
Buildrequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib) >= 1.0.0
BuildRequires: perl(Pango)
Requires: perl >= 2:5.8.0

%description
Perl bindings to the 2.x series of the Gtk+ widget set.  This module allows you
to write graphical user interfaces in a perlish and object-oriented way, freeing
you from the casting and memory management in C, yet remaining very close in
spirit to original API.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README TODO copyright.pod examples/
%doc %{_mandir}/man3/Gtk2.3pm*
%doc %{_mandir}/man3/Gtk2::*.3pm*
%{perl_vendorarch}/auto/Gtk2/
%{perl_vendorarch}/Gtk2/
%{perl_vendorarch}/Gtk2.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.221-1
- Updated to version 1.221.

* Sun May 10 2009 Dag Wieers <dag@wieers.com> - 1.220-1
- Updated to release 1.220.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.200-1
- Updated to release 1.200.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.183-1
- Updated to release 1.183.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.182-1
- Updated to release 1.182.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.180-1
- Updated to release 1.180.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.164-1
- Updated to release 1.164.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.162-1
- Updated to release 1.162.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.161-1
- Updated to release 1.161.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.146-1
- Updated to release 1.146.
- Disabled auto-requires for examples/ and gtk-demo/.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.141-1
- Updated to release 1.141.

* Tue Dec 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.102-1
- Updated to release 1.102.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.101-1
- Updated to release 1.101.

* Tue Mar 08 2005 Dag Wieers <dag@wieers.com> - 1.080-1
- Updated to release 1.080.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 1.062-1
- Updated to release 1.062.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 1.040-0
- Updated to release 1.040.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.023-0
- Updated to release 1.023.

* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 1.00-0
- Updated to release 1.00.

* Sun Sep 10 2003 Dag Wieers <dag@wieers.com> - 0.97-0
- Updated to release 0.97.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Updated to release 0.96.

* Fri Aug 22 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Updated to release 0.95.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 0.94-0
- Updated to release 0.94.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 0.93-0
- Updated to release 0.93.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 0.92-0
- Updated to release 0.92.

* Sun Jul 27 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.90-0
- Initial package. (using DAR)
