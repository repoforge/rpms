# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exception-Class

Summary: Perl module that allows you to declare real exception classes
Name: perl-Exception-Class
Version: 1.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Exception-Class/

Source: http://www.cpan.org/modules/by-module/Exception/Exception-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Devel::StackTrace)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

%description
This module allows you to declare hierarchies of exception classes for use
in your code. It also provides a simple exception class that it uses as the
default base class for all other exceptions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL
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
%doc Changes LICENSE MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/Exception::Class*.3pm*
%dir %{perl_vendorlib}/Exception/
%{perl_vendorlib}/Exception/Class/
%{perl_vendorlib}/Exception/Class.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.29-1
- Updated to version 1.29.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 1.20-1
- Initial package. (using DAR)
