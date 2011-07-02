# $Id$
# Authority: dfateyev
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name LEOCHARRE-Dir

Summary: LEOCHARRE-Dir module for perl
Name: perl-LEOCHARRE-Dir
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LEOCHARRE-Dir/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEOCHARRE/LEOCHARRE-Dir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(File::Path) >= 2.07

%description
LEOCHARRE-Dir module for perl

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
%doc Changes INSTALL MANIFEST META.yml
%doc %{_mandir}/man?/*
%{perl_vendorlib}/LEOCHARRE/

%changelog
* Mon May 23 2011 Denis Fateyev <denis@fateyev.com> - 1.08-1
- Initial package.

