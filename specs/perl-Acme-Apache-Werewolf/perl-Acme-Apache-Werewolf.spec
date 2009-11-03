# $Id$
# Authority: dag
# Upstream: Rich Bowen <rbowen$rcbowen,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Apache-Werewolf

Summary: Perl module named Acme-Apache-Werewolf
Name: perl-Acme-Apache-Werewolf
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Apache-Werewolf/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Apache-Werewolf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-Apache-Werewolf is a Perl module.

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
%doc Changes LICENSE MANIFEST README Todo
%doc %{_mandir}/man3/Acme::Apache::Werewolf.3pm*
%dir %{perl_vendorlib}/Acme/
%dir %{perl_vendorlib}/Acme/Apache/
%{perl_vendorlib}/Acme/Apache/Werewolf.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
