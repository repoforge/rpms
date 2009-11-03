# $Id$
# Authority: dries
# Upstream: Kentaro Kuribayashi <kentaro$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Plugin-Shorten

Summary: Template plugin to shorten/lengthen URLs
Name: perl-Template-Plugin-Shorten
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Plugin-Shorten/

Source: http://www.cpan.org/modules/by-module/Template/Template-Plugin-Shorten-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Template plugin to shorten/lengthen URLs.

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
%doc Changes README
%doc %{_mandir}/man3/Template::Plugin::Shorten*
%{perl_vendorlib}/Template/Plugin/Shorten.pm
%dir %{perl_vendorlib}/Template/Plugin/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
