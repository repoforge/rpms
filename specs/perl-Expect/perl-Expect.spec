# $Id$

# Authority: dries
# Upstream: Roland Giersig <RGiersig$cpan,org>


%define real_name Expect
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Expect for perl
Name: perl-Expect
Version: 1.15
Release: 2.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Expect/

Source: http://www.cpan.org/modules/by-module/Expect/Expect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains a version of expect written in perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Expect/.packlist
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Expect.pm
%{perl_vendorlib}/Expect.pod

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-2.2
- Rebuild for Fedora Core 5.

* Thu Nov 04 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-2
- Removed bad dependency (found by Martijn Lievaart, thanks!)

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
