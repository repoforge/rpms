# $Id$
# Authority: cmr
# Upstream: Paul Evans E<lt>leonerd$leonerd,org,ukE<gt>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-HexString

Summary: test binary strings with hex dump diagnostics
Name: perl-Test-HexString
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-HexString/

Source: http://www.cpan.org/modules/by-module/Test/Test-HexString-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)

%description
test binary strings with hex dump diagnostics.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Test::HexString.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/HexString/
%{perl_vendorlib}/Test/HexString.pm

%changelog
* Mon Jul 06 2009 Unknown - 0.01-1
- Initial package. (using DAR)
