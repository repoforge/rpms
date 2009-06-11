# $Id$
# Authority: cmr
# Upstream: Michael Stevens <michael$etla,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-ListDetector

Summary: Mailing list message detector
Name: perl-Mail-ListDetector
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-ListDetector/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-ListDetector-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Mailing list message detector.

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
%doc AUTHORS BUGS Changes LICENSE MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/Mail::ListDetector*.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/ListDetector/
%{perl_vendorlib}/Mail/ListDetector.pm
%{perl_vendorlib}//auto/Mail/ListDetector/autosplit.ix

%changelog
* Thu Jun 11 2009 Unknown - 1.01-1
- Initial package. (using DAR)
