# $Id$
# Authority: dag
# Upstream: Igor Chudov <ichudov$algebra,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-eBay

Summary: Perl Interface to XML based eBay API
Name: perl-Net-eBay
Version: 0.46
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-eBay/

Source: http://www.cpan.org/modules/by-module/Net/Net-eBay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl Interface to XML based eBay API.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__mv} -vf %{buildroot}%{perl_vendorlib}/Net/ebay*.pl %{buildroot}%{_bindir}
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::eBay.3pm*
%{_bindir}/ebay-add-item.pl
%{_bindir}/ebay-end-item-early.pl
%{_bindir}/ebay-get-categories.pl
%{_bindir}/ebay-get-item.pl
%{_bindir}/ebay-get-my-selling.pl
%{_bindir}/ebay-get-seller-list.pl
%{_bindir}/ebay-get-suggested-categories.pl
%{_bindir}/ebay-leave-feedback.pl
%{_bindir}/ebay-official-time.pl
%{_bindir}/ebay-revise-item.pl
%{_bindir}/ebay-search.pl
%{_bindir}/ebay-validate-test-user.pl
%dir %{perl_vendorlib}/Net/
#%{perl_vendorlib}/Net/eBay/
%{perl_vendorlib}/Net/eBay.pm

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.46-1
- Updated to release 0.46.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.45-1
- Initial package. (using DAR)
