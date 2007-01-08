# $Id$
# Authority: dries
# Upstream: S&#233;bastien Aperghis-Tramoni <maddingue$free,fr>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-FindFunctions

Summary: Find functions in external libraries
Name: perl-ExtUtils-FindFunctions
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-FindFunctions/

Source: http://search.cpan.org//CPAN/authors/id/S/SA/SAPER/ExtUtils-FindFunctions-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Find functions in external libraries.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/ExtUtils::FindFunctions*
%doc %{_mandir}/man1/install-extutils-findfunctions*
%{_bindir}/install-extutils-findfunctions
%{perl_vendorlib}/ExtUtils/FindFunctions.pm

%changelog
* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Updated to release 0.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
