# $Id$
# Authority: cmr
# Upstream: GomoR <perl$gomor,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Frame

Summary: the base framework for frame crafting
Name: perl-Net-Frame
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Frame/

Source: http://www.cpan.org/modules/by-module/Net/Net-Frame-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
the base framework for frame crafting.

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
%doc Changes LICENSE LICENSE.Artistic MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Net::Frame*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Frame/
%{perl_vendorlib}/Net/Frame.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Tue Jan 06 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Initial package. (using DAR)
