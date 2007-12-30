# $Id$
# Authority: dag
# Upstream: Andreas Marienborg  C<< <andreas@startsiden.no> >>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Action-RenderView-ErrorHandler

Summary: Custom errorhandling in deployed applications
Name: perl-Catalyst-Action-RenderView-ErrorHandler
Version: 0.0105
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Action-RenderView-ErrorHandler/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Action-RenderView-ErrorHandler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Action::RenderView)
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Catalyst::View::TT) >= 0.25
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(FindBin)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Diff)

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
%doc Changes MANIFEST MANIFEST.bak MANIFEST.skip META.yml README
%doc %{_mandir}/man3/Catalyst::Action::RenderView::ErrorHandler.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Action/
%dir %{perl_vendorlib}/Catalyst/Action/RenderView/
#%{perl_vendorlib}/Catalyst/Action/RenderView/ErrorHandler/
%{perl_vendorlib}/Catalyst/Action/RenderView/ErrorHandler.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.0105-1
- Initial package. (using DAR)
