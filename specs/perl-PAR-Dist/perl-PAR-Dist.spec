# $Id$

# Authority: dries
# Upstream: autrijus$autrijus,org

%define real_name PAR-Dist
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Create and manipulate PAR distributions
Name: perl-PAR-Dist
Version: 0.22
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PAR-Dist/

Source: http://www.cpan.org/modules/by-module/PAR/PAR-Dist-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module, you can create and manipulate PAR distributions.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/PAR/Dist.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
