# $Id$
# Authority: dag
# Upstream: Randy Kobes <r,kobes$uwinnipeg,ca>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-Command

Summary: Utilities to replace common UNIX commands in Makefiles
Name: perl-ExtUtils-Command
Version: 1.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-Command/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-Command-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Utilities to replace common UNIX commands in Makefiles.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/ExtUtils::Command.3pm*
%doc %{_mandir}/man3/Shell::Command.3pm*
%dir %{perl_vendorlib}/ExtUtils/
#%{perl_vendorlib}/ExtUtils/Command/
%{perl_vendorlib}/ExtUtils/Command.pm
%dir %{perl_vendorlib}/Shell/
%{perl_vendorlib}/Shell/Command.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.16-1
- Updated to version 1.16.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
