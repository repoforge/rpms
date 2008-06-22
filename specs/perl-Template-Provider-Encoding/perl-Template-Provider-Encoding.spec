# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Provider-Encoding
%define real_version 0.02

Summary: Template plugin to specify encoding
Name: perl-Template-Provider-Encoding
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Provider-Encoding/

Source: http://www.cpan.org/modules/by-module/Template/Template-Provider-Encoding-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Template plugin to specify encoding.

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
%doc %{_mandir}/man3/Template::Plugin::encoding.3pm*
%doc %{_mandir}/man3/Template::Provider::Encoding.3pm*
%doc %{_mandir}/man3/Template::Stash::ForceUTF8.3pm*
%dir %{perl_vendorlib}/Template/
%dir %{perl_vendorlib}/Template/Plugin/
%{perl_vendorlib}/Template/Plugin/encoding.pm
%dir %{perl_vendorlib}/Template/Provider/
#%{perl_vendorlib}/Template/Provider/Encoding/
%{perl_vendorlib}/Template/Provider/Encoding.pm
%dir %{perl_vendorlib}/Template/Stash/
%{perl_vendorlib}/Template/Stash/ForceUTF8.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
