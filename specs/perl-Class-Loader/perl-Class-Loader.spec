# $Id$
# Authority: dries
# Upstream: Vipul Ved Prakash <mail$vipul,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Loader

Summary: Load modules and create objects on demand
Name: perl-Class-Loader
Version: 2.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Loader/

Source: http://search.cpan.org/CPAN/authors/id/V/VI/VIPUL/Class-Loader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Load modules and create objects on demand.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Class/Loader.pm
%{perl_vendorlib}/Class/LoaderTest.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Updated to release 2.03.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.
