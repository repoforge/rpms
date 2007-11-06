# $Id$
# Authority: dries
# Upstream: Adrian Howard <adrianh$quietstars,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Class

Summary: Easily create test classes in an xUnit/JUnit style
Name: perl-Test-Class
Version: 0.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Class/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADIE/Test-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Easily create test classes in an xUnit/JUnit style.

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
%{perl_vendorlib}/Test/Class.p*
%{perl_vendorlib}/Test/Class

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
