# $Id$
# Authority: dag
# Upstream: Benjamin Franz <snowhare$nihongo,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-PathInfo

Summary: Lightweight CGI processing package for using PATH_INFO like GET method form parameters
Name: perl-CGI-PathInfo
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-PathInfo/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-PathInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A lightweight CGI processing package for using PATH_INFO like
GET method form parameters.

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
%doc Artistic_License.txt Changes GPL_License.txt LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/CGI::PathInfo.3pm*
%dir %{perl_vendorlib}/CGI/
#%{perl_vendorlib}/CGI/PathInfo/
%{perl_vendorlib}/CGI/PathInfo.pm
%{perl_vendorlib}/CGI/PathInfo.pod

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
