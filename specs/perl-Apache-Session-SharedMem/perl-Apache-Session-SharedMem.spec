# $Id$
# Authority: dries
# Upstream: Simon Wistow <simon$thegestalt,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Session-SharedMem

Summary: Session management via shared memory
Name: perl-Apache-Session-SharedMem
Version: 0.6
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Session-SharedMem/

Source: http://search.cpan.org/CPAN/authors/id/S/SI/SIMONW/Apache-Session-SharedMem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/Session/SharedMem.pm
%{perl_vendorlib}/Apache/Session/Store

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
