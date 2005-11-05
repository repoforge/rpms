# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-English

Summary: Create regular expressions more verbosely
Name: perl-Regexp-English
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-English/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/Regexp-English-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl module to create regular expressions more verbosely.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Regexp/English.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Updated to release 1.00.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
