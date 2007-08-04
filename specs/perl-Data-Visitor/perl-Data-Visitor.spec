# $Id$
# Authority: dag
# Upstream: יובל קוג'מן (Yuval Kogman) <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Visitor

Summary: None
Name: perl-Data-Visitor
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Visitor/

Source: http://www.cpan.org/modules/by-module/Data/Data-Visitor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
None.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml SIGNATURE
%doc %{_mandir}/man3/Data::Visitor.3pm*
%doc %{_mandir}/man3/Data::Visitor::Callback.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Visitor/
%{perl_vendorlib}/Data/Visitor.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
