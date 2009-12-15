# $Id$
# Authority: dag
# Upstream: Julian Mehnle <julian$mehnle,net>
# Upstream: Shevek <cpan$anarres,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SPF

Summary: Object-oriented implementation of Sender Policy Framework
Name: perl-Mail-SPF
Version: 2.007
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-SPF/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/mail-spf/Mail-SPF-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Error)
BuildRequires: perl(Module::Build) >= 0.2805
BuildRequires: perl(Net::DNS) >= 0.58
BuildRequires: perl(Net::DNS::Resolver::Programmable)
BuildRequires: perl(NetAddr::IP) >= 4
BuildRequires: perl(Test::More)
BuildRequires: perl(URI) >= 1.13
BuildRequires: perl >= v5.6
BuildRequires: perl(version)
Requires: perl(Error)
Requires: perl(Net::DNS) >= 0.58
Requires: perl(NetAddr::IP) >= 4
Requires: perl(URI) >= 1.13
Requires: perl >= v5.6
Requires: perl(version)

%filter_from_requires /^perl*/d
%filter_setup

%description
An object-oriented implementation of Sender Policy Framework.

%prep
%setup -n %{real_name}-v%{version}

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
%doc CHANGES INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO
%doc %{_mandir}/man1/spfquery.1*
%doc %{_mandir}/man3/Mail::SPF.3pm*
%doc %{_mandir}/man3/Mail::SPF::*.3pm*
%{_bindir}/spfquery
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/SPF/
%{perl_vendorlib}/Mail/SPF.pm

%changelog
* Tue Dec 15 2009 Christoph Maser <cmr@financial.com> - 2.007-1
- Updated to version 2.007.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 2.006-1
- Updated to release 2.006.

* Sun Aug 12 2007 Dag Wieers <dag@wieers.com> - 2.005-1
- Updated to release 2.005.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 2.004-1
- Initial package. (using DAR)
