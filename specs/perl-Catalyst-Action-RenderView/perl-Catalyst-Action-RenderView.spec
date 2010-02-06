# $Id$
# Authority: dag
# Upstream: Tomas Doran <bobtfish@bobtfish.net>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Action-RenderView

Summary: Sensible default end action
Name: perl-Catalyst-Action-RenderView
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Action-RenderView/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-Action-RenderView-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Runtime) >= 5.70
BuildRequires: perl(Data::Visitor) >= 0.24
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request::AsCGI)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Test::More)
Requires: perl(Catalyst::Runtime) >= 5.70
Requires: perl(Data::Visitor) >= 0.24
Requires: perl(MRO::Compat)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
Sensible default end action.

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
%doc %{_mandir}/man3/Catalyst::Action::RenderView.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Action/
#%{perl_vendorlib}/Catalyst/Action/RenderView/
%{perl_vendorlib}/Catalyst/Action/RenderView.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.14-1
- Updated to version 0.14.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
