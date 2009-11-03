# $Id$
# Authority: dag
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-CheckLib

Summary: Check that a library is available
Name: perl-Devel-CheckLib
Version: 0.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-CheckLib/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-CheckLib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Check that a library is available.

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
%doc CHANGES MANIFEST META.yml README TODO
%doc %{_mandir}/man1/use-devel-checklib.1*
%doc %{_mandir}/man3/Devel::CheckLib.3pm*
%{_bindir}/use-devel-checklib
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/CheckLib.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.6-1
- Updated to version 0.6.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
