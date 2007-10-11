# $Id$
# Authority: dag
# Upstream: The Catalyst Core Team - see http://catalyst.perl.org/

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Devel

Summary: Catalyst Development Tools
Name: perl-Catalyst-Devel
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Devel/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Devel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Catalyst Development Tools.

This package contains the following Perl module:

    Catalyst::Devel

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Catalyst::Devel.3pm*
%doc %{_mandir}/man3/Catalyst::Helper.3pm*
%doc %{_mandir}/man3/Module::Install::Catalyst.3pm*
%dir %{perl_vendorlib}/Catalyst/
%{perl_vendorlib}/Catalyst/Devel.pm
%{perl_vendorlib}/Catalyst/Helper.pm
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install/Catalyst.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
