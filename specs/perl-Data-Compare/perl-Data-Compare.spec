# $Id$
# Authority: dries
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Compare

Summary: Compare perl data structures
Name: perl-Data-Compare
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Compare/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCANTRELL/Data-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module compares arbitrary data structures to see if they are copies
of each other.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Data/Compare.pm
%{perl_vendorlib}/Data/Compare

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Initial package.

