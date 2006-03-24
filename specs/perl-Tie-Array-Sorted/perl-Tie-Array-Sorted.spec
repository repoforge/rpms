# $Id$
# Authority: dries
# Upstream: Tony Bowden <tonu$tmtm,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Array-Sorted

Summary: Sorted array
Name: perl-Tie-Array-Sorted
Version: 1.4
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Array-Sorted/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-Array-Sorted-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
An array which is kept sorted.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Tie/
%dir %{perl_vendorlib}/Tie/Array/
%{perl_vendorlib}/Tie/Array/Sorted.pm
%{perl_vendorlib}/Tie/Array/Sorted

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
