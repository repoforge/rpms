# $Id$

# Authority: dries
# Upstream: Vipul Ved Prakash <mail$vipul,net>


%define real_name Net-XWhois
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Whois Client Interface
Name: perl-Net-XWhois
Version: 0.90
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-XWhois/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/sv

Source: http://search.cpan.org/CPAN/authors/id/V/VI/VIPUL/Net-XWhois-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains a Whois Client Interface for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc TODO ARTISTIC Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Net/XWhois.pm

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.90-1
- Initial package.
