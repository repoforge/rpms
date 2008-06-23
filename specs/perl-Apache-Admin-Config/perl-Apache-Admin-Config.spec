# $Id$
# Authority: dries
# Upstream: Olivier Poitrey <rs-pause$rhapsodyk,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Admin-Config

Summary: Read/write Apache like configuration files
Name: perl-Apache-Admin-Config
Version: 0.94
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Admin-Config/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Admin-Config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
"Apache::Admin::Config" provides an object oriented interface for
reading and writing Apache-like configuration files without affecting
comments, indentation, or truncated lines.

You can easily extract informations from the apache configuration, or
manage htaccess files.

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
%{perl_vendorlib}/Apache/Admin/Config.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Updated to release 0.94.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- Initial package.
