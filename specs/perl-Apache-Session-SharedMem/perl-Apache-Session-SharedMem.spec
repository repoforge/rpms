# $Id$
# Authority: dries
# Upstream: Simon Wistow <simon$thegestalt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Session-SharedMem

Summary: Session management via shared memory
Name: perl-Apache-Session-SharedMem
Version: 0.6
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Session-SharedMem/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Session-SharedMem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is an Apache::Session extension module that stores the
session data in Shared memory (so, does exactly what it says
on the tin then) using IPC::Cache (and hence IPC::ShareLite).

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
%{perl_vendorlib}/Apache/Session/SharedMem.pm
%{perl_vendorlib}/Apache/Session/Store

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
