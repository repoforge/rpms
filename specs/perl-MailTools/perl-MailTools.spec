# $Id$
# Authority: dag
# Upstream: Mark Overmeer <perl$overmeer,net>

### EL6 ships with perl-MailTools-2.04-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MailTools

Summary: Various Mail related modules
Name: perl-MailTools
Version: 2.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MailTools/

Source: http://www.cpan.org/authors/id/M/MA/MARKOV/MailTools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: perl-Mail

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Date::Format)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(Net::Domain) >= 1.05
BuildRequires: perl(Net::SMTP) >= 1.03
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod) >= 1
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(Date::Format)
Requires: perl(Date::Parse)
Requires: perl(IO::Handle)
Requires: perl(Net::Domain) >= 1.05
Requires: perl(Net::SMTP) >= 1.03
Requires: perl(Test::More)
Requires: perl(Test::Pod) >= 1

%filter_from_requires /^perl*/d
%filter_setup

%description
Various Mail related modules.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README README.demos examples/
%doc %{_mandir}/man3/Mail::*.3pm*
%{perl_vendorlib}/Mail/

%changelog
* Fri Oct 01 2010 David Hrbáč <david@hrbac.cz> - 2.07-1
- new upstream release

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.77-1
- Updated to release 1.77.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.76-1
- Updated to release 1.76.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.74-1
- Updated to release 1.74.

* Tue Nov  8 2005 Matthias Saou <http://freshrpms.net/> 1.67-2
- Fix RH7 perl-libnet dependency.

* Sat Jun 19 2005 Dries Verachtert <dries@ulyssis.org> - 1.67-1
- Updated to release 1.67.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 1.66-1
- Updated to release 1.66.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.64-0
- Updated to release 1.64.

* Fri Nov 28 2003 Dag Wieers <dag@wieers.com> - 1.60-0
- Updated to release 1.60.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.58-0
- Updated to release 1.58.

* Sun Jan 23 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)

