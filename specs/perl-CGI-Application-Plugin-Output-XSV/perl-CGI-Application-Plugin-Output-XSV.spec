# $Id$
# Authority: dries
# Upstream: Evan A, Zacks <zackse$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Application-Plugin-Output-XSV

Summary: Produce csv output from a CGI::Application runmode
Name: perl-CGI-Application-Plugin-Output-XSV
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Application-Plugin-Output-XSV/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Application-Plugin-Output-XSV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Generate csv output from a CGI::Application runmode.

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
%doc Changes MANIFEST MANIFEST.skip META.yml README
%doc %{_mandir}/man3/CGI::Application::Plugin::Output::XSV.3pm*
%dir %{perl_vendorlib}/CGI/
%dir %{perl_vendorlib}/CGI/Application/
%dir %{perl_vendorlib}/CGI/Application/Plugin/
%dir %{perl_vendorlib}/CGI/Application/Plugin/Output/
#%{perl_vendorlib}/CGI/Application/Plugin/Output/XSV/
%{perl_vendorlib}/CGI/Application/Plugin/Output/XSV.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Initial package.
