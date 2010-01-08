# $Id$
# Authority: dag
# Upstream: Tomas Doran <bobtfish@bobtfish.net>
# ExcludeDist: el4  <- inherited by Catalyst::Runtime

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-View-TT

Summary: Template View Class
Name: perl-Catalyst-View-TT
Version: 0.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-View-TT/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-View-TT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst) >= 5.7
BuildRequires: perl(Class::Accessor)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Template)
BuildRequires: perl(Template::Timer)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.8.1
Requires: perl(Catalyst) >= 5.7
Requires: perl(Class::Accessor)
Requires: perl(MRO::Compat)
Requires: perl(Path::Class)
Requires: perl(Template)
Requires: perl(Template::Timer)
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup


%description
Template View Class.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 0.31-1
- Updated to version 0.31.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.25-1
- Initial package. (using DAR)
