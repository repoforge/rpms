# $Id$
# Authority: dag
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-File

Summary: Check file attributes
Name: perl-Test-File
Version: 1.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-File/

Source: http://www.cpan.org/modules/by-module/Test/Test-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Check file attributes.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Test::File.3*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/File/
%{perl_vendorlib}/Test/File.pm

%changelog
* Thu Sep 20 2012 Peter Eisentraut <peter@eisentraut.org> - 1.34-1
- Updated to version 1.34.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.29-1
- Updated to version 1.29.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.18-1
- Initial package. (using DAR)
