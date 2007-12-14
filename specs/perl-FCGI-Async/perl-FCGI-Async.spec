# $Id$
# Authority: dries
# Upstream: Paul Evans <leonerd$leonerd,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FCGI-Async

Summary: Module to allow use of FastCGI asynchronously
Name: perl-FCGI-Async
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FCGI-Async/

Source: http://www.cpan.org/modules/by-module/FCGI/FCGI-Async-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Module to allow use of FastCGI asynchronously.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README fcgi-spec.html examples/
%doc %{_mandir}/man3/FCGI::Async.3pm*
%doc %{_mandir}/man3/FCGI::Async::*.3pm*
%dir %{perl_vendorlib}/FCGI/
%{perl_vendorlib}/FCGI/Async/
%{perl_vendorlib}/FCGI/Async.pm

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
