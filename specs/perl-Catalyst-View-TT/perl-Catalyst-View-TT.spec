# $Id$
# Authority: dag
# Upstream: Marcus Ramberg <mramberg$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-View-TT

Summary: Template View Class
Name: perl-Catalyst-View-TT
Version: 0.25
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-View-TT/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-View-TT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst) >= 5.7
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Template)
BuildRequires: perl(Template::Timer)

%description
Template View Class.

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
%doc %{_mandir}/man3/Catalyst::View::TT.3pm*
%doc %{_mandir}/man3/Catalyst::Helper::View::TT.3pm*
%doc %{_mandir}/man3/Catalyst::Helper::View::TTSite.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/View/
#%{perl_vendorlib}/Catalyst/View/TT/
%{perl_vendorlib}/Catalyst/View/TT.pm
%dir %{perl_vendorlib}/Catalyst/Helper/
%dir %{perl_vendorlib}/Catalyst/Helper/View/
%{perl_vendorlib}/Catalyst/Helper/View/TT.pm
%{perl_vendorlib}/Catalyst/Helper/View/TTSite.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.25-1
- Initial package. (using DAR)
