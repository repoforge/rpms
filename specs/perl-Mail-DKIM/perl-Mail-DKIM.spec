# $Id$
# Authority: dag
# Upstream: Jason Long <jason$long,name>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-DKIM

Summary: Perl module to signs/verify Internet mail with DKIM/DomainKey signatures
Name: perl-Mail-DKIM
Version: 0.37
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-DKIM/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-DKIM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Crypt::OpenSSL::RSA) >= 0.24
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Mail::Address)
BuildRequires: perl(Net::DNS)
BuildRequires: perl(Test::Simple)


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
* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.37-1
- Updated to version 0.37.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.36-1
- Updated to version 0.36.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

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
