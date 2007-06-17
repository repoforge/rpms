# $Id$
# Authority: dries
# Upstream: Abhijit Menon-Sen <ams$wiw,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-NULL

Summary: NULL Encryption Algorithm
Name: perl-Crypt-NULL
Version: 1.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-NULL/

Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMS/Crypt-NULL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
The NULL Encryption Algorithm is a symmetric block cipher described
in RFC 2410 by Rob Glenn and Stephen Kent.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/NULL.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
