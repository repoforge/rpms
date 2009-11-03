# $Id$
# Authority: dag
# Upstream: Tels <nospam-abuse@bloodgate.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name bignum

Summary: Transparent BigNumber support for Perl
Name: perl-bignum
Version: 0.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/bignum/

Source: http://www.cpan.org/authors/id/T/TE/TELS/math/bignum-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.2
#BuildRequires: perl(Test::More) >= 0.62
Requires: perl >= 1:5.6.2

%description
Transparent BigNumber support for Perl.

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
%doc BUGS CHANGES INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/bigint.3pm*
%doc %{_mandir}/man3/bignum.3pm*
%doc %{_mandir}/man3/bigrat.3pm*
%dir %{perl_vendorlib}/Math/
%dir %{perl_vendorlib}/Math/BigFloat/
%{perl_vendorlib}/Math/BigFloat/Trace.pm
%dir %{perl_vendorlib}/Math/BigInt/
%{perl_vendorlib}/Math/BigInt/Trace.pm
#%{perl_vendorlib}/bignum/
%{perl_vendorlib}/bigint.pm
%{perl_vendorlib}/bignum.pm
%{perl_vendorlib}/bigrat.pm

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
