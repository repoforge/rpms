# $Id$
# Authority: dag
# Upstream: Benjamin Franz <snowhare$nihongo,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Minimal

Summary: A lightweight CGI form processing package
Name: perl-CGI-Minimal
Version: 1.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Minimal/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Minimal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A lightweight CGI form processing package.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic_License.txt Changes GPL_License.txt LICENSE MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/CGI::Minimal.3pm*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Minimal/
%{perl_vendorlib}/CGI/Minimal.pm
%{perl_vendorlib}/CGI/Minimal.pod

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.29-1
- Initial package. (using DAR)
