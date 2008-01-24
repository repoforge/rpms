# $Id$
# Authority: dag
# Upstream: Stevan Little E<lt>stevan,little$iinteractive,comE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Params-Validate

Summary: an extension of Params::Validate for using Moose's types
Name: perl-MooseX-Params-Validate
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Params-Validate/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-Params-Validate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Exception) >= 0.21
#BuildRequires: perl(Test::More) >= 0.62

%description
an extension of Params::Validate for using Moose's types.

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/MooseX::Params::Validate.3pm*
%dir %{perl_vendorlib}/MooseX/
%dir %{perl_vendorlib}/MooseX/Params/
%{perl_vendorlib}/MooseX/Params/Validate.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
