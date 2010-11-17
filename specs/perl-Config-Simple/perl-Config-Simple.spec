# $Id$
# Authority: dries
# Upstream: Sherzod Ruzmetov <sherzodr$cpan,org>

### EL6 ships with perl-Config-Simple-4.59-5.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Simple

Summary: Simple configuration file class
Name: perl-Config-Simple
Version: 4.59
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Simple/

Source: http://www.cpan.org/modules/by-module/Config/Config-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Config::Simple is a class representing configuration file object. It
supports several configuration file syntax and tries to identify the
file syntax to parse them accordingly. Library supports parsing,
updating and creating configuration files.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Config/Simple.pm
%{perl_vendorlib}/auto/Config/Simple

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 4.59-1
- Updated to release 4.59.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 4.58-1
- Initial package.
