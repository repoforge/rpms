# $Id: $

# Authority: dries
# Upstream:

%define real_name Gnome2-Vte
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to the Virtual Terminal Emulation library
Name: perl-Gnome2-Vte
Version: 0.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gnome2-Vte/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RM/RMCFARLA/Gtk2-Perl/Gnome2-Vte-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-ExtUtils-Depends, perl-ExtUtils-PkgConfig, perl-Glib, perl-Gtk2, pgkconfig

%description
This module allows you to use the Virtual Terminal Emulation library (libvte
for short) from Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README LICENSE ChangeLog
%{_mandir}/man3/*
%exclude %{perl_archlib}/perllocal.pod
%{perl_vendorarch}/Gnome2/Vte.pm
%{perl_vendorarch}/Gnome2/Vte
%{perl_vendorarch}/auto/Gnome2/Vte/Vte.bs
%{perl_vendorarch}/auto/Gnome2/Vte/Vte.so
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
