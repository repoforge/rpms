# $Id$
# Authority: dag
# Upstream: <gtk-perl-list$gnome,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2

Summary: Perl interface to the 2.x series of the Gimp Toolkit library
Name: perl-Gtk2
Version: 1.141
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0, perl(Glib) >= 1.0.0, perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires: gtk2-devel >= 2.0.0
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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE MANIFEST NEWS README TODO examples/ gtk-demo/
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Gtk2/
%{perl_vendorarch}/Gtk2.pm
%{perl_vendorarch}/auto/Gtk2/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.141-1
- Updated to release 1.141.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.102-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.102-1
- Updated to release 1.102.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.101-1
- Updated to release 1.101.

* Tue Mar 08 2005 Dag Wieers <dag@wieers.com> - 1.080-1 - $Rev$
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
