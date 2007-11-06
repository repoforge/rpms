# $Id$
# Authority: dries
# Upstream: Jeffrey Baker <jwbaker$acm,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Session

Summary: Session data persistence
Name: perl-Apache-Session
Version: 1.81
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Session/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl-DBI

%description
These modules provide persistent storage for arbitrary data, in arbitrary
backing stores.  The details of interacting with the backing store are
abstracted to make all backing stores behave alike.  The programmer simply
interacts with a tied hash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README TODO
%{_mandir}/man3/*
%{perl_vendorlib}/Apache/Session.pm
%{perl_vendorlib}/Apache/Session/*

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.81-1
- Updated to release 1.81.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.80-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Updated to release 1.80.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.

