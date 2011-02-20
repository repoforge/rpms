# $Id$
# Authority: dfateyev
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Prettify

Summary: String-Prettify module for perl
Name: perl-String-Prettify
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Prettify/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/String-Prettify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Simple)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
String-Prettify module for perl

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
%doc MANIFEST META.yml
%doc %{_mandir}/man?/*
%{perl_vendorlib}/String/

%changelog
* Sun Feb 20 2011 Denis Fateyev <denis@fateyev.com> - 1.04-1
- Initial package.

