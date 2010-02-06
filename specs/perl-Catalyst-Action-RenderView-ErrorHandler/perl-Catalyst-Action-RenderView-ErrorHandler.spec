# $Id$
# Authority: dag
# Upstream: Andreas Marienborg  C<< <andreas@startsiden.no> >>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Action-RenderView-ErrorHandler

Summary: Custom errorhandling in deployed applications
Name: perl-Catalyst-Action-RenderView-ErrorHandler
Version: 0.100160
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Action-RenderView-ErrorHandler/

Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANDREMAR/Catalyst-Action-RenderView-ErrorHandler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::Action::RenderView)
BuildRequires: perl(Catalyst::Test)
BuildRequires: perl(Catalyst::View::TT)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FindBin)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Diff)
BuildRequires: perl(base)
Requires: perl(Carp)
Requires: perl(Catalyst)
Requires: perl(Catalyst::Action::RenderView)
Requires: perl(Catalyst::Test)
Requires: perl(Catalyst::View::TT)
Requires: perl(Class::Inspector)
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(FindBin)
Requires: perl(MRO::Compat)
Requires: perl(Moose)
Requires: perl(Moose::Role)
Requires: perl(Test::More)
Requires: perl(Text::Diff)
Requires: perl(base)

%filter_from_requires /^perl*/d
%filter_setup


%description
Custom errorhandling in deployed applications.

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
%doc %{_mandir}/man3/Catalyst::Action::RenderView::ErrorHandler.3pm*
%doc %{_mandir}/man3/Catalyst::Action::RenderView::ErrorHandler::Action.3pm.gz
%doc %{_mandir}/man3/Catalyst::Action::RenderView::ErrorHandler::Action::Log.3pm.gz

%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Action/
%dir %{perl_vendorlib}/Catalyst/Action/RenderView/
#%{perl_vendorlib}/Catalyst/Action/RenderView/ErrorHandler/
%{perl_vendorlib}/Catalyst/Action/RenderView/ErrorHandler.pm
%{perl_vendorlib}/Catalyst/Action/RenderView/ErrorHandler/Action.pm
%{perl_vendorlib}/Catalyst/Action/RenderView/ErrorHandler/Action/Log.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.100160-1
- Updated to version 0.100160.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.0105-1
- Initial package. (using DAR)
