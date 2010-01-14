# $Id$
# Authority: cmr
# Upstream: Guillermo Roditi (groditi) <groditi@cpan.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Component-InstancePerContext

Summary: Moose role to create only one instance of component per context
Name: perl-Catalyst-Component-InstancePerContext
Version: 0.001001
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Component-InstancePerContext/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Component-InstancePerContext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst)
BuildRequires: perl(Moose)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
Requires: perl(Catalyst)
Requires: perl(Moose)
Requires: perl(Scalar::Util)

%filter_from_requires /^perl*/d
%filter_setup

%description
Moose role to create only one instance of component per context.

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
%doc %{_mandir}/man3/Catalyst::Component::InstancePerContext.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Component/
#%{perl_vendorlib}/Catalyst/Component/InstancePerContext/
%{perl_vendorlib}/Catalyst/Component/InstancePerContext.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.001001-1
- Initial package. (using DAR)
