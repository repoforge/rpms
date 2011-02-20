# $Id$
# Authority: dfateyev
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name LEOCHARRE-Strings

Summary: LEOCHARRE-Strings module for perl
Name: perl-LEOCHARRE-Strings
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LEOCHARRE-Strings/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/LEOCHARRE-Strings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(String::Prettify)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
LEOCHARRE-Strings module for perl

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/LEOCHARRE/

%changelog
* Sun Feb 20 2011 Denis Fateyev <denis@fateyev.com> - 1.02-1
- Initial package.

