# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-TrayIcon

Summary: Interface to the EggTrayIcon library
Name: perl-Gtk2-TrayIcon
Version: 0.03
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-TrayIcon/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-TrayIcon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-ExtUtils-Depends, perl-ExtUtils-PkgConfig
BuildRequires: perl-Glib, perl-Gtk2, pkgconfig, gtk2-devel, perl(Cairo::Install::Files)

%description
This module contains a perl interface to the EggTrayIcon library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc TODO
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Gtk2/
%{perl_vendorarch}/Gtk2/TrayIcon.pm
%{perl_vendorarch}/Gtk2/TrayIcon/
%dir %{perl_vendorarch}/auto/Gtk2/
%{perl_vendorarch}/auto/Gtk2/TrayIcon/

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
