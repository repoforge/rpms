# $Id$

# Authority: dries
# Upstream: Aaron Straup Cope <ascope$cpan,org>

%define real_name Net-Google
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to the Google SOAP API
Name: perl-Net-Google
Version: 1.0
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Google/

Source: http://www.cpan.org/modules/by-module/Net/Net-Google-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A simple OOP interface to the Google SOAP API.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Google.pm
%{perl_vendorlib}/Net/Google/*

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Initial package.
