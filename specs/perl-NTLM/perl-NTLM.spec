# $Id$
# Authority: dag
# Upstream: David (Buzz) Bussenschutt <davidbuzz$gmail,com>
# Upstreal: Mark Bush <Mark,Bush$bushnet,demon,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name NTLM

Summary: NTLM authentication module
Name: perl-NTLM
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NTLM/

Source: http://www.cpan.org/authors/id/B/BU/BUZZ/NTLM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
NTLM authentication module.

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
%doc %{_mandir}/man3/Authen::NTLM.3pm*
%dir %{perl_vendorlib}/Authen/
%{perl_vendorlib}/Authen/NTLM/
%{perl_vendorlib}/Authen/NTLM.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
