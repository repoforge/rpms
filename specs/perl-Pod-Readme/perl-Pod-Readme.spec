# $Id$
# Authority: dag
# Upstream: Robert Rothenberg <rrwo at cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Readme

Summary: Convert POD to README file
Name: perl-Pod-Readme
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Readme/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Readme-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.005

%description
Convert POD to README file.

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
%doc %{_mandir}/man1/pod2readme.1*
%doc %{_mandir}/man3/Pod::Readme.3pm*
%{_bindir}/pod2readme
%dir %{perl_vendorlib}/Pod/
%{perl_vendorlib}/Pod/Readme.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
