# $Id$
# Authority: dag
# Upstream: Vipul Ved Prakash <mail$vipul,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Persistent

Summary: Transparent state persistence for CGI applications
Name: perl-CGI-Persistent
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Persistent/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Persistent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Transparent state persistence for CGI applications.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/CGI::Persistent.3pm*
%dir %{perl_vendorlib}/CGI/
#%{perl_vendorlib}/CGI/Persistent/
%{perl_vendorlib}/CGI/Persistent.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
