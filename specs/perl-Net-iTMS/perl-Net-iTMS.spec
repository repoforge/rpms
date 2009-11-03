# $Id$
# Authority: dag
# Upstream: Thomas Sibley, http://zulutango,org:82/

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-iTMS

Summary: Interface to the iTunes Music Store (iTMS)
Name: perl-Net-iTMS
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-iTMS/

Source: http://www.cpan.org/modules/by-module/Net/Net-iTMS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)

%description
Interface to the iTunes Music Store (iTMS).

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
%doc ChangeLog INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Net::iTMS.3pm*
%doc %{_mandir}/man3/Net::iTMS::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/iTMS/
%{perl_vendorlib}/Net/iTMS.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
