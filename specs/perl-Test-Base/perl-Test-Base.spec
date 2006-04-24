# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Base

Summary: Data driven testing framework for perl
Name: perl-Test-Base
Version: 0.50
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Base/

Source: http://www.cpan.org/modules/by-module/Test/Test-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A data driven testing framework.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install/TestBase.pm
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Base.pm
%{perl_vendorlib}/Test/Base/

%changelog
* Mon Apr 24 2006 Dag Wieers <dag@wieers.com> - 0.50-1
- Initial package.
