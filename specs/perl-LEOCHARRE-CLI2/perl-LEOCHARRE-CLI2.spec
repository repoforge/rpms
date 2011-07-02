# $Id$
# Authority: dfateyev
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name LEOCHARRE-CLI2

Summary: LEOCHARRE-CLI2 module for perl
Name: perl-LEOCHARRE-CLI2
Version: 1.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LEOCHARRE-CLI2/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/LEOCHARRE-CLI2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Devel::Symdump) >= 2.07
BuildRequires: perl(Getopt::Std::Strict) >= 1.01
BuildRequires: perl(LEOCHARRE::Dir) >= 1.06
BuildRequires: perl(Smart::Comments) >= 1.0
BuildRequires: perl(String::ShellQuote) >= 1.03
BuildRequires: perl(YAML) >= 0.66
BuildRequires: perl(ExtUtils::MakeMaker)

%description
LEOCHARRE-CLI2 module for perl

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/LEOCHARRE/

%changelog
* Mon May 23 2011 Denis Fateyev <denis@fateyev.com> - 1.16-1
- Initial package.

