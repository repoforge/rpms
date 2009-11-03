# $Id$
# Authority: cmr
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Default

Summary: Static calls apply to a default instantiation
Name: perl-Class-Default
Version: 1.51
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Default/

Source: http://www.cpan.org/modules/by-module/Class/Class-Default-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Static calls apply to a default instantiation.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Class::Default.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Default/
%{perl_vendorlib}/Class/Default.pm

%changelog
* Thu Jul 09 2009 Christoph Maser <cmr@financial.com> - 1.51-1
- Initial package. (using DAR)
