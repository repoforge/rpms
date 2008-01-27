# $Id$
# Authority: dag
# Upstream: Jason Long <jason$long,name>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-DKIM

Summary: Perl module to signs/verify Internet mail with DKIM/DomainKey signatures
Name: perl-Mail-DKIM
Version: 0.30.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-DKIM/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-DKIM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Mail-DKIM is a Perl module to signs/verify Internet mail
with DKIM/DomainKey signatures.

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
%doc ChangeLog Changes HACKING.DKIM MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Mail::DKIM.3pm*
%doc %{_mandir}/man3/Mail::DKIM::*.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/DKIM/
%{perl_vendorlib}/Mail/DKIM.pm

%changelog
* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.30.1-1
- Updated to release 0.30.1.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Fri May 25 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.24-1
- Initial package. (using DAR)
