# $Id$
# Authority: dag
# Upstream: Jörn Reder <joern$zyn,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-GPG
%define real_version 1.000006

Summary: Handling of GnuPG encrypted / signed mails
Name: perl-Mail-GPG
Version: 1.0.6
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-GPG/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-GPG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Handling of GnuPG encrypted / signed mails.

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
%doc %{_mandir}/man3/Mail::GPG.3pm*
%doc %{_mandir}/man3/Mail::GPG::Result.3pm*
%{_bindir}/mgpg-test
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/GPG/
%{perl_vendorlib}/Mail/GPG.pm

%changelog
* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Initial package. (using DAR)
