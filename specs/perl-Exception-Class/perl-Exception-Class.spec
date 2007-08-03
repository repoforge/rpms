# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exception-Class

Summary: Exception-Class module for perl
Name: perl-Exception-Class
Version: 1.23
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Exception-Class/

Source: http://www.cpan.org/modules/by-module/Exception/Exception-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker), perl-Class-Data-Inheritable, perl-Devel-StackTrace

%description
This module allows you to declare hierarchies of exception classes for use
in your code. It also provides a simple exception class that it uses as the
default base class for all other exceptions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(444,root,root,755)
%doc Changes LICENSE README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Exception/
%{perl_vendorlib}/Exception/Class.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.22-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 1.20-1
- Initial package. (using DAR)
